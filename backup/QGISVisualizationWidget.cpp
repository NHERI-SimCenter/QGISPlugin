#include "QGISVisualizationWidget.h"

#include <QToolBar>
#include <QSplitter>
#include <QLabel>
#include <QAuthenticator>

// QGIS Includes
#include <qgsapplication.h>
#include <qgsproviderregistry.h>
#include <qgssinglesymbolrenderer.h>
#include <qgsvectorlayer.h>
#include <qgsmapcanvas.h>
#include <qgsprojecttimesettings.h>
#include <qgsmeshlayer.h>
#include <qgsvectortilelayer.h>
#include <qgsmaplayertemporalproperties.h>
#include <qgsmeshlayertemporalproperties.h>
#include <qgsauthguiutils.h>
#include <qgsauthmanager.h>
#include <qgsproviderutils.h>
#include <qgsprovidersublayerdetails.h>
#include <qgsprovidersublayersdialog.h>
#include <qgsmaplayerfactory.h>
#include <qgsrasterlayer.h>
#include <qgslayertree.h>
#include <qgsdatumtransformdialog.h>
#include <qgsxyzsourceselect.h>
#include <qgsdatasourcemanagerdialog.h>
#include <qgszipitem.h>
#include <qgslayertreeview.h>
#include <qgsruntimeprofiler.h>
#include <qgsbrowserguimodel.h>
#include <qgslayertreemodel.h>
#include <qgsgui.h>
#include <qgssourceselectproviderregistry.h>
#include <qgsnetworkaccessmanager.h>
#include <qgsappauthrequesthandler.h>
#include <qgsappsslerrorhandler.h>
#include <qgsmessagebaritem.h>
#include <qgsdockwidget.h>
#include <qgsmessagebar.h>
#include <qgsmessagelogviewer.h>
#include <qgscredentials.h>
#include <qgsmapcanvasdockwidget.h>
#include <qgslayertreemapcanvasbridge.h>
#include <qgsannotationmanager.h>
#include <qgsannotationitem.h>
#include <qgsmapcanvasannotationitem.h>
#include <qgsvectorlayerdigitizingproperties.h>
#include <qgscredentialdialog.h>
#include <qgswmsprovider.h>
#include <qgswmsprovidergui.h>
#include <qgsdataitemguiproviderregistry.h>
#include <qgsinbuiltdataitemproviders.h>
#include <qgsoptions.h>
#include <qgsproxyprogresstask.h>
#include <qgsmessageviewer.h>
#include <qgsmasterlayoutinterface.h>
#include <qgslayoutmanager.h>
#include <qgsstatusbarscalewidget.h>
#include <qgsappmaptools.h>
#include <qgsmeasuretool.h>
#include <qgsmaptoolmeasureangle.h>
#include <qgsmaptoolmeasurebearing.h>
#include <qgsstatusbarmagnifierwidget.h>

//#include <qgsnetworklogger.h>

// QGIS Map tools
#include "qgsmaptoolpan.h"
#include "qgsmaptoolzoom.h"

#include <memory>
#include <utility>
#include <QMessageBox>

// These are the other headers for available map tools (not used in this example)
//#include "qgsmaptoolcapture.h"
//#include "qgsmaptoolidentify.h"
//#include "qgsmaptoolselect.h"
//#include "qgsmaptoolvertexedit.h"
//#include "qgsmeasure.h"

QGISVisualizationWidget *QGISVisualizationWidget::sInstance = nullptr;

QGISVisualizationWidget::QGISVisualizationWidget(QWidget* parent, Qt::WindowFlags fl) : QMainWindow( parent, fl )
{
    if (sInstance)
    {
        QMessageBox::critical(
                    this,
                    tr( "Multiple Instances of QgisApp" ),
                    tr( "Multiple instances of QGIS application object detected.\nPlease contact the developers.\n" ) );
        abort();
    }

    sInstance = this;

    QgsRuntimeProfiler *profiler = QgsApplication::profiler();

    // start the network logger early, we want all requests logged!
    //     startProfile( tr( "Create network logger" ) );
    //     mNetworkLogger = new QgsNetworkLogger( QgsNetworkAccessManager::instance(), this );
    //     endProfile();

    setDockOptions(dockOptions() | QMainWindow::GroupedDragging);

    //    startProfile( tr( "Checking user database" ) );
    //    qDebug()<< tr( "Checking database" );
    //    qApp->processEvents();
    //    // Do this early on before anyone else opens it and prevents us copying it
    //    QString dbError;
    //    if ( !QgsApplication::createDatabase( &dbError ) )
    //    {
    //      QMessageBox::critical( this, tr( "Private qgis.db" ), dbError );
    //    }
    //    endProfile();


    QgsApplication::initQgis();
    if ( !QgsApplication::authManager()->isDisabled() )
    {
        // Most of the auth initialization is now done inside initQgis, no need to profile here
        masterPasswordSetup();
    }

    QgsSettings settings;



    // **** Map Canvas
    startProfile( tr( "Creating map canvas" ) );
    mMapCanvas = new QgsMapCanvas(this);
    mMapCanvas->setObjectName( QStringLiteral( "theMapCanvas" ) );


    this->setCentralWidget(mMapCanvas);
    QGridLayout *centralLayout = new QGridLayout( );
    mMapCanvas->setLayout( centralLayout );
    centralLayout->setContentsMargins( 0, 0, 0, 0 );


    // before anything, let's freeze canvas redraws
    QgsCanvasRefreshBlocker refreshBlocker;

    connect(mMapCanvas, &QgsMapCanvas::messageEmitted, this, &QGISVisualizationWidget::displayMessage);

    if ( settings.value( QStringLiteral( "qgis/main_canvas_preview_jobs" ) ).isNull() )
    {
        // So that it appears in advanced settings
        settings.setValue( QStringLiteral( "qgis/main_canvas_preview_jobs" ), true );
    }
    mMapCanvas->setPreviewJobsEnabled( settings.value( QStringLiteral( "qgis/main_canvas_preview_jobs" ), true ).toBool() );

    // set canvas color right away
    int myRed = settings.value( QStringLiteral( "qgis/default_canvas_color_red" ), 255 ).toInt();
    int myGreen = settings.value( QStringLiteral( "qgis/default_canvas_color_green" ), 255 ).toInt();
    int myBlue = settings.value( QStringLiteral( "qgis/default_canvas_color_blue" ), 255 ).toInt();
    mMapCanvas->setCanvasColor( QColor( myRed, myGreen, myBlue ) );
    mMapCanvas->setCanvasColor( Qt::white );

    // set project linked to main canvas
    mMapCanvas->setProject( QgsProject::instance() );

    applyDefaultSettingsToCanvas(mMapCanvas);

    //    mCanvasDock = new QgsDockWidget(tr("Map Canvas"), this);
    //    mCanvasDock->setObjectName( QStringLiteral( "MapCanvas" ) );
    //    mCanvasDock->setAllowedAreas( Qt::RightDockWidgetArea );
    //    addDockWidget(Qt::RightDockWidgetArea, mCanvasDock);
    //    mCanvasDock->setWidget(mMapCanvas);

    mMapCanvas->show();
    mMapCanvas->setFocus();

    centralLayout->addWidget( mMapCanvas, 0, 0, 2, 1 );

    endProfile();


    // a bar to warn the user with non-blocking messages
    startProfile( tr( "Message bar" ) );
    mInfoBar = new QgsMessageBar( this );
    mInfoBar->setSizePolicy( QSizePolicy::Minimum, QSizePolicy::Fixed );
    centralLayout->addWidget( mInfoBar, 0, 0, 1, 1 );
    endProfile();


    // ** Layer tree

    startProfile( tr( "Layer tree" ) );
    mLayerTreeView = new QgsLayerTreeView( this );
    mLayerTreeView->setObjectName( QStringLiteral( "theLayerTreeView" ) ); // "theLayerTreeView" used to find this canonical instance later
    endProfile();

    QgsLayerTreeModel *model = new QgsLayerTreeModel( QgsProject::instance()->layerTreeRoot(), this );
    model->setFlag(QgsLayerTreeModel::AllowNodeReorder);
    model->setFlag(QgsLayerTreeModel::AllowNodeRename);
    model->setFlag(QgsLayerTreeModel::AllowNodeChangeVisibility);
    model->setFlag(QgsLayerTreeModel::ShowLegendAsTree);
    model->setFlag(QgsLayerTreeModel::UseEmbeddedWidgets);
    model->setFlag(QgsLayerTreeModel::UseTextFormatting);
    model->setAutoCollapseLegendNodes(10);

    mLayerTreeView->setModel( model );
    mLayerTreeView->setMessageBar( mInfoBar );

    auto layersDock = new QgsDockWidget(tr("Map Layers"), this);
    layersDock->setObjectName( QStringLiteral( "LayersTree" ) );
    layersDock->setAllowedAreas( Qt::LeftDockWidgetArea );
    addDockWidget(Qt::LeftDockWidgetArea, layersDock);
    layersDock->setWidget( mLayerTreeView );

    endProfile();




    // initialize the plugin manager
    //    startProfile( tr( "Plugin manager" ) );
    //    mPluginManager = new QgsPluginManager( this, true );
    //    endProfile();

    //    registerMapLayerPropertiesFactory( new QgsVectorLayerDigitizingPropertiesFactory( this ) );
    //     registerMapLayerPropertiesFactory( new QgsPointCloudRendererWidgetFactory( this ) );
#ifdef HAVE_3D
    registerMapLayerPropertiesFactory( new QgsVectorLayer3DRendererWidgetFactory( this ) );
    registerMapLayerPropertiesFactory( new QgsMeshLayer3DRendererWidgetFactory( this ) );
    registerMapLayerPropertiesFactory( new QgsPointCloudLayer3DRendererWidgetFactory( this ) );
#endif
    //     registerMapLayerPropertiesFactory( new QgsPointCloudElevationPropertiesWidgetFactory( this ) );

    new QgsCredentialDialog( this );


    //     mLocatorWidget->setMapCanvas( mMapCanvas );
    //     connect( mLocatorWidget, &QgsLocatorWidget::configTriggered, this, [ = ] { showOptionsDialog( this, QStringLiteral( "mOptionsLocatorSettings" ) ); } );

    // set QGIS specific srs validation
    //     connect( this, &QGISVisualizationWidget::customCrsValidation,
    //              this, &QGISVisualizationWidget::validateCrs );
    //     QgsCoordinateReferenceSystem::setCustomCrsValidation(customSrsValidation_);


    namSetup();

    ///*************


    //    startProfile( tr( "Layer tree" ) );
    //    mLayerTreeView = new QgsLayerTreeView( this );
    //    mLayerTreeView->setObjectName( QStringLiteral( "theLayerTreeView" ) ); // "theLayerTreeView" used to find this canonical instance later
    //    endProfile();

    //    QgsLayerTreeModel *model = new QgsLayerTreeModel( QgsProject::instance()->layerTreeRoot(), this );
    //    model->setFlag(QgsLayerTreeModel::AllowNodeReorder);
    //    model->setFlag(QgsLayerTreeModel::AllowNodeRename);
    //    model->setFlag(QgsLayerTreeModel::AllowNodeChangeVisibility);
    //    model->setFlag(QgsLayerTreeModel::ShowLegendAsTree);
    //    model->setFlag(QgsLayerTreeModel::UseEmbeddedWidgets);
    //    model->setFlag(QgsLayerTreeModel::UseTextFormatting);
    //    model->setAutoCollapseLegendNodes(10);

    //    mLayerTreeView->setModel( model );
    //    mLayerTreeView->setMessageBar( mInfoBar );

    //    auto label = new QLabel("Test");
    //    mpLayout->addWidget(mLayerTreeView);
    //    mpLayout->addWidget(mMapCanvas);

    //    mpLayout->setStretchFactor(1,1);

        mBrowserModel = new QgsBrowserGuiModel( this );

    //    mLogViewer = new QgsMessageLogViewer( this );

    //    mLogDock = new QgsDockWidget( tr( "Log Messages" ), this );
    //    mLogDock->setObjectName( QStringLiteral( "MessageLog" ) );
    //    mLogDock->setAllowedAreas( Qt::AllDockWidgetAreas );
    //    addDockWidget( Qt::BottomDockWidgetArea, mLogDock );
    //    mLogDock->setWidget( mLogViewer );
    //    mLogDock->hide();

    //    mBrowserWidget = new QgsBrowserDockWidget( tr( "Browser" ), mBrowserModel, this );
    //    mBrowserWidget->setObjectName( QStringLiteral( "Browser" ) );
    //    mBrowserWidget->setMessageBar( mInfoBar );

        QgsGui::instance()->dataItemGuiProviderRegistry()->addProvider( new QgsAppDirectoryItemGuiProvider() );
          QgsGui::instance()->dataItemGuiProviderRegistry()->addProvider( new QgsAppFileItemGuiProvider() );
          QgsGui::instance()->dataItemGuiProviderRegistry()->addProvider( new QgsProjectHomeItemGuiProvider() );
          QgsGui::instance()->dataItemGuiProviderRegistry()->addProvider( new QgsProjectItemGuiProvider() );
          QgsGui::instance()->dataItemGuiProviderRegistry()->addProvider( new QgsFavoritesItemGuiProvider() );
          QgsGui::instance()->dataItemGuiProviderRegistry()->addProvider( new QgsLayerItemGuiProvider() );
//          QgsGui::instance()->dataItemGuiProviderRegistry()->addProvider( new QgsBookmarksItemGuiProvider() );
          QgsGui::instance()->dataItemGuiProviderRegistry()->addProvider( new QgsFieldsItemGuiProvider() );
          QgsGui::instance()->dataItemGuiProviderRegistry()->addProvider( new QgsFieldItemGuiProvider() );
          QgsGui::instance()->dataItemGuiProviderRegistry()->addProvider( new QgsDatabaseItemGuiProvider() );


//        QgsWmsProviderGuiMetadata
//        qgswmsprovidergui

//        QgsWmsProvider
//qgswmsprovider
//        auto dsWidget = this->createDataSourceWidget();
//        QgsGui::sourceSelectProviderRegistry()->addProvider(dsWidget);

       // show the virtual layer dialog
        QDialog *dts = dynamic_cast<QDialog *>( QgsGui::sourceSelectProviderRegistry()->createSelectionWidget( QStringLiteral( "XYZ" ), this, Qt::Widget, QgsProviderRegistry::WidgetMode::Embedded ) );
        if ( !dts )
        {
          QMessageBox::warning( this, tr( "Add Virtual Layer" ), tr( "Cannot get virtual layer select dialog from provider." ) );
          return;
        }

        dts->exec();


//        dataSourceManager();

    //    QgsGui::sourceSelectProviderRegistry()->addProvider();

    //    auto createdWidget = QgsGui::sourceSelectProviderRegistry()->createSelectionWidget( QStringLiteral( "xyz" ), this, Qt::Widget, QgsProviderRegistry::WidgetMode::Embedded );
    //createdWidget->show();

    //    auto dsWidget = this->createDataSourceWidget();
    //    dsWidget->show();


//    auto rasterLayer = new QgsRasterLayer("/Users/steve/Downloads/raster_layer.tiff");
//    QgsProject::instance()->addMapLayer(rasterLayer);
//    mMapCanvas->setExtent(rasterLayer->extent());
//    QList<QgsMapLayer *> rasterLst{rasterLayer};
//    mMapCanvas->setLayers(rasterLst);
}


QString QGISVisualizationWidget::saveAsFile( QgsMapLayer *layer, const bool onlySelected, const bool defaultToAddToMap )
{

  return QString();
}


QString QGISVisualizationWidget::saveAsRasterFile( QgsRasterLayer *rasterLayer, const bool defaultAddToCanvas )
{

  return QString();
}

QgsMessageBar *QGISVisualizationWidget::visibleMessageBar()
{
  if ( mDataSourceManagerDialog &&
       mDataSourceManagerDialog->isVisible() &&
       mDataSourceManagerDialog->isModal() )
  {
    return mDataSourceManagerDialog->messageBar();
  }
  else
  {
    return messageBar();
  }
}


void QGISVisualizationWidget::handleDropUriList( const QgsMimeDataUtils::UriList &lst )
{
  // avoid unnecessary work when adding lots of layers at once - defer emitting the active layer changed signal until we've
  // added all layers, and only emit the signal once for the final layer added
  mBlockActiveLayerChanged = true;

  QgsScopedProxyProgressTask task( tr( "Loading layers" ) );

  auto showLayerLoadWarnings = [ = ]( const QString & title, const QString & shortMessage, const QString & longMessage, Qgis::MessageLevel level )
  {
    QgsMessageBarItem *messageWidget = visibleMessageBar()->createMessage( title, shortMessage );
    QPushButton *detailsButton = new QPushButton( tr( "Details" ) );
    connect( detailsButton, &QPushButton::clicked, this, [ = ]
    {
      if ( QgsMessageViewer *dialog = dynamic_cast< QgsMessageViewer * >( QgsMessageOutput::createMessageOutput() ) )
      {
        dialog->setTitle( title );
        dialog->setMessage( longMessage, QgsMessageOutput::MessageHtml );
        dialog->showMessage();
      }
    } );
    messageWidget->layout()->addWidget( detailsButton );

    return visibleMessageBar()->pushWidget( messageWidget, level, 0 );
  };

  // insert items in reverse order as each one is inserted on top of previous one
  int count = 0;
  for ( int i = lst.size() - 1 ; i >= 0 ; i--, count++ )
  {
    const QgsMimeDataUtils::Uri &u = lst.at( i );

    QString uri = crsAndFormatAdjustedLayerUri( u.uri, u.supportedCrs, u.supportedFormats );

    if ( u.layerType == QLatin1String( "collection" ) )
    {
//      openLayer( uri, true );
    }
    else if ( u.layerType == QLatin1String( "vector" ) )
    {
      addVectorLayer( uri, u.name, u.providerKey );
    }
    else if ( u.layerType == QLatin1String( "raster" ) )
    {
      addRasterLayer( uri, u.name, u.providerKey );
    }
    else if ( u.layerType == QLatin1String( "mesh" ) )
    {
//      addMeshLayer( uri, u.name, u.providerKey );
    }
    else if ( u.layerType == QLatin1String( "pointcloud" ) )
    {
//      addPointCloudLayer( uri, u.name, u.providerKey );
    }
    else if ( u.layerType == QLatin1String( "vector-tile" ) )
    {
      QgsTemporaryCursorOverride busyCursor( Qt::WaitCursor );

      QgsVectorTileLayer *layer = new QgsVectorTileLayer( uri, u.name );
      bool ok = false;
      layer->loadDefaultMetadata( ok );

      QString error;
      QStringList warnings;
      bool res = layer->loadDefaultStyle( error, warnings );
      if ( res && !warnings.empty() )
      {
        QString message = QStringLiteral( "<p>%1</p>" ).arg( tr( "The following warnings were generated while converting the vector tile style:" ) );
        message += QLatin1String( "<ul>" );

        std::sort( warnings.begin(), warnings.end() );
        warnings.erase( std::unique( warnings.begin(), warnings.end() ), warnings.end() );

        for ( const QString &w : std::as_const( warnings ) )
        {
          message += QStringLiteral( "<li>%1</li>" ).arg( w.toHtmlEscaped().replace( '\n', QLatin1String( "<br>" ) ) );
        }
        message += QLatin1String( "</ul>" );
        showLayerLoadWarnings( tr( "Vector tiles" ), tr( "Style could not be completely converted" ),
                               message, Qgis::MessageLevel::Warning );
      }
      addMapLayer( layer );
    }
    else if ( u.layerType == QLatin1String( "plugin" ) )
    {
//      addPluginLayer( uri, u.name, u.providerKey );
    }
    else if ( u.layerType == QLatin1String( "custom" ) )
    {
      const auto constMCustomDropHandlers = mCustomDropHandlers;
      for ( QgsCustomDropHandler *handler : constMCustomDropHandlers )
      {
        if ( handler && handler->customUriProviderKey() == u.providerKey )
        {
          handler->handleCustomUriDrop( u );
          break;
        }
      }
    }
    else if ( u.layerType == QLatin1String( "project" ) )
    {
//      openFile( u.uri, QStringLiteral( "project" ) );
    }

    task.setProgress( 100.0 * static_cast< double >( count ) / lst.size() );
  }

  mBlockActiveLayerChanged = false;
  onActiveLayerChanged( activeLayer() );
}


void QGISVisualizationWidget::onActiveLayerChanged( QgsMapLayer *layer )
{
  if ( mBlockActiveLayerChanged )
    return;

  const QList< QgsMapCanvas * > canvases = mapCanvases();
  for ( QgsMapCanvas *canvas : canvases )
    canvas->setCurrentLayer( layer );

//  if ( mUndoWidget )
//  {
//    if ( layer )
//    {
//      mUndoWidget->setUndoStack( layer->undoStack() );
//    }
//    else
//    {
//      mUndoWidget->unsetStack();
//    }
//    updateUndoActions();
//  }

  emit activeLayerChanged( layer );
}



void QGISVisualizationWidget::addMapLayer( QgsMapLayer *mapLayer )
{
  QgsCanvasRefreshBlocker refreshBlocker;

  if ( mapLayer->isValid() )
  {
    // Register this layer with the layers registry
    QList<QgsMapLayer *> myList;
    myList << mapLayer;
    QgsProject::instance()->addMapLayers( myList );

    askUserForDatumTransform( mapLayer->crs(), QgsProject::instance()->crs(), mapLayer );
  }
  else
  {
    QString msg = tr( "The layer is not a valid layer and can not be added to the map" );
    visibleMessageBar()->pushMessage( tr( "Layer is not valid" ), msg, Qgis::MessageLevel::Critical );
  }
}


QgsMapCanvas *QGISVisualizationWidget::createNewMapCanvas( const QString &name )
{
    QgsMapCanvasDockWidget *dock = createNewMapCanvasDock( name );
    if ( !dock )
        return nullptr;

    setupDockWidget( dock );  // use default dock position settings

    dock->mapCanvas()->setLayers( mMapCanvas->layers() );
    dock->mapCanvas()->setExtent( mMapCanvas->extent() );
    QgsDebugMsgLevel( QStringLiteral( "QgisApp::createNewMapCanvas -2- : QgsProject::instance()->crs().description[%1]ellipsoid[%2]" ).arg( QgsProject::instance()->crs().description(), QgsProject::instance()->crs().ellipsoidAcronym() ), 3 );
    dock->mapCanvas()->setDestinationCrs( QgsProject::instance()->crs() );
    dock->mapCanvas()->freeze( false );
    return dock->mapCanvas();
}


QString QGISVisualizationWidget::crsAndFormatAdjustedLayerUri( const QString &uri, const QStringList &supportedCrs, const QStringList &supportedFormats ) const
{
  QString newuri = uri;

  // Adjust layer CRS to project CRS
  QgsCoordinateReferenceSystem testCrs;
  const auto constSupportedCrs = supportedCrs;
  for ( const QString &c : constSupportedCrs )
  {
    testCrs.createFromOgcWmsCrs( c );
    if ( testCrs == mMapCanvas->mapSettings().destinationCrs() )
    {
      newuri.replace( QRegExp( "crs=[^&]+" ), "crs=" + c );
      QgsDebugMsgLevel( QStringLiteral( "Changing layer crs to %1, new uri: %2" ).arg( c, uri ), 2 );
      break;
    }
  }

  // Use the last used image format
  QString lastImageEncoding = QgsSettings().value( QStringLiteral( "/qgis/lastWmsImageEncoding" ), "image/png" ).toString();
  const auto constSupportedFormats = supportedFormats;
  for ( const QString &fmt : constSupportedFormats )
  {
    if ( fmt == lastImageEncoding )
    {
      newuri.replace( QRegExp( "format=[^&]+" ), "format=" + fmt );
      QgsDebugMsgLevel( QStringLiteral( "Changing layer format to %1, new uri: %2" ).arg( fmt, uri ), 2 );
      break;
    }
  }
  return newuri;
}

// Open the project file corresponding to the
// path at the given index in mRecentProjectPaths
void QGISVisualizationWidget::openProject( const QString &fileName  )
{

}


//QgsOptions *QGISVisualizationWidget::createOptionsDialog( QWidget *parent )
//{
//  QList< QgsOptionsWidgetFactory * > factories;
//  const auto constMOptionsWidgetFactories = mOptionsWidgetFactories;
//  for ( const QPointer< QgsOptionsWidgetFactory > &f : constMOptionsWidgetFactories )
//  {
//    // remove any deleted factories
//    if ( f )
//      factories << f;
//  }
//  return new QgsOptions( parent, QgsGuiUtils::ModalDialogFlags, factories );
//}


//void QGISVisualizationWidget::showOptionsDialog( QWidget *parent, const QString &currentPage, int pageNumber )
//{
//  std::unique_ptr< QgsOptions > optionsDialog( createOptionsDialog( parent ) );

//  QgsSettings mySettings;
//  QString oldScales = mySettings.value( QStringLiteral( "Map/scales" ), Qgis::defaultProjectScales() ).toString();

//  if ( !currentPage.isEmpty() )
//  {
//    optionsDialog->setCurrentPage( currentPage );
//  }

//  if ( pageNumber >= 0 )
//  {
//    optionsDialog->setCurrentPage( pageNumber );
//  }

//  if ( optionsDialog->exec() )
//  {
//    QgsProject::instance()->layerTreeRegistryBridge()->setNewLayersVisible( mySettings.value( QStringLiteral( "qgis/new_layers_visible" ), true ).toBool() );

////    setupLayerTreeViewFromSettings();

//    const auto canvases = mapCanvases();
//    for ( QgsMapCanvas *canvas : canvases )
//    {
//      applyDefaultSettingsToCanvas( canvas );
//    }

//    //update any open compositions so they reflect new composer settings
//    //we have to push the changes to the compositions here, because compositions
//    //have no access to qgisapp and accordingly can't listen in to changes
//    const QList< QgsMasterLayoutInterface * > layouts = QgsProject::instance()->layoutManager()->layouts() ;
//    for ( QgsMasterLayoutInterface *layout : layouts )
//    {
//      layout->updateSettings();
//    }

//    //do we need this? TS
//    for ( QgsMapCanvas *canvas : canvases )
//    {
//      canvas->refresh();
//    }

//    mRasterFileFilter = QgsProviderRegistry::instance()->fileRasterFilters();

//    if ( oldScales != mySettings.value( QStringLiteral( "Map/scales" ), Qgis::defaultProjectScales() ).toString() )
//    {
//      mScaleWidget->updateScales();
//    }

//    mMapTools->mapTool< QgsMeasureTool >( QgsAppMapTools::MeasureDistance )->updateSettings();
//    mMapTools->mapTool< QgsMeasureTool >( QgsAppMapTools::MeasureArea )->updateSettings();
//    mMapTools->mapTool< QgsMapToolMeasureAngle >( QgsAppMapTools::MeasureAngle )->updateSettings();
//    mMapTools->mapTool< QgsMapToolMeasureBearing >( QgsAppMapTools::MeasureBearing )->updateSettings();

//#ifdef HAVE_3D
//    const QList< Qgs3DMapCanvasDockWidget * > canvases3D = findChildren< Qgs3DMapCanvasDockWidget * >();
//    for ( Qgs3DMapCanvasDockWidget *canvas3D : canvases3D )
//    {
//      canvas3D->measurementLineTool()->updateSettings();
//    }
//#endif

//    double factor = mySettings.value( QStringLiteral( "qgis/magnifier_factor_default" ), 1.0 ).toDouble();
//    mMagnifierWidget->setDefaultFactor( factor );
//    mMagnifierWidget->updateMagnification( factor );

//  }
//}


QgsMapCanvasDockWidget *QGISVisualizationWidget::createNewMapCanvasDock( const QString &name )
{
    const auto canvases = mapCanvases();
    for ( QgsMapCanvas *canvas : canvases )
    {
        if ( canvas->objectName() == name )
        {
            QgsDebugMsg( QStringLiteral( "A map canvas with name '%1' already exists!" ).arg( name ) );
            return nullptr;
        }
    }

    QgsMapCanvasDockWidget *mapCanvasWidget = new QgsMapCanvasDockWidget( name, this );
    mapCanvasWidget->setAllowedAreas( Qt::AllDockWidgetAreas );
    mapCanvasWidget->setMainCanvas( mMapCanvas );

    QgsMapCanvas *mapCanvas = mapCanvasWidget->mapCanvas();
    mapCanvas->freeze( true );
    mapCanvas->setObjectName( name );
    mapCanvas->setProject( QgsProject::instance() );
    connect( mapCanvas, &QgsMapCanvas::messageEmitted, this, &QGISVisualizationWidget::displayMessage );
    connect( mLayerTreeCanvasBridge, &QgsLayerTreeMapCanvasBridge::canvasLayersChanged, mapCanvas, &QgsMapCanvas::setLayers );

    applyProjectSettingsToCanvas( mapCanvas );
    applyDefaultSettingsToCanvas( mapCanvas );

    // add existing annotations to canvas
    const auto constAnnotations = QgsProject::instance()->annotationManager()->annotations();
    for ( QgsAnnotation *annotation : constAnnotations )
    {
        QgsMapCanvasAnnotationItem *canvasItem = new QgsMapCanvasAnnotationItem( annotation, mapCanvas );
        Q_UNUSED( canvasItem ) //item is already added automatically to canvas scene
    }

    mapCanvas->setCustomDropHandlers( mCustomDropHandlers );

    markDirty();
    connect( mapCanvasWidget, &QgsMapCanvasDockWidget::closed, this, &QGISVisualizationWidget::markDirty );
    //connect( mapCanvasWidget, &QgsMapCanvasDockWidget::renameTriggered, this, &QGISVisualizationWidget::renameView );

    return mapCanvasWidget;
}


void QGISVisualizationWidget::markDirty()
{
    // notify the project that there was a change
    QgsProject::instance()->setDirty( true );
}


void QGISVisualizationWidget::freezeCanvases( bool frozen )
{
    const auto canvases = mapCanvases();
    for ( QgsMapCanvas *canvas : canvases )
    {
        canvas->freeze( frozen );
    }
}


QgsBrowserGuiModel* QGISVisualizationWidget::browserModel()
{
  return mBrowserModel;
}


void QGISVisualizationWidget::setupDockWidget( QDockWidget *dockWidget, bool isFloating, QRect dockGeometry, Qt::DockWidgetArea area )
{
    dockWidget->setFloating( isFloating );
    if ( dockGeometry.isEmpty() )
    {
        // try to guess a nice initial placement for view - about 3/4 along, half way down
        dockWidget->setGeometry( QRect( static_cast< int >( rect().width() * 0.75 ), static_cast< int >( rect().height() * 0.5 ), 400, 400 ) );
        addDockWidget( area, dockWidget );
    }
    else
    {
        if ( !isFloating )
        {
            // ugly hack, but only way to set dock size correctly for Qt < 5.6
            dockWidget->setFixedSize( dockGeometry.size() );
            addDockWidget( area, dockWidget );
            dockWidget->resize( dockGeometry.size() );
            QgsApplication::processEvents(); // required!
            dockWidget->setFixedSize( QWIDGETSIZE_MAX, QWIDGETSIZE_MAX );
        }
        else
        {
            dockWidget->setGeometry( dockGeometry );
            addDockWidget( area, dockWidget );
        }
    }
}

QGISVisualizationWidget::~QGISVisualizationWidget()
{
    delete mpZoomInTool;
    delete mpZoomOutTool;
    delete mpPanTool;
    delete mpMapToolBar;
    delete mMapCanvas;
    delete mpLayout;
    delete mDataSourceManagerDialog;

}


void QGISVisualizationWidget::addDockWidget( Qt::DockWidgetArea area, QDockWidget *thepDockWidget )
{
    QMainWindow::addDockWidget(area, thepDockWidget );
    // Make the right and left docks consume all vertical space and top
    // and bottom docks nest between them
    setCorner( Qt::TopLeftCorner, Qt::LeftDockWidgetArea );
    setCorner( Qt::BottomLeftCorner, Qt::LeftDockWidgetArea );
    setCorner( Qt::TopRightCorner, Qt::RightDockWidgetArea );
    setCorner( Qt::BottomRightCorner, Qt::RightDockWidgetArea );
    // add to the Panel submenu
    //  mPanelMenu->addAction( thepDockWidget->toggleViewAction() );

    thepDockWidget->show();

    // refresh the map canvas
    refreshMapCanvas();
}


void QGISVisualizationWidget::applyProjectSettingsToCanvas( QgsMapCanvas *canvas )
{
    canvas->setCanvasColor( QgsProject::instance()->backgroundColor() );
    canvas->setSelectionColor( QgsProject::instance()->selectionColor() );
}


void QGISVisualizationWidget::applyDefaultSettingsToCanvas( QgsMapCanvas *canvas )
{
    QgsSettings settings;
    canvas->enableAntiAliasing( settings.value( QStringLiteral( "qgis/enable_anti_aliasing" ), true ).toBool() );
    double zoomFactor = settings.value( QStringLiteral( "qgis/zoom_factor" ), 2 ).toDouble();
    canvas->setWheelFactor( zoomFactor );
    canvas->setCachingEnabled( settings.value( QStringLiteral( "qgis/enable_render_caching" ), true ).toBool() );
    canvas->setParallelRenderingEnabled( settings.value( QStringLiteral( "qgis/parallel_rendering" ), true ).toBool() );
    canvas->setMapUpdateInterval( settings.value( QStringLiteral( "qgis/map_update_interval" ), 250 ).toInt() );
    canvas->setSegmentationTolerance( settings.value( QStringLiteral( "qgis/segmentationTolerance" ), "0.01745" ).toDouble() );
    canvas->setSegmentationToleranceType( QgsAbstractGeometry::SegmentationToleranceType( settings.enumValue( QStringLiteral( "qgis/segmentationToleranceType" ), QgsAbstractGeometry::MaximumAngle ) ) );
}

void QGISVisualizationWidget::namSetup()
{
    QgsNetworkAccessManager *nam = QgsNetworkAccessManager::instance();

    connect( nam, &QNetworkAccessManager::proxyAuthenticationRequired,
             this, &QGISVisualizationWidget::namProxyAuthenticationRequired );

    connect( nam, qOverload< QgsNetworkRequestParameters >( &QgsNetworkAccessManager::requestTimedOut ),
             this, &QGISVisualizationWidget::namRequestTimedOut );

    nam->setAuthHandler( std::make_unique<QgsAppAuthRequestHandler>() );
#ifndef QT_NO_SSL
    nam->setSslErrorHandler( std::make_unique<QgsAppSslErrorHandler>() );
#endif
}


void QGISVisualizationWidget::masterPasswordSetup()
{
    connect( QgsApplication::authManager(), &QgsAuthManager::messageOut,
             this, &QGISVisualizationWidget::authMessageOut );
    connect( QgsApplication::authManager(), &QgsAuthManager::passwordHelperMessageOut,
             this, &QGISVisualizationWidget::authMessageOut );
    connect( QgsApplication::authManager(), &QgsAuthManager::authDatabaseEraseRequested,
             this, &QGISVisualizationWidget::eraseAuthenticationDatabase );
}


void QGISVisualizationWidget::namRequestTimedOut( const QgsNetworkRequestParameters &request )
{
    QLabel *msgLabel = new QLabel( tr( "Network request to %1 timed out, any data received is likely incomplete." ).arg( request.request().url().host() ) +
                                   tr( " Please check the <a href=\"#messageLog\">message log</a> for further info." ), messageBar() );
    msgLabel->setWordWrap( true );
    connect( msgLabel, &QLabel::linkActivated, mLogDock, &QWidget::show );
    messageBar()->pushItem( new QgsMessageBarItem( msgLabel, Qgis::MessageLevel::Warning, QgsMessageBar::defaultMessageTimeout() ) );
}


void QGISVisualizationWidget::namProxyAuthenticationRequired( const QNetworkProxy &proxy, QAuthenticator *auth )
{
    QgsSettings settings;
    if ( !settings.value( QStringLiteral( "proxy/proxyEnabled" ), false ).toBool() ||
         settings.value( QStringLiteral( "proxy/proxyType" ), "" ).toString() == QLatin1String( "DefaultProxy" ) )
    {
        auth->setUser( QString() );
        return;
    }

    QString username = auth->user();
    QString password = auth->password();

    for ( ;; )
    {
        bool ok = QgsCredentials::instance()->get(
                    QStringLiteral( "proxy %1:%2 [%3]" ).arg( proxy.hostName() ).arg( proxy.port() ).arg( auth->realm() ),
                    username, password,
                    tr( "Proxy authentication required" ) );
        if ( !ok )
            return;

        if ( auth->user() != username || ( password != auth->password() && !password.isNull() ) )
        {
            QgsCredentials::instance()->put(
                        QStringLiteral( "proxy %1:%2 [%3]" ).arg( proxy.hostName() ).arg( proxy.port() ).arg( auth->realm() ),
                        username, password
                        );
            break;
        }
        else
        {
            // credentials didn't change - stored ones probably wrong? clear password and retry
            QgsCredentials::instance()->put(
                        QStringLiteral( "proxy %1:%2 [%3]" ).arg( proxy.hostName() ).arg( proxy.port() ).arg( auth->realm() ),
                        username, QString() );
        }
    }

    auth->setUser( username );
    auth->setPassword( password );
}



void QGISVisualizationWidget::startProfile( const QString &name )
{
    QgsApplication::profiler()->start( name );
}


void QGISVisualizationWidget::displayMessage( const QString &title, const QString &message, Qgis::MessageLevel level )
{
    qDebug()<<title  + message;
}


void QGISVisualizationWidget::endProfile()
{
    QgsApplication::profiler()->end();
}

QgsLayerTreeView *QGISVisualizationWidget::layerTreeView() const
{
    return mLayerTreeView;
}


void QGISVisualizationWidget::panMode()
{
    mMapCanvas->setMapTool(mpPanTool);

}


void QGISVisualizationWidget::zoomInMode()
{
    mMapCanvas->setMapTool(mpZoomInTool);
}


void QGISVisualizationWidget::zoomOutMode()
{
    mMapCanvas->setMapTool(mpZoomOutTool);
}

bool QGISVisualizationWidget::addVectorLayers( const QStringList &layerQStringList, const QString &enc, const QString &dataSourceType )
{
    return addVectorLayersPrivate( layerQStringList, enc, dataSourceType );
}


QgsVectorLayer *QGISVisualizationWidget::addVectorLayer( const QString &vectorLayerPath, const QString &name, const QString &providerKey )
{
    return addLayerPrivate< QgsVectorLayer >( QgsMapLayerType::VectorLayer, vectorLayerPath, name, providerKey, true );
}


QgsMapCanvas *QGISVisualizationWidget::mapCanvas()
{
    Q_ASSERT( mMapCanvas );
    return mMapCanvas;
}

QList<QgsMapCanvas *> QGISVisualizationWidget::mapCanvases()
{
    // filter out browser canvases -- they are children of app, but a different
    // kind of beast, and here we only want the main canvas or dock canvases
    auto canvases = findChildren< QgsMapCanvas * >();
    canvases.erase( std::remove_if( canvases.begin(), canvases.end(),
                                    []( QgsMapCanvas * canvas )
                    {
                        return !canvas || canvas->property( "browser_canvas" ).toBool();
                    } ), canvases.end() );
    return canvases;
}


void QGISVisualizationWidget::refreshMapCanvas( bool redrawAllLayers )
{
    const auto canvases = mapCanvases();
    for ( QgsMapCanvas *canvas : canvases )
    {
        //stop any current rendering
        canvas->stopRendering();
        if ( redrawAllLayers )
            canvas->refreshAllLayers();
        else
            canvas->refresh();
    }
}


void QGISVisualizationWidget::authMessageOut( const QString &message, const QString &authtag, QgsAuthManager::MessageLevel level )
{
    // Use system notifications if the main window is not the active one,
    // push message to the message bar if the main window is active

    qDebug()<< tr( "QGIS Authentication" ) + authtag + message;

}


void QGISVisualizationWidget::eraseAuthenticationDatabase()
{
    // First check if now is a good time to interact with the user, e.g. project is done loading.
    // If not, ask QgsAuthManager to re-emit authDatabaseEraseRequested from the schedule timer.
    // No way to know if user interaction will interfere with plugins loading layers.

    if ( !QgsProject::instance()->fileName().isNull() ) // a non-blank project is loaded
    {
        // Apparently, as of QGIS 2.9, the only way to query that the project is in a
        // layer-loading state is via a custom property of the project's layer tree.
        QgsLayerTreeGroup *layertree( QgsProject::instance()->layerTreeRoot() );
        if ( layertree && layertree->customProperty( QStringLiteral( "loading" ) ).toBool() )
        {
            QgsDebugMsgLevel( QStringLiteral( "Project loading, skipping auth db erase" ), 2 );
            QgsApplication::authManager()->setScheduledAuthDatabaseEraseRequestEmitted( false );
            return;
        }
    }

    // TODO: Check if Browser panel is also still loading?
    //       It has auto-connections in parallel (if tree item is expanded), though
    //       such connections with possible master password requests *should* be ignored
    //       when there is an authentication db erase scheduled.

    // This function should tell QgsAuthManager to stop any erase db schedule timer,
    // *after* interacting with the user
    QgsAuthGuiUtils::eraseAuthenticationDatabase( messageBar(), this );
}


bool QGISVisualizationWidget::addVectorLayersPrivate( const QStringList &layers, const QString &enc, const QString &dataSourceType, const bool guiWarning )
{
    //note: this method ONLY supports vector layers from the OGR provider!

    QgsCanvasRefreshBlocker refreshBlocker;

    QList<QgsMapLayer *> layersToAdd;
    QList<QgsMapLayer *> addedLayers;
    QgsSettings settings;
    bool userAskedToAddLayers = false;

    for ( const QString &layerUri : layers )
    {
        const QString uri = layerUri.trimmed();
        QString baseName;
        if ( dataSourceType == QLatin1String( "file" ) )
        {
            QString srcWithoutLayername( uri );
            int posPipe = srcWithoutLayername.indexOf( '|' );
            if ( posPipe >= 0 )
                srcWithoutLayername.resize( posPipe );
            baseName = QgsProviderUtils::suggestLayerNameFromFilePath( srcWithoutLayername );

            // if needed prompt for zipitem layers
            QString vsiPrefix = QgsZipItem::vsiPrefix( uri );
            if ( ! uri.startsWith( QLatin1String( "/vsi" ), Qt::CaseInsensitive ) &&
                 ( vsiPrefix == QLatin1String( "/vsizip/" ) || vsiPrefix == QLatin1String( "/vsitar/" ) ) )
            {
                if ( askUserForZipItemLayers( uri, { QgsMapLayerType::VectorLayer } ) )
                    continue;
            }
        }
        else if (dataSourceType == QLatin1String("database"))
        {
            // Try to extract the database name and use it as base name
            // sublayers names (if any) will be appended to the layer name
            const QVariantMap parts( QgsProviderRegistry::instance()->decodeUri( QStringLiteral( "ogr" ), uri ) );
            if ( parts.value( QStringLiteral( "databaseName" ) ).isValid() )
                baseName = parts.value( QStringLiteral( "databaseName" ) ).toString();
            else
                baseName = uri;
        }
        else //directory //protocol
        {
            baseName = QgsProviderUtils::suggestLayerNameFromFilePath( uri );
        }

        if ( settings.value( QStringLiteral( "qgis/formatLayerName" ), false ).toBool() )
        {
            baseName = QgsMapLayer::formatLayerName( baseName );
        }

        QgsDebugMsgLevel( "completeBaseName: " + baseName, 2 );
        const bool isVsiCurl { uri.startsWith( QLatin1String( "/vsicurl" ), Qt::CaseInsensitive ) };
        const auto scheme { QUrl( uri ).scheme() };
        const bool isRemoteUrl { scheme.startsWith( QLatin1String( "http" ) ) || scheme == QLatin1String( "ftp" ) };

        std::unique_ptr< QgsTemporaryCursorOverride > cursorOverride;
        if ( isVsiCurl || isRemoteUrl )
        {
            cursorOverride = std::make_unique< QgsTemporaryCursorOverride >( Qt::WaitCursor );
            qDebug()<<tr( "Remote layer" ) + tr( "loading %1, please wait …" ).arg( uri );
            qApp->processEvents();
        }

        QList< QgsProviderSublayerDetails > sublayers = QgsProviderRegistry::instance()->providerMetadata( QStringLiteral( "ogr" ) )->querySublayers( uri );
        // filter out non-vector sublayers
        sublayers.erase( std::remove_if( sublayers.begin(), sublayers.end(), []( const QgsProviderSublayerDetails & sublayer )
        {
            return sublayer.type() != QgsMapLayerType::VectorLayer;
        } ), sublayers.end() );

        cursorOverride.reset();

        const QVariantMap uriParts = QgsProviderRegistry::instance()->decodeUri( QStringLiteral( "ogr" ), uri );
        const QString path = uriParts.value( QStringLiteral( "path" ) ).toString();

        if ( !sublayers.empty() )
        {
            userAskedToAddLayers = true;

            const bool detailsAreIncomplete = QgsProviderUtils::sublayerDetailsAreIncomplete( sublayers, QgsProviderUtils::SublayerCompletenessFlag::IgnoreUnknownFeatureCount );
            const bool singleSublayerOnly = sublayers.size() == 1;
            QString groupName;

            if ( !singleSublayerOnly || detailsAreIncomplete )
            {
                // ask user for sublayers (unless user settings dictate otherwise!)
                switch ( shouldAskUserForSublayers( sublayers ) )
                {
                case SublayerHandling::AskUser:
                {
                    // prompt user for sublayers
                    QgsProviderSublayersDialog dlg( uri, path, sublayers, {QgsMapLayerType::VectorLayer}, this );

                    if ( dlg.exec() )
                        sublayers = dlg.selectedLayers();
                    else
                        sublayers.clear(); // dialog was canceled, so don't add any sublayers
                    groupName = dlg.groupName();
                    break;
                }

                case SublayerHandling::LoadAll:
                {
                    if ( detailsAreIncomplete )
                    {
                        // requery sublayers, resolving geometry types
                        sublayers = QgsProviderRegistry::instance()->querySublayers( uri, Qgis::SublayerQueryFlag::ResolveGeometryType );
                        // filter out non-vector sublayers
                        sublayers.erase( std::remove_if( sublayers.begin(), sublayers.end(), []( const QgsProviderSublayerDetails & sublayer )
                        {
                            return sublayer.type() != QgsMapLayerType::VectorLayer;
                        } ), sublayers.end() );
                    }
                    break;
                }

                case SublayerHandling::AbortLoading:
                    sublayers.clear(); // don't add any sublayers
                    break;
                };
            }
            else if ( detailsAreIncomplete )
            {
                // requery sublayers, resolving geometry types
                sublayers = QgsProviderRegistry::instance()->querySublayers( uri, Qgis::SublayerQueryFlag::ResolveGeometryType );
                // filter out non-vector sublayers
                sublayers.erase( std::remove_if( sublayers.begin(), sublayers.end(), []( const QgsProviderSublayerDetails & sublayer )
                {
                    return sublayer.type() != QgsMapLayerType::VectorLayer;
                } ), sublayers.end() );
            }

            // now add sublayers
            if ( !sublayers.empty() )
            {
                addedLayers << addSublayers( sublayers, baseName, groupName );
            }

        }
        else
        {
            QString msg = tr( "%1 is not a valid or recognized data source." ).arg( uri );
            // If the failed layer was a vsicurl type, give the user a chance to try the normal download.
            if ( isVsiCurl &&
                 QMessageBox::question( this, tr( "Invalid Data Source" ),
                                        tr( "Download with \"Protocol\" source type has failed, do you want to try the \"File\" source type?" ) ) == QMessageBox::Yes )
            {
                QString fileUri = uri;
                fileUri.replace( QLatin1String( "/vsicurl/" ), " " );
                return addVectorLayersPrivate( QStringList() << fileUri, enc, dataSourceType, guiWarning );
            }
            else if ( guiWarning )
            {
                qDebug()<<tr( "Invalid Data Source" ) + msg;
            }
        }
    }

    // make sure at least one layer was successfully added
    if ( layersToAdd.isEmpty() )
    {
        // we also return true if we asked the user for sublayers, but they choose none. In this case nothing
        // went wrong, so we shouldn't return false and cause GUI warnings to appear
        return userAskedToAddLayers || !addedLayers.isEmpty();
    }

    // Register this layer with the layers registry
    QgsProject::instance()->addMapLayers( layersToAdd );
    for ( QgsMapLayer *l : std::as_const( layersToAdd ) )
    {
        if ( !enc.isEmpty() )
        {
            if ( QgsVectorLayer *vl = qobject_cast< QgsVectorLayer * >( l ) )
                vl->setProviderEncoding( enc );
        }

        askUserForDatumTransform( l->crs(), QgsProject::instance()->crs(), l );
        postProcessAddedLayer( l );
    }

    //  activateDeactivateLayerRelatedActions( activeLayer() );

    return true;
}


void QGISVisualizationWidget::addLayer()
{



    //    OpenTopoMap

    //    https://tile.opentopomap.org/{z}/{x}/{y}.png
    //    (See comment below for attribution)

    //    OpenStreetMap

    //    http://tile.openstreetmap.org/{z}/{x}/{y}.png
    //    Google Hybrid

    //    https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}
    //    Google Satellite

    //    https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}
    //    Google Road

    //    https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}
    //    (Codes for other tile types from Google found here)

    //    Bing Aerial

    //    http://ecn.t3.tiles.virtualearth.net/tiles/a{q}.jpeg?g=1


    //  QString myLayerPath         = "../data";
    //  QString myLayerBaseName     = "test";
    //  QString myProviderName      = "ogr";

    //  QgsVectorLayer * mypLayer = new QgsVectorLayer(myLayerPath, myLayerBaseName, myProviderName);
    //  QgsSingleSymbolRenderer *mypRenderer = new QgsSingleSymbolRenderer(/*mypLayer->geometryType()*/ nullptr);
    //////  QList<QgsMapCanvasLayer> myLayerSet;
    //  mypLayer->setRenderer(mypRenderer);

    //  if (mypLayer->isValid())
    //  {
    //    qDebug("Layer is valid");
    //  }
    //  else
    //  {
    //    qDebug("Layer is NOT valid");
    //    return;
    //  }
    ////  // Add the Vector Layer to the Layer Registry
    ////  QgsMapLayerRegistry::instance()->addMapLayer(mypLayer, TRUE);

    //  // Add the Layer to the Layer Set
    //  myLayerSet.append(QgsMapCanvasLayer(mypLayer));
    //  // set the canvas to the extent of our layer
    //  mpMapCanvas->setExtent(mypLayer->extent());
    //  // Set the Map Canvas Layer Set
    ////  mpMapCanvas->setLayerSet(myLayerSet);
}


QgsVectorTileLayer *QGISVisualizationWidget::addVectorTileLayer( const QString &url, const QString &baseName )
{
    return addVectorTileLayerPrivate( url, baseName );
}



QgsVectorTileLayer *QGISVisualizationWidget::addVectorTileLayerPrivate( const QString &url, const QString &baseName, const bool guiWarning )
{
    QgsCanvasRefreshBlocker refreshBlocker;

    QgsSettings settings;

    QString base(baseName);

    if (settings.value(QStringLiteral("qgis/formatLayerName"), false).toBool())
    {
        base = QgsMapLayer::formatLayerName( base );
    }

    QgsDebugMsgLevel("completeBaseName: " + base, 2);

    // create the layer
    std::unique_ptr<QgsVectorTileLayer> layer = std::make_unique<QgsVectorTileLayer>(url, base);

    if ( !layer || !layer->isValid() )
    {
        if ( guiWarning )
        {
            QString msg = tr("%1 is not a valid or recognized data source.").arg(url);
            qDebug()<<msg;
        }

        return nullptr;
    }

    this->postProcessAddedLayer(layer.get());

    QgsProject::instance()->addMapLayer(layer.get());
    //activateDeactivateLayerRelatedActions(activeLayer());

    return layer.release();
}


QgsMessageBar *QGISVisualizationWidget::messageBar()
{
    // Q_ASSERT( mInfoBar );
    return mInfoBar;
}


QgsRasterLayer *QGISVisualizationWidget::addRasterLayer( QString const &uri, QString const &baseName, QString const &providerKey )
{
    return addLayerPrivate< QgsRasterLayer >( QgsMapLayerType::RasterLayer, uri, baseName, providerKey, true );
}


QgsAbstractDataSourceWidget* QGISVisualizationWidget::createDataSourceWidget( QWidget *parent, Qt::WindowFlags fl, QgsProviderRegistry::WidgetMode widgetMode) const
{
    auto xyzSourceSelect = new QgsXyzSourceSelect( parent, fl, widgetMode );

    connect(xyzSourceSelect,&QgsXyzSourceSelect::addRasterLayer,this,&QGISVisualizationWidget::addRasterLayer);

    return xyzSourceSelect;
}


template<typename T>
T* QGISVisualizationWidget::addLayerPrivate( QgsMapLayerType type, const QString &uri, const QString &name, const QString &providerKey, bool guiWarnings )
{
    QgsSettings settings;

    QgsCanvasRefreshBlocker refreshBlocker;

    QString baseName = settings.value( QStringLiteral( "qgis/formatLayerName" ), false ).toBool() ? QgsMapLayer::formatLayerName( name ) : name;

    // if the layer needs authentication, ensure the master password is set
    const QRegularExpression rx( "authcfg=([a-z]|[A-Z]|[0-9]){7}" );
    if ( rx.match( uri ).hasMatch() )
    {
        if ( !QgsAuthGuiUtils::isDisabled(messageBar()))
        {
            QgsApplication::authManager()->setMasterPassword( true );
        }
    }

    QVariantMap uriElements = QgsProviderRegistry::instance()->decodeUri( providerKey, uri );
    QString path = uri;
    if ( uriElements.contains( QStringLiteral( "path" ) ) )
    {
        // run layer path through QgsPathResolver so that all inbuilt paths and other localised paths are correctly expanded
        path = QgsPathResolver().readPath( uriElements.value( QStringLiteral( "path" ) ).toString() );
        uriElements[ QStringLiteral( "path" ) ] = path;
    }
    // Not all providers implement decodeUri(), so use original uri if uriElements is empty
    const QString updatedUri = uriElements.isEmpty() ? uri : QgsProviderRegistry::instance()->encodeUri( providerKey, uriElements );

    const bool canQuerySublayers = QgsProviderRegistry::instance()->providerMetadata( providerKey ) &&
            ( QgsProviderRegistry::instance()->providerMetadata( providerKey )->capabilities() & QgsProviderMetadata::QuerySublayers );

    T *result = nullptr;
    if ( canQuerySublayers )
    {
        // query sublayers
        QList< QgsProviderSublayerDetails > sublayers = QgsProviderRegistry::instance()->providerMetadata( providerKey ) ?
                    QgsProviderRegistry::instance()->providerMetadata( providerKey )->querySublayers( updatedUri )
                  : QgsProviderRegistry::instance()->querySublayers( updatedUri );

        // filter out non-matching sublayers
        sublayers.erase( std::remove_if( sublayers.begin(), sublayers.end(), [type]( const QgsProviderSublayerDetails & sublayer )
        {
            return sublayer.type() != type;
        } ), sublayers.end() );

        if ( sublayers.empty() )
        {
            if ( guiWarnings )
            {
                QString msg = tr( "%1 is not a valid or recognized data source." ).arg( uri );
                qDebug()<<tr( "Invalid Data Source" ) + msg;
            }

            // since the layer is bad, stomp on it
            return nullptr;
        }
        else if ( sublayers.size() > 1 || QgsProviderUtils::sublayerDetailsAreIncomplete( sublayers, QgsProviderUtils::SublayerCompletenessFlag::IgnoreUnknownFeatureCount ) )
        {
            // ask user for sublayers (unless user settings dictate otherwise!)
            switch (shouldAskUserForSublayers(sublayers))
            {
            case SublayerHandling::AskUser:
            {
                QgsProviderSublayersDialog dlg( updatedUri, path, sublayers, {type}, this );
                if ( dlg.exec() )
                {
                    const QList< QgsProviderSublayerDetails > selectedLayers = dlg.selectedLayers();
                    if ( !selectedLayers.isEmpty() )
                    {
                        result = qobject_cast< T * >( addSublayers( selectedLayers, baseName, dlg.groupName() ).value( 0 ) );
                    }
                }
                break;
            }
            case SublayerHandling::LoadAll:
            {
                result = qobject_cast< T * >(addSublayers(sublayers, baseName, QString()).value( 0 ));
                break;
            }
            case SublayerHandling::AbortLoading:
                break;
            };
        }
        else
        {
            result = qobject_cast< T * >(addSublayers( sublayers, name, QString() ).value( 0 ));

            if (result)
            {
                QString base(baseName);
                if (settings.value( QStringLiteral( "qgis/formatLayerName" ), false ).toBool())
                {
                    base = QgsMapLayer::formatLayerName(base);
                }
                result->setName(base);
            }
        }
    }
    else
    {
        QgsMapLayerFactory::LayerOptions options( QgsProject::instance()->transformContext() );
        options.loadDefaultStyle = false;
        result = qobject_cast< T * >( QgsMapLayerFactory::createLayer( uri, name, type, options, providerKey ) );
        if (result)
        {
            QString base( baseName );
            if ( settings.value( QStringLiteral( "qgis/formatLayerName" ), false ).toBool() )
            {
                base = QgsMapLayer::formatLayerName(base);
            }
            result->setName(base);
            QgsProject::instance()->addMapLayer(result);

            askUserForDatumTransform(result->crs(), QgsProject::instance()->crs(), result);
            postProcessAddedLayer(result);
        }
    }

    mMapCanvas->setExtent(result->extent());
    QList<QgsMapLayer *> rasterLst{result};
    mMapCanvas->setLayers(rasterLst);

    refreshMapCanvas(true);

    //  activateDeactivateLayerRelatedActions(activeLayer());
    return result;
}


QList< QgsMapLayer * > QGISVisualizationWidget::addSublayers(const QList<QgsProviderSublayerDetails> &layers, const QString &baseName, const QString &groupName)
{
    QgsLayerTreeGroup *group = nullptr;
    if ( !groupName.isEmpty() )
    {
        group = QgsProject::instance()->layerTreeRoot()->insertGroup( 0, groupName );
    }

    QgsSettings settings;
    const bool formatLayerNames = settings.value( QStringLiteral( "qgis/formatLayerName" ), false ).toBool();

    // if we aren't adding to a group, we need to add the layers in reverse order so that they maintain the correct
    // order in the layer tree!
    QList<QgsProviderSublayerDetails> sortedLayers = layers;
    if ( groupName.isEmpty() )
    {
        std::reverse( sortedLayers.begin(), sortedLayers.end() );
    }

    QList< QgsMapLayer * > result;
    result.reserve(sortedLayers.size());

    for(const QgsProviderSublayerDetails &sublayer : std::as_const(sortedLayers))
    {
        QgsProviderSublayerDetails::LayerOptions options(QgsProject::instance()->transformContext());
        options.loadDefaultStyle = false;

        std::unique_ptr<QgsMapLayer> layer( sublayer.toLayer( options ) );
        if ( !layer )
            continue;

        QgsMapLayer *ml = layer.get();
        // if we aren't adding to a group, then we're iterating the layers in the reverse order
        // so account for that in the returned list of layers
        if ( groupName.isEmpty() )
            result.insert( 0, ml );
        else
            result << ml;

        QString layerName = layer->name();
        if ( formatLayerNames )
        {
            layerName = QgsMapLayer::formatLayerName( layerName );
        }

        // if user has opted to add sublayers to a group, then we don't need to include the
        // filename in the layer's name, because the group is already titled with the filename.
        // But otherwise, we DO include the file name so that users can differentiate the source
        // when multiple layers are loaded from a GPX file or similar (refs https://github.com/qgis/QGIS/issues/37551)
        if ( group )
        {
            if ( !layerName.isEmpty() )
                layer->setName( layerName );
            else if ( !baseName.isEmpty() )
                layer->setName( baseName );
            QgsProject::instance()->addMapLayer( layer.release(), false );
            group->addLayer( ml );
        }
        else
        {
            if ( layerName != baseName && !layerName.isEmpty() && !baseName.isEmpty() )
                layer->setName( QStringLiteral( "%1 — %2" ).arg( baseName, layerName ) );
            else if ( !layerName.isEmpty() )
                layer->setName( layerName );
            else if ( !baseName.isEmpty() )
                layer->setName( baseName );
            QgsProject::instance()->addMapLayer( layer.release() );
        }

        askUserForDatumTransform( ml->crs(), QgsProject::instance()->crs(), ml );
        postProcessAddedLayer( ml );
    }

    if ( group )
    {
        // Respect if user don't want the new group of layers visible.
        QgsSettings settings;
        const bool newLayersVisible = settings.value( QStringLiteral( "/qgis/new_layers_visible" ), true ).toBool();
        if ( !newLayersVisible )
            group->setItemVisibilityCheckedRecursive( newLayersVisible );
    }

    return result;
}


void QGISVisualizationWidget::dataSourceManager( const QString &pageName )
{
    if (! mDataSourceManagerDialog )
    {
        mDataSourceManagerDialog = new QgsDataSourceManagerDialog( mBrowserModel, this, mMapCanvas);
        //    connect( this, &QGISVisualizationWidget::connectionsChanged, mDataSourceManagerDialog, &QgsDataSourceManagerDialog::refresh );
        //    connect( mDataSourceManagerDialog, &QgsDataSourceManagerDialog::connectionsChanged, this, &QGISVisualizationWidget::connectionsChanged );
        connect( mDataSourceManagerDialog, SIGNAL( addRasterLayer( QString const &, QString const &, QString const & ) ),
                 this, SLOT(addRasterLayer( QString const &, QString const &, QString const & ) ) );
        connect( mDataSourceManagerDialog, &QgsDataSourceManagerDialog::addRasterLayers, this, [ = ]( const QStringList & layersList ) { addRasterLayers( layersList ); } );
        connect( mDataSourceManagerDialog, SIGNAL( addVectorLayer( QString const &, QString const &, QString const & ) ),
                 this, SLOT(addVectorLayer( QString const &, QString const &, QString const & ) ) );
        connect( mDataSourceManagerDialog, SIGNAL( addVectorLayers( QStringList const &, QString const &, QString const & ) ),
                 this, SLOT(addVectorLayers( QStringList const &, QString const &, QString const & ) ) );
        connect( mDataSourceManagerDialog, &QgsDataSourceManagerDialog::addVectorTileLayer, this, &QGISVisualizationWidget::addVectorTileLayer );

//        connect( mDataSourceManagerDialog, &QgsDataSourceManagerDialog::addMeshLayer, this, &QGISVisualizationWidget::addMeshLayer );
        //    connect( mDataSourceManagerDialog, &QgsDataSourceManagerDialog::addPointCloudLayer, this, &QGISVisualizationWidget::addPointCloudLayer );
        //    connect( mDataSourceManagerDialog, &QgsDataSourceManagerDialog::showStatusMessage, this, &QGISVisualizationWidget::showStatusMessage );
        //    connect( mDataSourceManagerDialog, &QgsDataSourceManagerDialog::addDatabaseLayers, this, &QGISVisualizationWidget::addDatabaseLayers );
        //    connect( mDataSourceManagerDialog, &QgsDataSourceManagerDialog::replaceSelectedVectorLayer, this, &QGISVisualizationWidget::replaceSelectedVectorLayer );
        //    connect( mDataSourceManagerDialog, &QgsDataSourceManagerDialog::handleDropUriList, this, &QGISVisualizationWidget::handleDropUriList );
        //    connect( this, &QgisApp::newProject, mDataSourceManagerDialog, &QgsDataSourceManagerDialog::updateProjectHome );
        //    connect( mDataSourceManagerDialog, &QgsDataSourceManagerDialog::openFile, this, &QGISVisualizationWidget::openFile );

    }
    else
    {
        mDataSourceManagerDialog->reset();
    }
    // Try to open the dialog on a particular page
    if (!pageName.isEmpty())
    {
        mDataSourceManagerDialog->openPage(pageName);
    }
    if (QgsSettings().value( QStringLiteral( "/qgis/dataSourceManagerNonModal" ), true ).toBool())
    {
        mDataSourceManagerDialog->show();
    }
    else
    {
        mDataSourceManagerDialog->exec();
    }
}


bool QGISVisualizationWidget::askUserForDatumTransform( const QgsCoordinateReferenceSystem &sourceCrs, const QgsCoordinateReferenceSystem &destinationCrs, const QgsMapLayer *layer )
{
    Q_ASSERT( qApp->thread() == QThread::currentThread() );

    QString title;
    if ( layer )
    {
        // try to make a user-friendly (short!) identifier for the layer
        QString layerIdentifier;
        if ( !layer->name().isEmpty() )
        {
            layerIdentifier = layer->name();
        }
        else
        {
            const QVariantMap parts = QgsProviderRegistry::instance()->decodeUri( layer->providerType(), layer->source() );
            if ( parts.contains( QStringLiteral( "path" ) ) )
            {
                const QFileInfo fi( parts.value( QStringLiteral( "path" ) ).toString() );
                layerIdentifier = fi.fileName();
            }
            else if ( layer->dataProvider() )
            {
                const QgsDataSourceUri uri( layer->source() );
                layerIdentifier = uri.table();
            }
        }
        if ( !layerIdentifier.isEmpty() )
            title = tr( "Select Transformation for %1" ).arg( layerIdentifier );
    }

    return QgsDatumTransformDialog::run( sourceCrs, destinationCrs, this, mMapCanvas, title );
}


bool QGISVisualizationWidget::askUserForZipItemLayers(const QString &path, const QList< QgsMapLayerType > &acceptableTypes)
{
    // query sublayers
    QList< QgsProviderSublayerDetails > sublayers = QgsProviderRegistry::instance()->querySublayers( path );

    // filter out non-matching sublayers
    sublayers.erase( std::remove_if( sublayers.begin(), sublayers.end(), [acceptableTypes]( const QgsProviderSublayerDetails & sublayer )
    {
        return !acceptableTypes.empty() && !acceptableTypes.contains( sublayer.type() );
    } ), sublayers.end() );

    if ( sublayers.empty() )
        return false;

    const bool detailsAreIncomplete = QgsProviderUtils::sublayerDetailsAreIncomplete( sublayers, QgsProviderUtils::SublayerCompletenessFlag::IgnoreUnknownFeatureCount );
    const bool singleSublayerOnly = sublayers.size() == 1;
    QString groupName;

    if ( !singleSublayerOnly || detailsAreIncomplete )
    {
        // ask user for sublayers (unless user settings dictate otherwise!)
        switch ( shouldAskUserForSublayers( sublayers ) )
        {
        case SublayerHandling::AskUser:
        {
            // prompt user for sublayers
            QgsProviderSublayersDialog dlg( path, path, sublayers, acceptableTypes, this );

            if ( dlg.exec() )
                sublayers = dlg.selectedLayers();
            else
                sublayers.clear(); // dialog was canceled, so don't add any sublayers
            groupName = dlg.groupName();
            break;
        }

        case SublayerHandling::LoadAll:
        {
            if ( detailsAreIncomplete )
            {
                // requery sublayers, resolving geometry types
                sublayers = QgsProviderRegistry::instance()->querySublayers( path, Qgis::SublayerQueryFlag::ResolveGeometryType );
                sublayers.erase( std::remove_if( sublayers.begin(), sublayers.end(), [acceptableTypes]( const QgsProviderSublayerDetails & sublayer )
                {
                    return !acceptableTypes.empty() && !acceptableTypes.contains( sublayer.type() );
                } ), sublayers.end() );
            }
            break;
        }

        case SublayerHandling::AbortLoading:
            sublayers.clear(); // don't add any sublayers
            break;
        };
    }
    else if ( detailsAreIncomplete )
    {
        // requery sublayers, resolving geometry types
        sublayers = QgsProviderRegistry::instance()->querySublayers( path, Qgis::SublayerQueryFlag::ResolveGeometryType );
        sublayers.erase( std::remove_if( sublayers.begin(), sublayers.end(), [acceptableTypes]( const QgsProviderSublayerDetails & sublayer )
        {
            return !acceptableTypes.empty() && !acceptableTypes.contains( sublayer.type() );
        } ), sublayers.end() );
    }

    // now add sublayers
    if ( !sublayers.empty() )
    {
        QgsCanvasRefreshBlocker refreshBlocker;
        QgsSettings settings;

        QString base = QgsProviderUtils::suggestLayerNameFromFilePath( path );
        if ( settings.value( QStringLiteral( "qgis/formatLayerName" ), false ).toBool() )
        {
            base = QgsMapLayer::formatLayerName( base );
        }

        addSublayers( sublayers, base, groupName );
        //    activateDeactivateLayerRelatedActions( activeLayer() );
    }

    return true;
}


QgsMapLayer *QGISVisualizationWidget::activeLayer()
{
    return mLayerTreeView ? mLayerTreeView->currentLayer() : nullptr;
}


bool QGISVisualizationWidget::addRasterLayers(QStringList const &files, bool guiWarning)
{
    if ( files.empty() )
    {
        return false;
    }

    QgsCanvasRefreshBlocker refreshBlocker;

    // this is messy since some files in the list may be rasters and others may
    // be ogr layers. We'll set returnValue to false if one or more layers fail
    // to load.
    bool returnValue = true;
    for ( const QString &src : files )
    {
        QString errMsg;
        bool ok = false;

        // if needed prompt for zipitem layers
        QString vsiPrefix = QgsZipItem::vsiPrefix( src );
        if ( ( !src.startsWith( QLatin1String( "/vsi" ), Qt::CaseInsensitive ) || src.endsWith( QLatin1String( ".zip" ) ) || src.endsWith( QLatin1String( ".tar" ) ) ) &&
             ( vsiPrefix == QLatin1String( "/vsizip/" ) || vsiPrefix == QLatin1String( "/vsitar/" ) ) )
        {
            if (askUserForZipItemLayers( src, { QgsMapLayerType::RasterLayer } ))
                continue;
        }

        if ( QgsRasterLayer::isValidRasterFileName( src, errMsg ) )
        {
            QFileInfo myFileInfo( src );

            // set the layer name to the file base name unless provided explicitly
            QString layerName;
            const QVariantMap uriDetails = QgsProviderRegistry::instance()->decodeUri( QStringLiteral( "gdal" ), src );
            if ( !uriDetails[ QStringLiteral( "layerName" ) ].toString().isEmpty() )
            {
                layerName = uriDetails[ QStringLiteral( "layerName" ) ].toString();
            }
            else
            {
                layerName = QgsProviderUtils::suggestLayerNameFromFilePath( src );
            }

            // try to create the layer
            QgsRasterLayer *layer = addLayerPrivate< QgsRasterLayer >( QgsMapLayerType::RasterLayer, src, layerName, QStringLiteral( "gdal" ), guiWarning );

            if ( layer && layer->isValid() )
            {
                //only allow one copy of a ai grid file to be loaded at a
                //time to prevent the user selecting all adfs in 1 dir which
                //actually represent 1 coverage,

                if ( myFileInfo.fileName().endsWith( QLatin1String( ".adf" ), Qt::CaseInsensitive ) )
                {
                    break;
                }
            }
            // if layer is invalid addLayerPrivate() will show the error

        } // valid raster filename
        else
        {
            ok = false;

            // Issue message box warning unless we are loading from cmd line since
            // non-rasters are passed to this function first and then successfully
            // loaded afterwards (see main.cpp)
            if ( guiWarning )
            {
                QString msg = tr( "%1 is not a supported raster data source" ).arg( src );
                if ( !errMsg.isEmpty() )
                    msg += '\n' + errMsg;

                qDebug()<<tr( "Unsupported Data Source" ) + msg;
            }
        }
        if ( ! ok )
        {
            returnValue = false;
        }
    }
    return returnValue;
}


QGISVisualizationWidget::SublayerHandling QGISVisualizationWidget::shouldAskUserForSublayers( const QList<QgsProviderSublayerDetails> &layers, bool hasNonLayerItems ) const
{
    if ( hasNonLayerItems )
        return SublayerHandling::AskUser;

    QgsSettings settings;
    const Qgis::SublayerPromptMode promptLayers = settings.enumValue( QStringLiteral( "qgis/promptForSublayers" ), Qgis::SublayerPromptMode::AlwaysAsk );

    switch ( promptLayers )
    {
    case Qgis::SublayerPromptMode::AlwaysAsk:
        return SublayerHandling::AskUser;

    case Qgis::SublayerPromptMode::AskExcludingRasterBands:
    {
        // if any non-raster layers are found, we ask the user. Otherwise we load all
        for ( const QgsProviderSublayerDetails &sublayer : layers )
        {
            if ( sublayer.type() != QgsMapLayerType::RasterLayer )
                return SublayerHandling::AskUser;
        }
        return SublayerHandling::LoadAll;
    }

    case Qgis::SublayerPromptMode::NeverAskSkip:
        return SublayerHandling::AbortLoading;

    case Qgis::SublayerPromptMode::NeverAskLoadAll:
        return SublayerHandling::LoadAll;
    }

    return SublayerHandling::AskUser;
}


void QGISVisualizationWidget::postProcessAddedLayer(QgsMapLayer *layer)
{

    switch (layer->type())
    {
    case QgsMapLayerType::VectorLayer:
    case QgsMapLayerType::RasterLayer:
    {
        bool ok = false;
        layer->loadDefaultStyle( ok );
        layer->loadDefaultMetadata( ok );
        break;
    }

    case QgsMapLayerType::PluginLayer:
        break;

    case QgsMapLayerType::MeshLayer:
    {
        QgsMeshLayer *meshLayer = qobject_cast< QgsMeshLayer *>( layer );
        QDateTime referenceTime = QgsProject::instance()->timeSettings()->temporalRange().begin();
        if ( !referenceTime.isValid() ) // If project reference time is invalid, use current date
            referenceTime = QDateTime( QDate::currentDate(), QTime( 0, 0, 0 ), Qt::UTC );

        if ( meshLayer->dataProvider() && !qobject_cast< QgsMeshLayerTemporalProperties * >( meshLayer->temporalProperties() )->referenceTime().isValid() )
            qobject_cast< QgsMeshLayerTemporalProperties * >( meshLayer->temporalProperties() )->setReferenceTime( referenceTime, meshLayer->dataProvider()->temporalCapabilities() );

        bool ok = false;
        meshLayer->loadDefaultStyle( ok );
        meshLayer->loadDefaultMetadata( ok );
        break;
    }

    case QgsMapLayerType::VectorTileLayer:
    {
        bool ok = false;
        QString error = layer->loadDefaultStyle( ok );
        if ( !ok )
            qDebug()<< "Error loading style";
        error = layer->loadDefaultMetadata( ok );
        if ( !ok )
            qDebug()<< tr( "Error loading layer metadata" );
        break;
    }

    case QgsMapLayerType::AnnotationLayer:
        break;

    case QgsMapLayerType::PointCloudLayer:
    {
        bool ok = false;
        layer->loadDefaultStyle(ok);
        layer->loadDefaultMetadata(ok);

#ifdef HAVE_3D
        if (!layer->renderer3D())
        {
            QgsPointCloudLayer *pcLayer = qobject_cast< QgsPointCloudLayer * >( layer );
            // for point clouds we default to a 3d renderer. it just makes sense :)
            std::unique_ptr< QgsPointCloudLayer3DRenderer > renderer3D = Qgs3DAppUtils::convert2dPointCloudRendererTo3d( pcLayer->renderer() );
            if ( renderer3D )
                layer->setRenderer3D( renderer3D.release() );
            else
            {
                // maybe waiting on an index...
                if ( pcLayer->dataProvider()->indexingState() != QgsPointCloudDataProvider::Indexed )
                {
                    QPointer< QgsPointCloudLayer > layerPointer( pcLayer );
                    connect( pcLayer->dataProvider(), &QgsPointCloudDataProvider::indexGenerationStateChanged, this, [layerPointer]( QgsPointCloudDataProvider::PointCloudIndexGenerationState state )
                    {
                        if ( !layerPointer || state != QgsPointCloudDataProvider::Indexed )
                            return;

                        std::unique_ptr< QgsPointCloudLayer3DRenderer > renderer3D = Qgs3DAppUtils::convert2dPointCloudRendererTo3d( layerPointer->renderer() );
                        if ( renderer3D )
                            layerPointer->setRenderer3D( renderer3D.release() );
                    } );
                }
            }
        }
#endif
        break;
    }
    }
}


/*
void QgisApp::activateDeactivateLayerRelatedActions( QgsMapLayer *layer )
{
  updateLabelToolButtons();

  mMenuPasteAs->setEnabled(clipboard() && !clipboard()->isEmpty());
  mActionPasteAsNewVector->setEnabled( clipboard() && !clipboard()->isEmpty() );
  mActionPasteAsNewMemoryVector->setEnabled( clipboard() && !clipboard()->isEmpty() );

  updateLayerModifiedActions();

  QgsAbstractMapToolHandler::Context context;
  for (QgsAbstractMapToolHandler *handler : std::as_const(mMapToolHandlers))
  {
    handler->action()->setEnabled(handler->isCompatibleWithLayer(layer, context));
    if (handler->mapTool() == mMapCanvas->mapTool())
    {
      if (!handler->action()->isEnabled())
      {
        mMapCanvas->unsetMapTool(handler->mapTool());
        mActionPan->trigger();
      }
      else
      {
        handler->setLayerForTool( layer );
      }
    }
  }

  bool identifyModeIsActiveLayer = QgsSettings().enumValue(QStringLiteral("/Map/identifyMode"), QgsMapToolIdentify::ActiveLayer) == QgsMapToolIdentify::ActiveLayer;

  if (!layer)
  {
    mMenuSelect->setEnabled( false );
    mActionSelectFeatures->setEnabled( false );
    mActionSelectPolygon->setEnabled( false );
    mActionSelectFreehand->setEnabled( false );
    mActionSelectRadius->setEnabled( false );
    mActionIdentify->setEnabled( true );
    mActionSelectByExpression->setEnabled( false );
    mActionSelectByForm->setEnabled( false );
    mActionLabeling->setEnabled( false );
    mActionOpenTable->setEnabled( false );
    mMenuFilterTable->setEnabled( false );
    mActionOpenTableSelected->setEnabled( false );
    mActionOpenTableVisible->setEnabled( false );
    mActionOpenTableEdited->setEnabled( false );
    mActionSelectAll->setEnabled( false );
    mActionReselect->setEnabled( false );
    mActionInvertSelection->setEnabled( false );
    mActionOpenFieldCalc->setEnabled( false );
    mActionToggleEditing->setEnabled( false );
    mActionToggleEditing->setChecked( false );
    mActionSaveLayerEdits->setEnabled( false );
    mActionSaveLayerDefinition->setEnabled( false );
    mActionLayerSaveAs->setEnabled( false );
    mActionLayerProperties->setEnabled( false );
    mActionLayerSubsetString->setEnabled( false );
    mActionAddToOverview->setEnabled( false );
    mActionFeatureAction->setEnabled( false );
    mActionAddFeature->setEnabled( false );
    mActionCircularStringCurvePoint->setEnabled( false );
    mActionCircularStringRadius->setEnabled( false );
    mMenuCircle->setEnabled( false );
    mActionCircle2Points->setEnabled( false );
    mActionCircle3Points->setEnabled( false );
    mActionCircle3Tangents->setEnabled( false );
    mActionCircle2TangentsPoint->setEnabled( false );
    mActionCircleCenterPoint->setEnabled( false );
    mMenuEllipse->setEnabled( false );
    mActionEllipseCenter2Points->setEnabled( false );
    mActionEllipseCenterPoint->setEnabled( false );
    mActionEllipseExtent->setEnabled( false );
    mActionEllipseFoci->setEnabled( false );
    mMenuRectangle->setEnabled( false );
    mActionRectangleCenterPoint->setEnabled( false );
    mActionRectangleExtent->setEnabled( false );
    mActionRectangle3PointsDistance->setEnabled( false );
    mActionRectangle3PointsProjected->setEnabled( false );
    mMenuRegularPolygon->setEnabled( false );
    mActionRegularPolygon2Points->setEnabled( false );
    mActionRegularPolygonCenterPoint->setEnabled( false );
    mActionRegularPolygonCenterCorner->setEnabled( false );
    mMenuEditGeometry->setEnabled( false );
    mActionMoveFeature->setEnabled( false );
    mActionMoveFeatureCopy->setEnabled( false );
    mActionRotateFeature->setEnabled( false );
    mActionScaleFeature->setEnabled( false );
    mActionOffsetCurve->setEnabled( false );
    mActionVertexTool->setEnabled( false );
    mActionVertexToolActiveLayer->setEnabled( false );
    mActionDeleteSelected->setEnabled( false );
    mActionCutFeatures->setEnabled( false );
    mActionCopyFeatures->setEnabled( false );
    mActionPasteFeatures->setEnabled( false );
    mActionCopyStyle->setEnabled( false );
    mActionPasteStyle->setEnabled( false );
    mActionCopyLayer->setEnabled( false );
    // pasting should be allowed if there is a layer in the clipboard
    mActionPasteLayer->setEnabled( clipboard()->hasFormat( QStringLiteral( QGSCLIPBOARD_MAPLAYER_MIME ) ) );
    mActionReverseLine->setEnabled( false );
    mActionTrimExtendFeature->setEnabled( false );

    if ( mUndoDock && mUndoDock->widget() )
      mUndoDock->widget()->setEnabled( false );
    mActionUndo->setEnabled( false );
    mActionRedo->setEnabled( false );
    mActionSimplifyFeature->setEnabled( false );
    mActionAddRing->setEnabled( false );
    mActionFillRing->setEnabled( false );
    mActionAddPart->setEnabled( false );
    mActionDeleteRing->setEnabled( false );
    mActionDeletePart->setEnabled( false );
    mActionReshapeFeatures->setEnabled( false );
    mActionSplitFeatures->setEnabled( false );
    mActionSplitParts->setEnabled( false );
    mActionMergeFeatures->setEnabled( false );
    mMenuEditAttributes->setEnabled( false );
    mActionMergeFeatureAttributes->setEnabled( false );
    mActionMultiEditAttributes->setEnabled( false );
    mActionRotatePointSymbols->setEnabled( false );
    mActionOffsetPointSymbol->setEnabled( false );

    mActionPinLabels->setEnabled( false );
    mActionShowHideLabels->setEnabled( false );
    mActionMoveLabel->setEnabled( false );
    mActionRotateLabel->setEnabled( false );
    mActionChangeLabelProperties->setEnabled( false );

    mActionDiagramProperties->setEnabled( false );

    mActionLocalHistogramStretch->setEnabled( false );
    mActionFullHistogramStretch->setEnabled( false );
    mActionLocalCumulativeCutStretch->setEnabled( false );
    mActionFullCumulativeCutStretch->setEnabled( false );
    mActionIncreaseBrightness->setEnabled( false );
    mActionDecreaseBrightness->setEnabled( false );
    mActionIncreaseContrast->setEnabled( false );
    mActionDecreaseContrast->setEnabled( false );
    mActionIncreaseGamma->setEnabled( false );
    mActionDecreaseGamma->setEnabled( false );
    mActionPanToSelected->setEnabled( false );
    mActionZoomActualSize->setEnabled( false );
    mActionZoomToSelected->setEnabled( false );
    mActionZoomToLayers->setEnabled( false );
    mActionZoomToLayer->setEnabled( false );

    enableMeshEditingTools( false );
    enableDigitizeTechniqueActions( false );

    return;
  }

  mMenuSelect->setEnabled( true );

  mActionLayerProperties->setEnabled( QgsProject::instance()->layerIsEmbedded( layer->id() ).isEmpty() );
  mActionAddToOverview->setEnabled( true );
  mActionPanToSelected->setEnabled( true );
  mActionZoomToSelected->setEnabled( true );
  mActionZoomToLayers->setEnabled( true );
  mActionZoomToLayer->setEnabled( true );

  mActionCopyStyle->setEnabled( true );
  mActionPasteStyle->setEnabled( clipboard()->hasFormat( QStringLiteral( QGSCLIPBOARD_STYLE_MIME ) ) );
  mActionCopyLayer->setEnabled( true );

  // Vector layers
  switch ( layer->type() )
  {
    case QgsMapLayerType::VectorLayer:
    {
      QgsVectorLayer *vlayer = qobject_cast<QgsVectorLayer *>( layer );
      QgsVectorDataProvider *dprovider = vlayer->dataProvider();
      QString addFeatureText;

      bool isEditable = vlayer->isEditable();
      bool layerHasSelection = vlayer->selectedFeatureCount() > 0;
      bool layerHasActions = !vlayer->actions()->actions(QStringLiteral("Canvas")).isEmpty() || !QgsGui::mapLayerActionRegistry()->mapLayerActions(vlayer).isEmpty();
      bool isSpatial = vlayer->isSpatial();

      mActionLocalHistogramStretch->setEnabled( false );
      mActionFullHistogramStretch->setEnabled( false );
      mActionLocalCumulativeCutStretch->setEnabled( false );
      mActionFullCumulativeCutStretch->setEnabled( false );
      mActionIncreaseBrightness->setEnabled( false );
      mActionDecreaseBrightness->setEnabled( false );
      mActionIncreaseContrast->setEnabled( false );
      mActionDecreaseContrast->setEnabled( false );
      mActionIncreaseGamma->setEnabled( false );
      mActionDecreaseGamma->setEnabled( false );
      mActionZoomActualSize->setEnabled( false );
      mActionZoomToLayer->setEnabled( isSpatial );
      mActionLabeling->setEnabled( isSpatial );
      mActionDiagramProperties->setEnabled( isSpatial );
      mActionReverseLine->setEnabled( false );
      mActionTrimExtendFeature->setEnabled( false );

      enableMeshEditingTools( false );

      mActionSelectFeatures->setEnabled( isSpatial );
      mActionSelectPolygon->setEnabled( isSpatial );
      mActionSelectFreehand->setEnabled( isSpatial );
      mActionSelectRadius->setEnabled( isSpatial );
      mActionIdentify->setEnabled( isSpatial || !identifyModeIsActiveLayer );
      mActionSelectByExpression->setEnabled( true );
      mActionSelectByForm->setEnabled( true );
      mActionOpenTable->setEnabled( true );
      mMenuFilterTable->setEnabled( true );
      mActionOpenTableSelected->setEnabled( true );
      mActionOpenTableVisible->setEnabled( true );
      mActionOpenTableEdited->setEnabled( true );
      mActionSelectAll->setEnabled( true );
      mActionReselect->setEnabled( true );
      mActionInvertSelection->setEnabled( true );
      mActionSaveLayerDefinition->setEnabled( true );
      mActionLayerSaveAs->setEnabled( true );
      mActionCopyFeatures->setEnabled( layerHasSelection );
      mActionFeatureAction->setEnabled( layerHasActions );

      if ( !isEditable && mMapCanvas && mMapCanvas->mapTool()
           && ( mMapCanvas->mapTool()->flags() & QgsMapTool::EditTool ) && !mSaveRollbackInProgress )
      {
        mMapCanvas->setMapTool( mNonEditMapTool );
      }

      if ( dprovider )
      {
        bool canChangeAttributes = dprovider->capabilities() & QgsVectorDataProvider::ChangeAttributeValues;
        bool canDeleteFeatures = dprovider->capabilities() & QgsVectorDataProvider::DeleteFeatures;
        bool canAddFeatures = dprovider->capabilities() & QgsVectorDataProvider::AddFeatures;
        bool canChangeGeometry = isSpatial && dprovider->capabilities() & QgsVectorDataProvider::ChangeGeometries;
        bool canSupportEditing = vlayer->supportsEditing();

        mActionLayerSubsetString->setEnabled( !isEditable && dprovider->supportsSubsetString() );

        mActionToggleEditing->setEnabled( canSupportEditing );
        mActionToggleEditing->setChecked( canSupportEditing && isEditable );
        mActionSaveLayerEdits->setEnabled( canSupportEditing && isEditable && vlayer->isModified() );
        mUndoDock->widget()->setEnabled( canSupportEditing && isEditable );
        mActionUndo->setEnabled( canSupportEditing );
        mActionRedo->setEnabled( canSupportEditing );
        mMenuEditGeometry->setEnabled( canSupportEditing && isEditable );

        //start editing/stop editing
        if ( canSupportEditing )
        {
          updateUndoActions();
        }

        mActionPasteFeatures->setEnabled( isEditable && canAddFeatures && !clipboard()->isEmpty() );

        mActionAddFeature->setEnabled( isEditable && canAddFeatures );

        bool enableCircularTools;
        bool enableShapeTools;
        enableCircularTools = isEditable && ( canAddFeatures || canChangeGeometry )
                              && ( vlayer->geometryType() == QgsWkbTypes::LineGeometry || vlayer->geometryType() == QgsWkbTypes::PolygonGeometry );
        enableShapeTools = enableCircularTools;
        mActionCircularStringCurvePoint->setEnabled( enableCircularTools );
        mActionCircularStringRadius->setEnabled( enableCircularTools );
        mMenuCircle->setEnabled( enableShapeTools );
        mActionCircle2Points->setEnabled( enableShapeTools );
        mActionCircle3Points->setEnabled( enableShapeTools );
        mActionCircle3Tangents->setEnabled( enableShapeTools );
        mActionCircle2TangentsPoint->setEnabled( enableShapeTools );
        mActionCircleCenterPoint->setEnabled( enableShapeTools );
        mMenuEllipse->setEnabled( enableShapeTools );
        mActionEllipseCenter2Points->setEnabled( enableShapeTools );
        mActionEllipseCenterPoint->setEnabled( enableShapeTools );
        mActionEllipseExtent->setEnabled( enableShapeTools );
        mActionEllipseFoci->setEnabled( enableShapeTools );
        mMenuRectangle->setEnabled( enableShapeTools );
        mActionRectangleCenterPoint->setEnabled( enableShapeTools );
        mActionRectangleExtent->setEnabled( enableShapeTools );
        mActionRectangle3PointsDistance->setEnabled( enableShapeTools );
        mActionRectangle3PointsProjected->setEnabled( enableShapeTools );
        mMenuRegularPolygon->setEnabled( enableShapeTools );
        mActionRegularPolygon2Points->setEnabled( enableShapeTools );
        mActionRegularPolygonCenterPoint->setEnabled( enableShapeTools );
        mActionRegularPolygonCenterCorner->setEnabled( enableShapeTools );

        //does provider allow deleting of features?
        mActionDeleteSelected->setEnabled( isEditable && canDeleteFeatures && layerHasSelection );
        mActionCutFeatures->setEnabled( isEditable && canDeleteFeatures && layerHasSelection );

        //merge tool needs editable layer and provider with the capability of adding and deleting features
        if ( isEditable && canChangeAttributes )
        {
          mActionMergeFeatures->setEnabled( layerHasSelection && canDeleteFeatures && canAddFeatures );
          mMenuEditAttributes->setEnabled( layerHasSelection );
          mActionMergeFeatureAttributes->setEnabled( layerHasSelection );
          mActionMultiEditAttributes->setEnabled( layerHasSelection );
        }
        else
        {
          mActionMergeFeatures->setEnabled( false );
          mMenuEditAttributes->setEnabled( false );
          mActionMergeFeatureAttributes->setEnabled( false );
          mActionMultiEditAttributes->setEnabled( false );
        }

        bool isMultiPart = QgsWkbTypes::isMultiType( vlayer->wkbType() ) || !dprovider->doesStrictFeatureTypeCheck();

        // moving enabled if geometry changes are supported
        mActionAddPart->setEnabled( isEditable && canChangeGeometry );
        mActionDeletePart->setEnabled( isEditable && canChangeGeometry );
        mActionMoveFeature->setEnabled( isEditable && canChangeGeometry );
        mActionMoveFeatureCopy->setEnabled( isEditable && canChangeGeometry );
        mActionRotateFeature->setEnabled( isEditable && canChangeGeometry );
        mActionScaleFeature->setEnabled( isEditable && canChangeGeometry );
        mActionVertexTool->setEnabled( isEditable && canChangeGeometry );
        mActionVertexToolActiveLayer->setEnabled( isEditable && canChangeGeometry );

        enableDigitizeTechniqueActions( isEditable && canChangeGeometry );

        if ( vlayer->geometryType() == QgsWkbTypes::PointGeometry )
        {
          mActionAddFeature->setIcon( QgsApplication::getThemeIcon( QStringLiteral( "/mActionCapturePoint.svg" ) ) );
          addFeatureText = tr( "Add Point Feature" );
          mActionMoveFeature->setIcon( QgsApplication::getThemeIcon( QStringLiteral( "/mActionMoveFeaturePoint.svg" ) ) );
          mActionMoveFeatureCopy->setIcon( QgsApplication::getThemeIcon( QStringLiteral( "/mActionMoveFeatureCopyPoint.svg" ) ) );

          mActionAddRing->setEnabled( false );
          mActionFillRing->setEnabled( false );
          mActionReshapeFeatures->setEnabled( false );
          mActionSplitFeatures->setEnabled( false );
          mActionSplitParts->setEnabled( false );
          mActionSimplifyFeature->setEnabled( false );
          mActionDeleteRing->setEnabled( false );
          mActionRotatePointSymbols->setEnabled( false );
          mActionOffsetPointSymbol->setEnabled( false );
          mActionOffsetCurve->setEnabled( false );

          if ( isEditable && canChangeAttributes )
          {
            if ( QgsMapToolRotatePointSymbols::layerIsRotatable( vlayer ) )
            {
              mActionRotatePointSymbols->setEnabled( true );
            }
            if ( QgsMapToolOffsetPointSymbol::layerIsOffsetable( vlayer ) )
            {
              mActionOffsetPointSymbol->setEnabled( true );
            }
          }
        }
        else if ( vlayer->geometryType() == QgsWkbTypes::LineGeometry )
        {
          mActionAddFeature->setIcon( QgsApplication::getThemeIcon( QStringLiteral( "/mActionCaptureLine.svg" ) ) );
          addFeatureText = tr( "Add Line Feature" );
          mActionMoveFeature->setIcon( QgsApplication::getThemeIcon( QStringLiteral( "/mActionMoveFeatureLine.svg" ) ) );
          mActionMoveFeatureCopy->setIcon( QgsApplication::getThemeIcon( QStringLiteral( "/mActionMoveFeatureCopyLine.svg" ) ) );

          mActionReshapeFeatures->setEnabled( isEditable && canChangeGeometry );
          mActionSplitFeatures->setEnabled( isEditable && canAddFeatures );
          mActionSplitParts->setEnabled( isEditable && canChangeGeometry && isMultiPart );
          mActionSimplifyFeature->setEnabled( isEditable && canChangeGeometry );
          mActionOffsetCurve->setEnabled( isEditable && canAddFeatures && canChangeAttributes );
          mActionReverseLine->setEnabled( isEditable && canChangeGeometry );
          mActionTrimExtendFeature->setEnabled( isEditable && canChangeGeometry );

          mActionAddRing->setEnabled( false );
          mActionFillRing->setEnabled( false );
          mActionDeleteRing->setEnabled( false );
        }
        else if ( vlayer->geometryType() == QgsWkbTypes::PolygonGeometry )
        {
          mActionAddFeature->setIcon( QgsApplication::getThemeIcon( QStringLiteral( "/mActionCapturePolygon.svg" ) ) );
          addFeatureText = tr( "Add Polygon Feature" );
          mActionMoveFeature->setIcon( QgsApplication::getThemeIcon( QStringLiteral( "/mActionMoveFeature.svg" ) ) );
          mActionMoveFeatureCopy->setIcon( QgsApplication::getThemeIcon( QStringLiteral( "/mActionMoveFeatureCopy.svg" ) ) );

          mActionAddRing->setEnabled( isEditable && canChangeGeometry );
          mActionFillRing->setEnabled( isEditable && canChangeGeometry );
          mActionReshapeFeatures->setEnabled( isEditable && canChangeGeometry );
          mActionSplitFeatures->setEnabled( isEditable && canAddFeatures );
          mActionSplitParts->setEnabled( isEditable && canChangeGeometry && isMultiPart );
          mActionSimplifyFeature->setEnabled( isEditable && canChangeGeometry );
          mActionDeleteRing->setEnabled( isEditable && canChangeGeometry );
          mActionOffsetCurve->setEnabled( isEditable && canAddFeatures && canChangeAttributes );
          mActionTrimExtendFeature->setEnabled( isEditable && canChangeGeometry );
        }
        else if ( vlayer->geometryType() == QgsWkbTypes::NullGeometry )
        {
          mActionAddFeature->setIcon( QgsApplication::getThemeIcon( QStringLiteral( "/mActionNewTableRow.svg" ) ) );
          addFeatureText = tr( "Add Record" );
          mActionAddRing->setEnabled( false );
          mActionFillRing->setEnabled( false );
          mActionReshapeFeatures->setEnabled( false );
          mActionSplitFeatures->setEnabled( false );
          mActionSplitParts->setEnabled( false );
          mActionSimplifyFeature->setEnabled( false );
          mActionDeleteRing->setEnabled( false );
          mActionOffsetCurve->setEnabled( false );
        }

        mActionOpenFieldCalc->setEnabled( true );
        mActionAddFeature->setText( addFeatureText );
        mActionAddFeature->setToolTip( addFeatureText );
        QgsGui::shortcutsManager()->unregisterAction( mActionAddFeature );
        if ( !mActionAddFeature->text().isEmpty() ) // The text will be empty on unknown geometry type -> in this case do not create a shortcut
          QgsGui::shortcutsManager()->registerAction( mActionAddFeature, mActionAddFeature->shortcut().toString() );
      }
      else
      {
        mUndoDock->widget()->setEnabled( false );
        mActionUndo->setEnabled( false );
        mActionRedo->setEnabled( false );
        mActionLayerSubsetString->setEnabled( false );
      }
      break;
    }

    case QgsMapLayerType::RasterLayer:
    {
      const QgsRasterLayer *rlayer = qobject_cast<const QgsRasterLayer *>( layer );
      const QgsRasterDataProvider *dprovider = rlayer->dataProvider();

      if ( dprovider
           && dprovider->dataType( 1 ) != Qgis::DataType::ARGB32
           && dprovider->dataType( 1 ) != Qgis::DataType::ARGB32_Premultiplied )
      {
        if ( dprovider->capabilities() & QgsRasterDataProvider::Size )
        {
          mActionFullHistogramStretch->setEnabled( true );
        }
        else
        {
          // it would hang up reading the data for WMS for example
          mActionFullHistogramStretch->setEnabled( false );
        }
        mActionLocalHistogramStretch->setEnabled( true );
      }
      else
      {
        mActionLocalHistogramStretch->setEnabled( false );
        mActionFullHistogramStretch->setEnabled( false );
      }

      mActionLocalCumulativeCutStretch->setEnabled( true );
      mActionFullCumulativeCutStretch->setEnabled( true );
      mActionIncreaseBrightness->setEnabled( true );
      mActionDecreaseBrightness->setEnabled( true );
      mActionIncreaseContrast->setEnabled( true );
      mActionDecreaseContrast->setEnabled( true );
      mActionIncreaseGamma->setEnabled( true );
      mActionDecreaseGamma->setEnabled( true );

      mActionLayerSubsetString->setEnabled( false );
      mActionFeatureAction->setEnabled( false );
      mActionSelectFeatures->setEnabled( false );
      mActionSelectPolygon->setEnabled( false );
      mActionSelectFreehand->setEnabled( false );
      mActionSelectRadius->setEnabled( false );
      mActionZoomActualSize->setEnabled( true );
      mActionZoomToLayer->setEnabled( true );
      mActionOpenTable->setEnabled( false );
      mMenuFilterTable->setEnabled( false );
      mActionOpenTableSelected->setEnabled( false );
      mActionOpenTableVisible->setEnabled( false );
      mActionOpenTableEdited->setEnabled( false );
      mActionSelectAll->setEnabled( false );
      mActionReselect->setEnabled( false );
      mActionInvertSelection->setEnabled( false );
      mActionSelectByExpression->setEnabled( false );
      mActionSelectByForm->setEnabled( false );
      mActionOpenFieldCalc->setEnabled( false );
      mActionToggleEditing->setEnabled( false );
      mActionToggleEditing->setChecked( false );
      mActionSaveLayerEdits->setEnabled( false );
      mUndoDock->widget()->setEnabled( false );
      mActionUndo->setEnabled( false );
      mActionRedo->setEnabled( false );
      mActionSaveLayerDefinition->setEnabled( true );
      mActionLayerSaveAs->setEnabled( true );
      mActionAddFeature->setEnabled( false );
      mActionCircularStringCurvePoint->setEnabled( false );
      mActionCircularStringRadius->setEnabled( false );
      mMenuCircle->setEnabled( false );
      mActionCircle2Points->setEnabled( false );
      mActionCircle3Points->setEnabled( false );
      mActionCircle3Tangents->setEnabled( false );
      mActionCircle2TangentsPoint->setEnabled( false );
      mActionCircleCenterPoint->setEnabled( false );
      mMenuEllipse->setEnabled( false );
      mActionEllipseCenter2Points->setEnabled( false );
      mActionEllipseCenterPoint->setEnabled( false );
      mActionEllipseExtent->setEnabled( false );
      mActionEllipseFoci->setEnabled( false );
      mMenuRectangle->setEnabled( false );
      mActionRectangleCenterPoint->setEnabled( false );
      mActionRectangleExtent->setEnabled( false );
      mActionRectangle3PointsDistance->setEnabled( false );
      mActionRectangle3PointsProjected->setEnabled( false );
      mMenuRegularPolygon->setEnabled( false );
      mActionRegularPolygon2Points->setEnabled( false );
      mActionRegularPolygonCenterPoint->setEnabled( false );
      mActionRegularPolygonCenterCorner->setEnabled( false );
      mMenuEditAttributes->setEnabled( false );
      mMenuEditGeometry->setEnabled( false );
      mActionReverseLine->setEnabled( false );
      mActionTrimExtendFeature->setEnabled( false );
      mActionDeleteSelected->setEnabled( false );
      mActionAddRing->setEnabled( false );
      mActionFillRing->setEnabled( false );
      mActionAddPart->setEnabled( false );
      mActionVertexTool->setEnabled( false );
      mActionVertexToolActiveLayer->setEnabled( false );
      mActionMoveFeature->setEnabled( false );
      mActionMoveFeatureCopy->setEnabled( false );
      mActionRotateFeature->setEnabled( false );
      mActionScaleFeature->setEnabled( false );
      mActionOffsetCurve->setEnabled( false );
      mActionCopyFeatures->setEnabled( false );
      mActionCutFeatures->setEnabled( false );
      mActionPasteFeatures->setEnabled( false );
      mActionRotatePointSymbols->setEnabled( false );
      mActionOffsetPointSymbol->setEnabled( false );
      mActionDeletePart->setEnabled( false );
      mActionDeleteRing->setEnabled( false );
      mActionSimplifyFeature->setEnabled( false );
      mActionReshapeFeatures->setEnabled( false );
      mActionSplitFeatures->setEnabled( false );
      mActionSplitParts->setEnabled( false );
      mActionLabeling->setEnabled( false );
      mActionDiagramProperties->setEnabled( false );

      enableMeshEditingTools( false );
      enableDigitizeTechniqueActions( false );

      //NOTE: This check does not really add any protection, as it is called on load not on layer select/activate
      //If you load a layer with a provider and idenitfy ability then load another without, the tool would be disabled for both

      //Enable the Identify tool ( GDAL datasets draw without a provider )
      //but turn off if data provider exists and has no Identify capabilities
      mActionIdentify->setEnabled( true );

      if ( identifyModeIsActiveLayer )
      {
        if ( dprovider )
        {
          // does provider allow the identify map tool?
          if ( dprovider->capabilities() & QgsRasterDataProvider::Identify )
          {
            mActionIdentify->setEnabled( true );
          }
          else
          {
            mActionIdentify->setEnabled( false );
          }
        }
      }
      break;
    }

    case QgsMapLayerType::MeshLayer:
    {
      QgsMeshLayer *mlayer = qobject_cast<QgsMeshLayer *>( layer );

      mActionLocalHistogramStretch->setEnabled( false );
      mActionFullHistogramStretch->setEnabled( false );
      mActionLocalCumulativeCutStretch->setEnabled( false );
      mActionFullCumulativeCutStretch->setEnabled( false );
      mActionIncreaseBrightness->setEnabled( false );
      mActionDecreaseBrightness->setEnabled( false );
      mActionIncreaseContrast->setEnabled( false );
      mActionDecreaseContrast->setEnabled( false );
      mActionIncreaseGamma->setEnabled( false );
      mActionDecreaseGamma->setEnabled( false );
      mActionLayerSubsetString->setEnabled( false );
      mActionFeatureAction->setEnabled( false );
      mActionSelectFeatures->setEnabled( false );
      mActionSelectPolygon->setEnabled( false );
      mActionSelectFreehand->setEnabled( false );
      mActionSelectRadius->setEnabled( false );
      mActionZoomActualSize->setEnabled( false );
      mActionZoomToLayer->setEnabled( true );
      mActionOpenTable->setEnabled( false );
      mMenuFilterTable->setEnabled( false );
      mActionOpenTableSelected->setEnabled( false );
      mActionOpenTableVisible->setEnabled( false );
      mActionOpenTableEdited->setEnabled( false );
      mActionSelectAll->setEnabled( false );
      mActionReselect->setEnabled( false );
      mActionInvertSelection->setEnabled( false );
      mActionSelectByExpression->setEnabled( false );
      mActionSelectByForm->setEnabled( false );
      mActionOpenFieldCalc->setEnabled( false );
      mActionSaveLayerEdits->setEnabled( false );
      mUndoDock->widget()->setEnabled( false );
      mActionSaveLayerDefinition->setEnabled( true );
      mActionLayerSaveAs->setEnabled( false );
      mActionAddFeature->setEnabled( false );
      mActionCircularStringCurvePoint->setEnabled( false );
      mActionCircularStringRadius->setEnabled( false );
      mActionDeleteSelected->setEnabled( false );
      mActionAddRing->setEnabled( false );
      mActionFillRing->setEnabled( false );
      mActionAddPart->setEnabled( false );
      mActionVertexTool->setEnabled( false );
      mActionVertexToolActiveLayer->setEnabled( false );
      mActionMoveFeature->setEnabled( false );
      mActionMoveFeatureCopy->setEnabled( false );
      mActionRotateFeature->setEnabled( false );
      mActionScaleFeature->setEnabled( false );
      mActionOffsetCurve->setEnabled( false );
      mActionCopyFeatures->setEnabled( false );
      mActionCutFeatures->setEnabled( false );
      mActionPasteFeatures->setEnabled( false );
      mActionRotatePointSymbols->setEnabled( false );
      mActionOffsetPointSymbol->setEnabled( false );
      mActionDeletePart->setEnabled( false );
      mActionDeleteRing->setEnabled( false );
      mActionSimplifyFeature->setEnabled( false );
      mActionReshapeFeatures->setEnabled( false );
      mActionSplitFeatures->setEnabled( false );
      mActionSplitParts->setEnabled( false );
      mActionLabeling->setEnabled( false );
      mActionDiagramProperties->setEnabled( false );
      mActionIdentify->setEnabled( true );
      enableDigitizeTechniqueActions( false );

      bool canSupportEditing = mlayer->supportsEditing();
      bool isEditable = mlayer->isEditable();
      mActionToggleEditing->setEnabled( canSupportEditing );
      mActionToggleEditing->setChecked( canSupportEditing && isEditable );
      enableMeshEditingTools( isEditable );
      mActionUndo->setEnabled( canSupportEditing && isEditable );
      mActionRedo->setEnabled( canSupportEditing && isEditable );
      updateUndoActions();
    }

    break;

    case QgsMapLayerType::VectorTileLayer:
      mActionLocalHistogramStretch->setEnabled( false );
      mActionFullHistogramStretch->setEnabled( false );
      mActionLocalCumulativeCutStretch->setEnabled( false );
      mActionFullCumulativeCutStretch->setEnabled( false );
      mActionIncreaseBrightness->setEnabled( false );
      mActionDecreaseBrightness->setEnabled( false );
      mActionIncreaseContrast->setEnabled( false );
      mActionDecreaseContrast->setEnabled( false );
      mActionIncreaseGamma->setEnabled( false );
      mActionDecreaseGamma->setEnabled( false );
      mActionLayerSubsetString->setEnabled( false );
      mActionFeatureAction->setEnabled( false );
      mActionSelectFeatures->setEnabled( false );
      mActionSelectPolygon->setEnabled( false );
      mActionSelectFreehand->setEnabled( false );
      mActionSelectRadius->setEnabled( false );
      mActionZoomActualSize->setEnabled( false );
      mActionZoomToLayer->setEnabled( true );
      mActionOpenTable->setEnabled( false );
      mMenuFilterTable->setEnabled( false );
      mActionOpenTableSelected->setEnabled( false );
      mActionOpenTableVisible->setEnabled( false );
      mActionOpenTableEdited->setEnabled( false );
      mActionSelectAll->setEnabled( false );
      mActionReselect->setEnabled( false );
      mActionInvertSelection->setEnabled( false );
      mActionSelectByExpression->setEnabled( false );
      mActionSelectByForm->setEnabled( false );
      mActionOpenFieldCalc->setEnabled( false );
      mActionToggleEditing->setEnabled( false );
      mActionToggleEditing->setChecked( false );
      mActionSaveLayerEdits->setEnabled( false );
      mUndoDock->widget()->setEnabled( false );
      mActionUndo->setEnabled( false );
      mActionRedo->setEnabled( false );
      mActionSaveLayerDefinition->setEnabled( true );
      mActionLayerSaveAs->setEnabled( false );
      mActionAddFeature->setEnabled( false );
      mActionCircularStringCurvePoint->setEnabled( false );
      mActionCircularStringRadius->setEnabled( false );
      mActionDeleteSelected->setEnabled( false );
      mActionAddRing->setEnabled( false );
      mActionFillRing->setEnabled( false );
      mActionAddPart->setEnabled( false );
      mActionVertexTool->setEnabled( false );
      mActionVertexToolActiveLayer->setEnabled( false );
      mActionMoveFeature->setEnabled( false );
      mActionMoveFeatureCopy->setEnabled( false );
      mActionRotateFeature->setEnabled( false );
      mActionScaleFeature->setEnabled( false );
      mActionOffsetCurve->setEnabled( false );
      mActionCopyFeatures->setEnabled( false );
      mActionCutFeatures->setEnabled( false );
      mActionPasteFeatures->setEnabled( false );
      mActionRotatePointSymbols->setEnabled( false );
      mActionOffsetPointSymbol->setEnabled( false );
      mActionDeletePart->setEnabled( false );
      mActionDeleteRing->setEnabled( false );
      mActionSimplifyFeature->setEnabled( false );
      mActionReshapeFeatures->setEnabled( false );
      mActionSplitFeatures->setEnabled( false );
      mActionSplitParts->setEnabled( false );
      mActionLabeling->setEnabled( false );
      mActionDiagramProperties->setEnabled( false );
      mActionIdentify->setEnabled( true );
      enableDigitizeTechniqueActions( false );
      enableMeshEditingTools( false );
      break;

    case QgsMapLayerType::PointCloudLayer:
      mActionLocalHistogramStretch->setEnabled( false );
      mActionFullHistogramStretch->setEnabled( false );
      mActionLocalCumulativeCutStretch->setEnabled( false );
      mActionFullCumulativeCutStretch->setEnabled( false );
      mActionIncreaseBrightness->setEnabled( false );
      mActionDecreaseBrightness->setEnabled( false );
      mActionIncreaseContrast->setEnabled( false );
      mActionDecreaseContrast->setEnabled( false );
      mActionIncreaseGamma->setEnabled( false );
      mActionDecreaseGamma->setEnabled( false );
      mActionLayerSubsetString->setEnabled( false );
      mActionFeatureAction->setEnabled( false );
      mActionSelectFeatures->setEnabled( false );
      mActionSelectPolygon->setEnabled( false );
      mActionSelectFreehand->setEnabled( false );
      mActionSelectRadius->setEnabled( false );
      mActionZoomActualSize->setEnabled( false );
      mActionZoomToLayer->setEnabled( true );
      mActionOpenTable->setEnabled( false );
      mMenuFilterTable->setEnabled( false );
      mActionOpenTableSelected->setEnabled( false );
      mActionOpenTableVisible->setEnabled( false );
      mActionOpenTableEdited->setEnabled( false );
      mActionSelectAll->setEnabled( false );
      mActionReselect->setEnabled( false );
      mActionInvertSelection->setEnabled( false );
      mActionSelectByExpression->setEnabled( false );
      mActionSelectByForm->setEnabled( false );
      mActionOpenFieldCalc->setEnabled( false );
      mActionToggleEditing->setEnabled( false );
      mActionToggleEditing->setChecked( false );
      mActionSaveLayerEdits->setEnabled( false );
      mUndoDock->widget()->setEnabled( false );
      mActionUndo->setEnabled( false );
      mActionRedo->setEnabled( false );
      mActionSaveLayerDefinition->setEnabled( true );
      mActionLayerSaveAs->setEnabled( false );
      mActionAddFeature->setEnabled( false );
      mActionCircularStringCurvePoint->setEnabled( false );
      mActionCircularStringRadius->setEnabled( false );
      mActionDeleteSelected->setEnabled( false );
      mActionAddRing->setEnabled( false );
      mActionFillRing->setEnabled( false );
      mActionAddPart->setEnabled( false );
      mActionVertexTool->setEnabled( false );
      mActionVertexToolActiveLayer->setEnabled( false );
      mActionMoveFeature->setEnabled( false );
      mActionMoveFeatureCopy->setEnabled( false );
      mActionRotateFeature->setEnabled( false );
      mActionScaleFeature->setEnabled( false );
      mActionOffsetCurve->setEnabled( false );
      mActionCopyFeatures->setEnabled( false );
      mActionCutFeatures->setEnabled( false );
      mActionPasteFeatures->setEnabled( false );
      mActionRotatePointSymbols->setEnabled( false );
      mActionOffsetPointSymbol->setEnabled( false );
      mActionDeletePart->setEnabled( false );
      mActionDeleteRing->setEnabled( false );
      mActionSimplifyFeature->setEnabled( false );
      mActionReshapeFeatures->setEnabled( false );
      mActionSplitFeatures->setEnabled( false );
      mActionSplitParts->setEnabled( false );
      mActionLabeling->setEnabled( false );
      mActionDiagramProperties->setEnabled( false );
      mActionIdentify->setEnabled( true );
      enableDigitizeTechniqueActions( false );
      enableMeshEditingTools( false );
      break;

    case QgsMapLayerType::PluginLayer:
    case QgsMapLayerType::AnnotationLayer:
      break;

  }

  refreshFeatureActions();
}
*/

