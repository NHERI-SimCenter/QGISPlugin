#include "qgisapp.h"

#include <QToolBar>
#include <QSplitter>
#include <QLabel>
#include <QAuthenticator>
#include <QUrlQuery>

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
#include <qgsuserinputwidget.h>
#include <qgsrenderer.h>
#include <qgstransaction.h>
#include <qgstransactiongroup.h>
#include <qgssettingsregistrycore.h>
#include <qgsvectorlayer.h>
#include <qgsvectorlayerutils.h>
#include <qgsvectorlayertools.h>
#include <qgsvectortilelayerproperties.h>
#include <qgsguivectorlayertools.h>
#include <qgslayertreeregistrybridge.h>
#include <qgspointcloudlayerproperties.h>
#include <qgsclipboard.h>
#include <qgsfixattributedialog.h>
#include <qgsproviderguiregistry.h>
#include <qgsrasterlayerproperties.h>
#include <qgsmeshlayerproperties.h>
#include <qgslayerstylingwidget.h>
#include <qgsvectorlayerproperties.h>
#include <qgsauxiliarystorage.h>
#include <qgspluginlayer.h>
#include <qgspluginlayerregistry.h>
#include <qgssourceselectproviderregistry.h>
#include <qgsarcgisrestdataitemguiprovider.h>
#include <qgswmsdataitemguiproviders.h>
#include <qgswmsprovidergui.h>
#include <qgsmbtiles.h>
#include <qgsprojectstorage.h>
#include <qgsprojectstorageregistry.h>
#include <qgshandlebadlayers.h>
#include <qgspythonrunner.h>
#include <qgslegendfilterbutton.h>
#include <qgsstatusbar.h>
#include <qgsvectorfilewriter.h>
#include <qgscustomprojectopenhandler.h>
#include <qgsziputils.h>
#include <qgsvectortilelayer.h>
#include <qgsprojectviewsettings.h>

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

QgisApp *QgisApp::sInstance = nullptr;

QgisApp::QgisApp(QWidget* parent, Qt::WindowFlags fl) : QMainWindow( parent, fl )
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

    QgsGui::instance();

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

    connect(mMapCanvas, &QgsMapCanvas::messageEmitted, this, &QgisApp::displayMessage);

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

    QgsGui::providerGuiRegistry()->registerGuis( this );


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
    //     connect( this, &QgisApp::customCrsValidation,
    //              this, &QgisApp::validateCrs );
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
    QgsGui::instance()->dataItemGuiProviderRegistry()->addProvider( new QgsArcGisRestDataItemGuiProvider() );

//    auto wmsProvGui = new QgsWmsProviderGuiMetadata();

//    auto providers = wmsProvGui->sourceSelectProviders();

//    for(auto&& it : providers)
//    {
//        QgsGui::instance()->sourceSelectProviderRegistry()->addProvider(it);
//    }

    mBrowserModel = new QgsBrowserGuiModel( this );

    QString str1 = "tilePixelRatio=2&type=xyz&url=http://tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png&zmax=18&zmin=0";
    QString str2 = "Open Street Map";
    QString str3 = "wms";

    this->addRasterLayer(str1,str2,str3);


    //        QgsWmsProviderGuiMetadata
    //        qgswmsprovidergui

    //        QgsWmsProvider
    //qgswmsprovider
    //        auto dsWidget = this->createDataSourceWidget();
    //        QgsGui::sourceSelectProviderRegistry()->addProvider(dsWidget);

    // show the virtual layer dialog
    //        QDialog *dts = dynamic_cast<QDialog *>( QgsGui::sourceSelectProviderRegistry()->createSelectionWidget( QStringLiteral( "XYZ" ), this, Qt::Widget, QgsProviderRegistry::WidgetMode::Embedded ) );
    //        if ( !dts )
    //        {
    //          QMessageBox::warning( this, tr( "Add Virtual Layer" ), tr( "Cannot get virtual layer select dialog from provider." ) );
    //          return;
    //        }

    //        dts->exec();

    //    dataSourceManager();

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


QString QgisApp::saveAsFile( QgsMapLayer *layer, const bool onlySelected, const bool defaultToAddToMap )
{

    return QString();
}


QgsOptions *QgisApp::createOptionsDialog( QWidget *parent )
{

    return nullptr;
}


void QgisApp::showOptionsDialog( QWidget *parent, const QString &currentPage, int pageNumber )
{


}


QgsClipboard *QgisApp::clipboard()
{
    return mInternalClipboard;
}


void QgisApp::saveEdits( QgsMapLayer *layer, bool leaveEditable, bool triggerRepaint )
{
    if ( !layer )
        return;

    switch ( layer->type() )
    {
    case QgsMapLayerType::VectorLayer:
        return saveVectorLayerEdits( layer, leaveEditable, triggerRepaint );
    case QgsMapLayerType::MeshLayer:
        return saveMeshLayerEdits( layer, leaveEditable, triggerRepaint );
    case QgsMapLayerType::RasterLayer:
    case QgsMapLayerType::PluginLayer:
    case QgsMapLayerType::VectorTileLayer:
    case QgsMapLayerType::AnnotationLayer:
    case QgsMapLayerType::PointCloudLayer:
        break;
    }
}


void QgisApp::saveEdits()
{
    const auto constSelectedLayers = mLayerTreeView->selectedLayers();
    for ( QgsMapLayer *layer : constSelectedLayers )
    {
        saveEdits( layer, true, false );
    }
    refreshMapCanvas();
    //  activateDeactivateLayerRelatedActions( activeLayer() );
}


QSize QgisApp::iconSize( bool dockedToolbar ) const
{
    return QgsGuiUtils::iconSize( dockedToolbar );
}


void QgisApp::saveVectorLayerEdits( QgsMapLayer *layer, bool leaveEditable, bool triggerRepaint )
{
    QgsVectorLayer *vlayer = qobject_cast<QgsVectorLayer *>( layer );
    if ( !vlayer || !vlayer->isEditable() || !vlayer->isModified() )
        return;

    if ( vlayer == activeLayer() )
        mSaveRollbackInProgress = true;

    if ( !vlayer->commitChanges( !leaveEditable ) )
    {
        mSaveRollbackInProgress = false;
        commitError( vlayer );
    }

    if ( triggerRepaint )
    {
        vlayer->triggerRepaint();
    }
}


void QgisApp::saveMeshLayerEdits( QgsMapLayer *layer, bool leaveEditable, bool triggerRepaint )
{
    QgsMeshLayer *mlayer = qobject_cast<QgsMeshLayer *>( layer );
    if ( !mlayer || !mlayer->isEditable() || !mlayer->isModified() )
        return;

    if ( mlayer == activeLayer() )
        mSaveRollbackInProgress = true;

    QgsCanvasRefreshBlocker refreshBlocker;
    QgsCoordinateTransform transform( mlayer->crs(), mMapCanvas->mapSettings().destinationCrs(), QgsProject::instance() );
    mlayer->commitFrameEditing( transform, leaveEditable );

    if ( triggerRepaint )
    {
        mlayer->triggerRepaint();
    }
}


void QgisApp::copySelectionToClipboard( QgsMapLayer *layerContainingSelection )
{
    QgsVectorLayer *selectionVectorLayer = qobject_cast<QgsVectorLayer *>( layerContainingSelection ? layerContainingSelection : activeLayer() );
    if ( !selectionVectorLayer )
        return;

    // Test for feature support in this layer
    clipboard()->replaceWithCopyOf( selectionVectorLayer );
}


void QgisApp::cutSelectionToClipboard( QgsMapLayer *layerContainingSelection )
{
    // Test for feature support in this layer
    QgsVectorLayer *selectionVectorLayer = qobject_cast<QgsVectorLayer *>( layerContainingSelection ? layerContainingSelection : activeLayer() );
    if ( !selectionVectorLayer )
        return;

    if ( !selectionVectorLayer->isEditable() )
    {
        visibleMessageBar()->pushMessage( tr( "Layer not editable" ),
                                          tr( "The current layer is not editable. Choose 'Start editing' in the digitizing toolbar." ),
                                          Qgis::MessageLevel::Info );
        return;
    }

    clipboard()->replaceWithCopyOf( selectionVectorLayer );

    selectionVectorLayer->beginEditCommand( tr( "Features cut" ) );
    selectionVectorLayer->deleteSelectedFeatures();
    selectionVectorLayer->endEditCommand();
}


void QgisApp::addTabifiedDockWidget( Qt::DockWidgetArea area, QDockWidget *dockWidget, const QStringList &tabifyWith, bool raiseTab )
{
    QList< QDockWidget * > dockWidgetsInArea;
    const auto dockWidgets = findChildren< QDockWidget * >();
    for ( QDockWidget *w : dockWidgets )
    {
        if ( w->isVisible() && dockWidgetArea( w ) == area )
        {
            dockWidgetsInArea << w;
        }
    }

    addDockWidget( area, dockWidget );  // First add the dock widget, then attempt to tabify
    if ( dockWidgetsInArea.length() > 0 )
    {
        // Get the base dock widget that we'll use to tabify our new dockWidget
        QDockWidget *tabifyWithDockWidget = nullptr;
        if ( !tabifyWith.isEmpty() )
        {
            // Iterate the list of object names looking for a
            // dock widget to tabify the new one on top of it
            bool objectNameFound = false;
            for ( int i = 0; i < tabifyWith.size(); i++ )
            {
                for ( QDockWidget *cw : dockWidgetsInArea )
                {
                    if ( cw->objectName() == tabifyWith.at( i ) )
                    {
                        tabifyWithDockWidget = cw;
                        objectNameFound = true;  // Also exit the outer for loop
                        break;
                    }
                }
                if ( objectNameFound )
                {
                    break;
                }
            }
        }
        if ( !tabifyWithDockWidget )
        {
            tabifyWithDockWidget = dockWidgetsInArea.at( 0 );  // Last resort
        }

        QTabBar *existentTabBar = nullptr;
        int currentIndex = -1;
        if ( !raiseTab && dockWidgetsInArea.length() > 1 )
        {
            // Chances are we've already got a tabBar, if so, get
            // currentIndex to restore status after inserting our new tab
            const QList<QTabBar *> tabBars = findChildren<QTabBar *>( QString(), Qt::FindDirectChildrenOnly );
            bool tabBarFound = false;
            for ( QTabBar *tabBar : tabBars )
            {
                for ( int i = 0; i < tabBar->count(); i++ )
                {
                    if ( tabBar->tabText( i ) == tabifyWithDockWidget->windowTitle() )
                    {
                        existentTabBar = tabBar;
                        currentIndex = tabBar->currentIndex();
                        tabBarFound = true;
                        break;
                    }
                }
                if ( tabBarFound )
                {
                    break;
                }
            }
        }

        // Now we can put the new dockWidget on top of tabifyWith
        tabifyDockWidget( tabifyWithDockWidget, dockWidget );

        // Should we restore dock widgets status?
        if ( !raiseTab )
        {
            if ( existentTabBar )
            {
                existentTabBar->setCurrentIndex( currentIndex );
            }
            else
            {
                tabifyWithDockWidget->raise();  // Single base dock widget, we can just raise it
            }
        }
    }
}


QgsAttributeEditorContext QgisApp::createAttributeEditorContext()
{
    QgsAttributeEditorContext context;
    context.setVectorLayerTools( vectorLayerTools() );
    context.setMapCanvas( mapCanvas() );
    context.setCadDockWidget( cadDockWidget() );
    context.setMainMessageBar( messageBar() );
    return context;
}


void QgisApp::pasteFromClipboard( QgsMapLayer *destinationLayer )
{
    QgsVectorLayer *pasteVectorLayer = qobject_cast<QgsVectorLayer *>( destinationLayer ? destinationLayer : activeLayer() );
    if ( !pasteVectorLayer )
        return;

    if ( !pasteVectorLayer->isEditable() )
    {
        visibleMessageBar()->pushMessage( tr( "Layer not editable" ),
                                          tr( "The current layer is not editable. Choose 'Start editing' in the digitizing toolbar." ),
                                          Qgis::MessageLevel::Info );
        return;
    }

    pasteVectorLayer->beginEditCommand( tr( "Features pasted" ) );
    QgsFeatureList features = clipboard()->transformedCopyOf( pasteVectorLayer->crs(), pasteVectorLayer->fields() );
    int nTotalFeatures = features.count();
    QgsExpressionContext context = pasteVectorLayer->createExpressionContext();

    QgsFeatureList compatibleFeatures( QgsVectorLayerUtils::makeFeaturesCompatible( features, pasteVectorLayer, QgsFeatureSink::RegeneratePrimaryKey ) );
    QgsVectorLayerUtils::QgsFeaturesDataList newFeaturesDataList;
    newFeaturesDataList.reserve( compatibleFeatures.size() );

    // Count collapsed geometries
    int invalidGeometriesCount = 0;

    for ( const auto &feature : std::as_const( compatibleFeatures ) )
    {

        QgsGeometry geom = feature.geometry();

        if ( !( geom.isEmpty() || geom.isNull( ) ) )
        {
            // avoid intersection if enabled in digitize settings
            QList<QgsVectorLayer *>  avoidIntersectionsLayers;
            switch ( QgsProject::instance()->avoidIntersectionsMode() )
            {
            case QgsProject::AvoidIntersectionsMode::AvoidIntersectionsCurrentLayer:
                avoidIntersectionsLayers.append( pasteVectorLayer );
                break;
            case QgsProject::AvoidIntersectionsMode::AvoidIntersectionsLayers:
                avoidIntersectionsLayers = QgsProject::instance()->avoidIntersectionsLayers();
                break;
            case QgsProject::AvoidIntersectionsMode::AllowIntersections:
                break;
            }
            if ( avoidIntersectionsLayers.size() > 0 )
            {
                geom.avoidIntersections( avoidIntersectionsLayers );
            }

            // count collapsed geometries
            if ( geom.isEmpty() || geom.isNull( ) )
                invalidGeometriesCount++;
        }

        QgsAttributeMap attrMap;
        for ( int i = 0; i < feature.attributes().count(); i++ )
        {
            attrMap[i] = feature.attribute( i );
        }
        newFeaturesDataList << QgsVectorLayerUtils::QgsFeatureData( geom, attrMap );
    }

    // now create new feature using pasted feature as a template. This automatically handles default
    // values and field constraints
    QgsFeatureList newFeatures {QgsVectorLayerUtils::createFeatures( pasteVectorLayer, newFeaturesDataList, &context )};

    // check constraints
    bool hasStrongConstraints = false;

    for ( const QgsField &field : pasteVectorLayer->fields() )
    {
        if ( ( field.constraints().constraints() & QgsFieldConstraints::ConstraintUnique && field.constraints().constraintStrength( QgsFieldConstraints::ConstraintUnique ) & QgsFieldConstraints::ConstraintStrengthHard )
             || ( field.constraints().constraints() & QgsFieldConstraints::ConstraintNotNull && field.constraints().constraintStrength( QgsFieldConstraints::ConstraintNotNull ) & QgsFieldConstraints::ConstraintStrengthHard )
             || ( field.constraints().constraints() & QgsFieldConstraints::ConstraintExpression && !field.constraints().constraintExpression().isEmpty() && field.constraints().constraintStrength( QgsFieldConstraints::ConstraintExpression ) & QgsFieldConstraints::ConstraintStrengthHard )
             )
        {
            hasStrongConstraints = true;
            break;
        }
    }

    if ( hasStrongConstraints )
    {
        QgsFeatureList validFeatures = newFeatures;
        QgsFeatureList invalidFeatures;
        QMutableListIterator<QgsFeature> it( validFeatures );
        while ( it.hasNext() )
        {
            QgsFeature &f = it.next();
            for ( int idx = 0; idx < pasteVectorLayer->fields().count(); ++idx )
            {
                QStringList errors;
                if ( !QgsVectorLayerUtils::validateAttribute( pasteVectorLayer, f, idx, errors, QgsFieldConstraints::ConstraintStrengthHard, QgsFieldConstraints::ConstraintOriginNotSet ) )
                {
                    invalidFeatures << f;
                    it.remove();
                    break;
                }
            }
        }

        if ( !invalidFeatures.isEmpty() )
        {
            newFeatures.clear();

            QgsAttributeEditorContext context( createAttributeEditorContext() );
            context.setAllowCustomUi( false );
            context.setFormMode( QgsAttributeEditorContext::StandaloneDialog );

            QgsFixAttributeDialog *dialog = new QgsFixAttributeDialog( pasteVectorLayer, invalidFeatures, this, context );

            connect( dialog, &QgsFixAttributeDialog::finished, this, [ = ]( int feedback )
            {
                QgsFeatureList features = newFeatures;
                switch ( feedback )
                {
                case QgsFixAttributeDialog::PasteValid:
                    //paste valid and fixed, vanish unfixed
                    features << validFeatures << dialog->fixedFeatures();
                    break;
                case QgsFixAttributeDialog::PasteAll:
                    //paste all, even unfixed
                    features << validFeatures << dialog->fixedFeatures() << dialog->unfixedFeatures();
                    break;
                }
                pasteFeatures( pasteVectorLayer, invalidGeometriesCount, nTotalFeatures, features );
                dialog->deleteLater();
            } );
            dialog->show();
            return;
        }
    }

    pasteFeatures( pasteVectorLayer, invalidGeometriesCount, nTotalFeatures, newFeatures );
}

void QgisApp::pasteFeatures( QgsVectorLayer *pasteVectorLayer, int invalidGeometriesCount, int nTotalFeatures, QgsFeatureList &features )
{
    int nCopiedFeatures = features.count();
    if ( pasteVectorLayer->addFeatures( features ) )
    {
        QgsFeatureIds newIds;
        newIds.reserve( features.size() );
        for ( const QgsFeature &f : std::as_const( features ) )
        {
            newIds << f.id();
        }

        pasteVectorLayer->selectByIds( newIds );
    }
    else
    {
        nCopiedFeatures = 0;
    }
    pasteVectorLayer->endEditCommand();
    pasteVectorLayer->updateExtents();

    Qgis::MessageLevel level = ( nCopiedFeatures == 0 || invalidGeometriesCount > 0 ) ? Qgis::MessageLevel::Warning : Qgis::MessageLevel::Info;
    QString message;
    if ( nCopiedFeatures == 0 )
    {
        message = tr( "No features pasted." );
    }
    else if ( nCopiedFeatures == nTotalFeatures )
    {
        message = tr( "%1 features were pasted." ).arg( nCopiedFeatures );
    }
    else
    {
        message = tr( "%1 of %2 features could be pasted." ).arg( nCopiedFeatures ).arg( nTotalFeatures );
    }

    // warn the user if the pasted features have invalid geometries
    if ( invalidGeometriesCount > 0 )
        message +=  invalidGeometriesCount == 1 ? tr( " Geometry collapsed due to intersection avoidance." ) :
                                                  tr( "%1 geometries collapsed due to intersection avoidance." )
                                                  .arg( invalidGeometriesCount );

    visibleMessageBar()->pushMessage( tr( "Paste features" ),
                                      message,
                                      level );

    pasteVectorLayer->triggerRepaint();
}


void QgisApp::setupLayerTreeViewFromSettings()
{
    QgsSettings s;

    QgsLayerTreeModel *model = mLayerTreeView->layerTreeModel();
    QFont fontLayer, fontGroup;
    fontLayer.setBold( true );
    fontGroup.setBold( false );
    model->setLayerTreeNodeFont( QgsLayerTreeNode::NodeLayer, fontLayer );
    model->setLayerTreeNodeFont( QgsLayerTreeNode::NodeGroup, fontGroup );
}


void QgisApp::commitError( QgsVectorLayer *vlayer )
{
    const QStringList commitErrors = vlayer->commitErrors();
    if ( !vlayer->allowCommit() && commitErrors.empty() )
    {
        return;
    }

    QgsMessageViewer *mv = new QgsMessageViewer();
    mv->setWindowTitle( tr( "Commit Errors" ) );
    mv->setMessageAsPlainText( tr( "Could not commit changes to layer %1" ).arg( vlayer->name() )
                               + "\n\n"
                             + tr( "Errors: %1\n" ).arg( commitErrors.join( QLatin1String( "\n  " ) ) )
                               );

    QToolButton *showMore = new QToolButton();
    // store pointer to vlayer in data of QAction
    QAction *act = new QAction( showMore );
    act->setData( QVariant( QMetaType::QObjectStar, &vlayer ) );
    act->setText( tr( "Show more" ) );
    showMore->setStyleSheet( QStringLiteral( "background-color: rgba(255, 255, 255, 0); color: black; text-decoration: underline;" ) );
    showMore->setCursor( Qt::PointingHandCursor );
    showMore->setSizePolicy( QSizePolicy::Maximum, QSizePolicy::Preferred );
    showMore->addAction( act );
    showMore->setDefaultAction( act );
    connect( showMore, &QToolButton::triggered, mv, &QDialog::exec );
    connect( showMore, &QToolButton::triggered, showMore, &QObject::deleteLater );

    // no timeout set, since notice needs attention and is only shown first time layer is labeled
    QgsMessageBarItem *errorMsg = new QgsMessageBarItem(
                tr( "Commit errors" ),
                tr( "Could not commit changes to layer %1" ).arg( vlayer->name() ),
                showMore,
                Qgis::MessageLevel::Warning,
                0,
                messageBar() );
    messageBar()->pushItem( errorMsg );
}


QString QgisApp::saveAsRasterFile( QgsRasterLayer *rasterLayer, const bool defaultAddToCanvas )
{

    return QString();
}


QgsMessageBar *QgisApp::visibleMessageBar()
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


void QgisApp::addUserInputWidget( QWidget *widget )
{
    mUserInputDockWidget->addUserInputWidget( widget );
}


void QgisApp::handleDropUriList( const QgsMimeDataUtils::UriList &lst )
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


void QgisApp::onActiveLayerChanged( QgsMapLayer *layer )
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


bool QgisApp::checkMemoryLayers()
{
  if ( !QgsSettings().value( QStringLiteral( "askToSaveMemoryLayers" ), true, QgsSettings::App ).toBool() )
    return true;

  // check to see if there are any temporary layers present (with features)
  bool hasTemporaryLayers = false;
  bool hasMemoryLayers = false;

  const QMap<QString, QgsMapLayer *> layers = QgsProject::instance()->mapLayers();
  for ( auto it = layers.begin(); it != layers.end(); ++it )
  {
    if ( it.value() && it.value()->providerType() == QLatin1String( "memory" ) )
    {
      QgsVectorLayer *vl = qobject_cast< QgsVectorLayer * >( it.value() );
      if ( vl && vl->featureCount() != 0 && !vl->customProperty( QStringLiteral( "skipMemoryLayersCheck" ) ).toInt() )
      {
        hasMemoryLayers = true;
        break;
      }
    }
    else if ( it.value() && it.value()->isTemporary() )
    {
      hasTemporaryLayers = true;
    }
  }

  bool close = true;
  if ( hasTemporaryLayers )
    close &= QMessageBox::warning( this,
                                   tr( "Close Project" ),
                                   tr( "This project includes one or more temporary layers. These layers are not permanently saved and their contents will be lost. Are you sure you want to proceed?" ),
                                   QMessageBox::Yes | QMessageBox::Cancel, QMessageBox::Cancel ) == QMessageBox::Yes ;
  else if ( hasMemoryLayers )
    // use the more specific warning for memory layers
    close &= QMessageBox::warning( this,
                                   tr( "Close Project" ),
                                   tr( "This project includes one or more temporary scratch layers. These layers are not saved to disk and their contents will be permanently lost. Are you sure you want to proceed?" ),
                                   QMessageBox::Yes | QMessageBox::Cancel, QMessageBox::Cancel ) == QMessageBox::Yes;

  return close;
}

bool QgisApp::checkUnsavedLayerEdits()
{
  // check to see if there are any vector layers with unsaved provider edits
  // to ensure user has opportunity to save any editing
  if ( QgsProject::instance()->count() > 0 )
  {
    const QMap<QString, QgsMapLayer *> layers = QgsProject::instance()->mapLayers();
    for ( auto it = layers.begin(); it != layers.end(); ++it )
    {
      if ( QgsVectorLayer *vl = qobject_cast<QgsVectorLayer *>( it.value() ) )
      {
        // note that we skip the unsaved edits check for memory layers -- it's misleading, because their contents aren't actually
        // saved if this is part of a project close operation. Instead we let these get picked up by checkMemoryLayers()
        if ( ! vl->dataProvider() || vl->providerType() == QLatin1String( "memory" ) )
          continue;

        const bool hasUnsavedEdits = ( vl->isEditable() && vl->isModified() );
        if ( !hasUnsavedEdits )
          continue;

        if ( !toggleEditing( vl, true ) )
          return false;
      }
    }
  }

  return true;
}

bool QgisApp::openLayer( const QString &fileName, bool allowInteractive )
{
  bool ok = false;
  const QFileInfo fileInfo( fileName );

  // highest priority = delegate to provider registry to handle
  const QList< QgsProviderRegistry::ProviderCandidateDetails > candidateProviders = QgsProviderRegistry::instance()->preferredProvidersForUri( fileName );
  if ( candidateProviders.size() == 1 && candidateProviders.at( 0 ).layerTypes().size() == 1 )
  {
    // one good candidate provider and possible layer type -- that makes things nice and easy!
    switch ( candidateProviders.at( 0 ).layerTypes().at( 0 ) )
    {
      case QgsMapLayerType::VectorLayer:
      case QgsMapLayerType::RasterLayer:
      case QgsMapLayerType::MeshLayer:
      case QgsMapLayerType::AnnotationLayer:
      case QgsMapLayerType::PluginLayer:
      case QgsMapLayerType::VectorTileLayer:
        // not supported here yet!
        break;

      case QgsMapLayerType::PointCloudLayer:
//        ok = static_cast< bool >( addPointCloudLayerPrivate( fileName, fileInfo.completeBaseName(), candidateProviders.at( 0 ).metadata()->key(), false ) );
        break;
    }
  }

  if ( ok )
    return true;

//  CPLPushErrorHandler( CPLQuietErrorHandler );

  // if needed prompt for zipitem layers
  QString vsiPrefix = QgsZipItem::vsiPrefix( fileName );
  if ( vsiPrefix == QLatin1String( "/vsizip/" ) || vsiPrefix == QLatin1String( "/vsitar/" ) )
  {
    if ( askUserForZipItemLayers( fileName, {} ) )
    {
//      CPLPopErrorHandler();
      return true;
    }
  }

  if ( fileName.endsWith( QStringLiteral( ".mbtiles" ), Qt::CaseInsensitive ) )
  {
    QgsMbTiles reader( fileName );
    if ( reader.open() )
    {
      if ( reader.metadataValue( "format" ) == QLatin1String( "pbf" ) )
      {
        // these are vector tiles
        QUrlQuery uq;
        uq.addQueryItem( QStringLiteral( "type" ), QStringLiteral( "mbtiles" ) );
        uq.addQueryItem( QStringLiteral( "url" ), fileName );
        std::unique_ptr<QgsVectorTileLayer> vtLayer( new QgsVectorTileLayer( uq.toString(), fileInfo.completeBaseName() ) );
        if ( vtLayer->isValid() )
        {
          QgsProject::instance()->addMapLayer( vtLayer.release() );
          return true;
        }
      }
      else // raster tiles
      {
        // prefer to use WMS provider's implementation to open MBTiles rasters
        QUrlQuery uq;
        uq.addQueryItem( QStringLiteral( "type" ), QStringLiteral( "mbtiles" ) );
        uq.addQueryItem( QStringLiteral( "url" ), QUrl::fromLocalFile( fileName ).toString() );
        if ( addRasterLayer( uq.toString(), fileInfo.completeBaseName(), QStringLiteral( "wms" ) ) )
          return true;
      }
    }
  }

  QList< QgsProviderSublayerModel::NonLayerItem > nonLayerItems;
  if ( QgsProjectStorage *ps = QgsApplication::projectStorageRegistry()->projectStorageFromUri( fileName ) )
  {
    const QStringList projects = ps->listProjects( fileName );
    for ( const QString &project : projects )
    {
      QgsProviderSublayerModel::NonLayerItem projectItem;
      projectItem.setType( QStringLiteral( "project" ) );
      projectItem.setName( project );
      projectItem.setUri( QStringLiteral( "%1://%2?projectName=%3" ).arg( ps->type(), fileName, project ) );
      projectItem.setIcon( QgsApplication::getThemeIcon( QStringLiteral( "/mIconQgsProjectFile.svg" ) ) );
      nonLayerItems << projectItem;
    }
  }

  // query sublayers
  QList< QgsProviderSublayerDetails > sublayers = QgsProviderRegistry::instance()->querySublayers( fileName );

  if ( !sublayers.empty() || !nonLayerItems.empty() )
  {
    const bool detailsAreIncomplete = QgsProviderUtils::sublayerDetailsAreIncomplete( sublayers, QgsProviderUtils::SublayerCompletenessFlag::IgnoreUnknownFeatureCount );
    const bool singleSublayerOnly = sublayers.size() == 1;
    QString groupName;

    if ( allowInteractive && ( !singleSublayerOnly || detailsAreIncomplete || !nonLayerItems.empty() ) )
    {
      // ask user for sublayers (unless user settings dictate otherwise!)
      switch ( shouldAskUserForSublayers( sublayers, !nonLayerItems.empty() ) )
      {
        case SublayerHandling::AskUser:
        {
          // prompt user for sublayers
          QgsProviderSublayersDialog dlg( fileName, fileName, sublayers, {}, this );
          dlg.setNonLayerItems( nonLayerItems );

          if ( dlg.exec() )
          {
            sublayers = dlg.selectedLayers();
            nonLayerItems = dlg.selectedNonLayerItems();
          }
          else
          {
            sublayers.clear(); // dialog was canceled, so don't add any sublayers
            nonLayerItems.clear();
          }
          groupName = dlg.groupName();
          break;
        }

        case SublayerHandling::LoadAll:
        {
          if ( detailsAreIncomplete )
          {
            // requery sublayers, resolving geometry types
            sublayers = QgsProviderRegistry::instance()->querySublayers( fileName, Qgis::SublayerQueryFlag::ResolveGeometryType );
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
      sublayers = QgsProviderRegistry::instance()->querySublayers( fileName, Qgis::SublayerQueryFlag::ResolveGeometryType );
    }

    ok = true;

    // now add sublayers
    if ( !sublayers.empty() )
    {
      QgsCanvasRefreshBlocker refreshBlocker;
      QgsSettings settings;

      QString base = QgsProviderUtils::suggestLayerNameFromFilePath( fileName );
      if ( settings.value( QStringLiteral( "qgis/formatLayerName" ), false ).toBool() )
      {
        base = QgsMapLayer::formatLayerName( base );
      }

      addSublayers( sublayers, base, groupName );
//      activateDeactivateLayerRelatedActions( activeLayer() );
    }
    else if ( !nonLayerItems.empty() )
    {
      QgsCanvasRefreshBlocker refreshBlocker;
      if ( checkTasksDependOnProject() )
        return true;

      // possibly save any pending work before opening a different project
      if ( checkUnsavedLayerEdits() && checkMemoryLayers() && saveDirty() )
      {
        // error handling and reporting is in addProject() function
        addProject( nonLayerItems.at( 0 ).uri() );
      }
      return true;
    }
  }

//  CPLPopErrorHandler();

  if ( !ok )
  {
    // maybe a known file type, which couldn't be opened due to a missing dependency... (eg. las for a non-pdal-enabled build)
    QgsProviderRegistry::UnusableUriDetails details;
    if ( QgsProviderRegistry::instance()->handleUnusableUri( fileName, details ) )
    {
      ok = true;

      if ( details.detailedWarning.isEmpty() )
        visibleMessageBar()->pushMessage( QString(), details.warning, Qgis::MessageLevel::Critical );
      else
        visibleMessageBar()->pushMessage( QString(), details.warning, details.detailedWarning, Qgis::MessageLevel::Critical );
    }
  }

  if ( !ok )
  {
    // we have no idea what this file is...
    QgsMessageLog::logMessage( tr( "Unable to load %1" ).arg( fileName ) );

    const QString msg = tr( "%1 is not a valid or recognized data source." ).arg( fileName );
    visibleMessageBar()->pushMessage( tr( "Invalid Data Source" ), msg, Qgis::MessageLevel::Critical );
  }

  return ok;
}


void QgisApp::closeProject()
{
  QgsCanvasRefreshBlocker refreshBlocker;

  // unload the project macros before changing anything
  if ( mPythonMacrosEnabled )
  {
    QgsPythonRunner::run( QStringLiteral( "qgis.utils.unloadProjectMacros();" ) );
  }

  mPythonMacrosEnabled = false;

  mLegendExpressionFilterButton->setExpressionText( QString() );
  mLegendExpressionFilterButton->setChecked( false );
  mFilterLegendByMapContentAction->setChecked( false );

  closeAdditionalMapCanvases();
  closeAdditional3DMapCanvases();

  deleteLayoutDesigners();

  // ensure layout widgets are fully deleted
  QgsApplication::sendPostedEvents( nullptr, QEvent::DeferredDelete );

  removeAnnotationItems();

  // clear out any stuff from project
  mMapCanvas->setLayers( QList<QgsMapLayer *>() );
  mMapCanvas->clearCache();
  mOverviewCanvas->setLayers( QList<QgsMapLayer *>() );

  // Avoid unnecessary layer changed handling for each layer removed - instead,
  // defer the handling until we've removed all layers
  mBlockActiveLayerChanged = true;
  QgsProject::instance()->clear();
  mBlockActiveLayerChanged = false;

  onActiveLayerChanged( activeLayer() );
}


bool QgisApp::addProject( const QString &projectFile )
{
  QgsCanvasRefreshBlocker refreshBlocker;

  bool returnCode = false;
  std::unique_ptr< QgsProjectDirtyBlocker > dirtyBlocker = std::make_unique< QgsProjectDirtyBlocker >( QgsProject::instance() );
  QObject connectionScope; // manually control scope of layersChanged lambda connection - we need the connection automatically destroyed when this function finishes
  bool badLayersHandled = false;
  connect( mAppBadLayersHandler, &QgsHandleBadLayersHandler::layersChanged, &connectionScope, [&badLayersHandled] { badLayersHandled = true; } );

  // close the previous opened project if any
  closeProject();

  QFileInfo pfi( projectFile );
  mStatusBar->showMessage( tr( "Loading project: %1" ).arg( pfi.fileName() ) );
  qApp->processEvents();

  QApplication::setOverrideCursor( Qt::WaitCursor );

  bool autoSetupOnFirstLayer = mLayerTreeCanvasBridge->autoSetupOnFirstLayer();
  mLayerTreeCanvasBridge->setAutoSetupOnFirstLayer( false );

  // give custom handlers a chance first
  bool usedCustomHandler = false;
  bool customHandlerWantsThumbnail = false;
  QIcon customHandlerIcon;
  for ( QgsCustomProjectOpenHandler *handler : std::as_const( mCustomProjectOpenHandlers ) )
  {
    if ( handler && handler->handleProjectOpen( projectFile ) )
    {
      usedCustomHandler = true;
      customHandlerWantsThumbnail = handler->createDocumentThumbnailAfterOpen();
      customHandlerIcon = handler->icon();
      break;
    }
  }

  if ( !usedCustomHandler && !QgsProject::instance()->read( projectFile ) && !QgsZipUtils::isZipFile( projectFile ) )
  {
    QString backupFile = projectFile + "~";
    QString loadBackupPrompt;
    QMessageBox::StandardButtons buttons;
    if ( QFile( backupFile ).exists() )
    {
      loadBackupPrompt = "\n\n" + tr( "Do you want to open the backup file\n%1\ninstead?" ).arg( backupFile );
      buttons |= QMessageBox::Yes;
      buttons |= QMessageBox::No;
    }
    else
    {
      buttons |= QMessageBox::Ok;
    }
    QApplication::restoreOverrideCursor();
    mStatusBar->clearMessage();

    int r = QMessageBox::critical( this,
                                   tr( "Unable to open project" ),
                                   QgsProject::instance()->error() + loadBackupPrompt,
                                   buttons );

    if ( QMessageBox::Yes == r && addProject( backupFile ) )
    {
      // We loaded data from the backup file, but we pretend to work on the original project file.
      QgsProject::instance()->setFileName( projectFile );
      QgsProject::instance()->setDirty( true );
      mProjectLastModified = QgsProject::instance()->lastModified();
      returnCode = true;
    }
    else
    {
      returnCode = false;
    }
  }
  else
  {

    mProjectLastModified = QgsProject::instance()->lastModified();

    setTitleBarText_( *this );
    mOverviewCanvas->setBackgroundColor( QgsProject::instance()->backgroundColor() );

    applyProjectSettingsToCanvas( mMapCanvas );

    //load project scales
    bool projectScales = QgsProject::instance()->viewSettings()->useProjectScales();
    if ( projectScales )
    {
      mScaleWidget->updateScales();
    }

    mMapCanvas->updateScale();
    QgsDebugMsgLevel( QStringLiteral( "Scale restored..." ), 3 );

    mFilterLegendByMapContentAction->setChecked( QgsProject::instance()->readBoolEntry( QStringLiteral( "Legend" ), QStringLiteral( "filterByMap" ) ) );

    // Select the first layer
    if ( mLayerTreeView->layerTreeModel()->rootGroup()->findLayers().count() > 0 )
    {
      mLayerTreeView->setCurrentLayer( mLayerTreeView->layerTreeModel()->rootGroup()->findLayers().at( 0 )->layer() );
    }

    QgsSettings settings;

#ifdef WITH_BINDINGS
    // does the project have any macros?
    if ( mPythonUtils && mPythonUtils->isEnabled() )
    {
      if ( !QgsProject::instance()->readEntry( QStringLiteral( "Macros" ), QStringLiteral( "/pythonCode" ), QString() ).isEmpty() )
      {
        auto lambda = []() {QgisApp::instance()->enableProjectMacros();};
        QgsGui::pythonMacroAllowed( lambda, mInfoBar );
      }
    }
#endif

    // Check for missing layer widget dependencies
    const auto constVLayers { QgsProject::instance()->layers<QgsVectorLayer *>( ) };
    for ( QgsVectorLayer *vl : constVLayers )
    {
      if ( vl->isValid() )
      {
        resolveVectorLayerDependencies( vl );
      }
    }

    emit projectRead(); // let plug-ins know that we've read in a new
    // project so that they can check any project
    // specific plug-in state

    // add this to the list of recently used project files
    // if a custom handler was used, then we generate a thumbnail
    if ( !usedCustomHandler || !customHandlerWantsThumbnail )
      saveRecentProjectPath( false );
    else if ( !QgsProject::instance()->originalPath().isEmpty() )
    {
      // we have to delay the thumbnail creation until after the canvas has refreshed for the first time
      QMetaObject::Connection *connection = new QMetaObject::Connection();
      *connection = connect( mMapCanvas, &QgsMapCanvas::mapCanvasRefreshed, [ = ]()
      {
        QObject::disconnect( *connection );
        delete connection;
        saveRecentProjectPath( true, customHandlerIcon );
      } );
    }

    QApplication::restoreOverrideCursor();

    if ( autoSetupOnFirstLayer )
      mLayerTreeCanvasBridge->setAutoSetupOnFirstLayer( true );

    mStatusBar->showMessage( tr( "Project loaded" ), 3000 );
    returnCode = true;
  }

  if ( badLayersHandled )
  {
    dirtyBlocker.reset(); // allow project dirtying again
    QgsProject::instance()->setDirty( true );
  }

  return returnCode;
} // QgisApp::addProject(QString projectFile)


void QgisApp::addMapLayer( QgsMapLayer *mapLayer )
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


QgsMapCanvas *QgisApp::createNewMapCanvas( const QString &name )
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


bool QgisApp::saveDirty()
{
  QString whyDirty;
  bool hasUnsavedEdits = false;
  // extra check to see if there are any vector layers with unsaved provider edits
  // to ensure user has opportunity to save any editing
  if ( QgsProject::instance()->count() > 0 )
  {
    QMap<QString, QgsMapLayer *> layers = QgsProject::instance()->mapLayers();
    for ( QMap<QString, QgsMapLayer *>::iterator it = layers.begin(); it != layers.end(); ++it )
    {
      QgsVectorLayer *vl = qobject_cast<QgsVectorLayer *>( it.value() );
      // note that we skip the unsaved edits check for memory layers -- it's misleading, because their contents aren't actually
      // saved if this is part of a project close operation. Instead we let these get picked up by checkMemoryLayers().
      if ( !vl || vl->providerType() == QLatin1String( "memory" ) )
      {
        continue;
      }

      hasUnsavedEdits = ( vl->isEditable() && vl->isModified() );
      if ( hasUnsavedEdits )
      {
        break;
      }
    }

    if ( hasUnsavedEdits )
    {
      markDirty();
      whyDirty = QStringLiteral( "<p style='color:darkred;'>" );
      whyDirty += tr( "Project has layer(s) in edit mode with unsaved edits, which will NOT be saved!" );
      whyDirty += QLatin1String( "</p>" );
    }
  }

  QMessageBox::StandardButton answer( QMessageBox::Discard );
  QgsCanvasRefreshBlocker refreshBlocker;

  QgsSettings settings;
  bool askThem = settings.value( QStringLiteral( "qgis/askToSaveProjectChanges" ), true ).toBool();

  if ( askThem && QgsProject::instance()->isDirty() )
  {
    // flag project as dirty since dirty state of canvas is reset if "dirty"
    // is based on a zoom or pan
    markDirty();

    // prompt user to save
    answer = QMessageBox::question( this, tr( "Save Project" ),
                                    tr( "Do you want to save the current project? %1" )
                                    .arg( whyDirty ),
                                    QMessageBox::Save | QMessageBox::Cancel | QMessageBox::Discard,
                                    hasUnsavedEdits ? QMessageBox::Cancel : QMessageBox::Save );
    if ( QMessageBox::Save == answer )
    {
      if ( !fileSave() )
        answer = QMessageBox::Cancel;
    }
  }

  if ( answer == QMessageBox::Cancel )
    return false;

  // for memory layers, we discard all unsaved changes manually. Users have already been warned about
  // these by an earlier call to checkMemoryLayers(), and we don't want duplicate "unsaved changes" prompts
  // and anyway, saving the changes to a memory layer here won't actually save ANYTHING!
  // we do this at the very end here, because if the user opted to cancel above then ALL unsaved
  // changes in memory layers should still exist for them.
  const QMap<QString, QgsMapLayer *> layers = QgsProject::instance()->mapLayers();
  for ( auto it = layers.begin(); it != layers.end(); ++it )
  {
    if ( QgsVectorLayer *vl = qobject_cast<QgsVectorLayer *>( it.value() ) )
    {
      if ( vl->providerType() == QLatin1String( "memory" ) && vl->isEditable() && vl->isModified() )
      {
        vl->rollBack();
      }
    }
  }

  return true;
}


bool QgisApp::checkTasksDependOnProject()
{
  QSet< QString > activeTaskDescriptions;
  QMap<QString, QgsMapLayer *> layers = QgsProject::instance()->mapLayers();
  QMap<QString, QgsMapLayer *>::const_iterator layerIt = layers.constBegin();

  for ( ; layerIt != layers.constEnd(); ++layerIt )
  {
    QList< QgsTask * > tasks = QgsApplication::taskManager()->tasksDependentOnLayer( layerIt.value() );
    if ( !tasks.isEmpty() )
    {
      const auto constTasks = tasks;
      for ( QgsTask *task : constTasks )
      {
        activeTaskDescriptions.insert( tr( " • %1" ).arg( task->description() ) );
      }
    }
  }

  if ( !activeTaskDescriptions.isEmpty() )
  {
    QMessageBox::warning( this, tr( "Active Tasks" ),
                          tr( "The following tasks are currently running which depend on layers in this project:\n\n%1\n\nPlease cancel these tasks and retry." ).arg( qgis::setToList( activeTaskDescriptions ).join( QLatin1Char( '\n' ) ) ) );
    return true;
  }
  return false;
}


QString QgisApp::crsAndFormatAdjustedLayerUri( const QString &uri, const QStringList &supportedCrs, const QStringList &supportedFormats ) const
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


void QgisApp::openProject( const QString &fileName  )
{

}


//QgsOptions *QgisApp::createOptionsDialog( QWidget *parent )
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


//void QgisApp::showOptionsDialog( QWidget *parent, const QString &currentPage, int pageNumber )
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


QgsMapCanvasDockWidget *QgisApp::createNewMapCanvasDock( const QString &name )
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
    connect( mapCanvas, &QgsMapCanvas::messageEmitted, this, &QgisApp::displayMessage );
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
    connect( mapCanvasWidget, &QgsMapCanvasDockWidget::closed, this, &QgisApp::markDirty );
    //connect( mapCanvasWidget, &QgsMapCanvasDockWidget::renameTriggered, this, &QgisApp::renameView );

    return mapCanvasWidget;
}


void QgisApp::markDirty()
{
    // notify the project that there was a change
    QgsProject::instance()->setDirty( true );
}


void QgisApp::freezeCanvases( bool frozen )
{
    const auto canvases = mapCanvases();
    for ( QgsMapCanvas *canvas : canvases )
    {
        canvas->freeze( frozen );
    }
}


QgsBrowserGuiModel* QgisApp::browserModel()
{
    return mBrowserModel;
}


void QgisApp::setupDockWidget( QDockWidget *dockWidget, bool isFloating, QRect dockGeometry, Qt::DockWidgetArea area )
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


QgisApp::~QgisApp()
{
    delete mpZoomInTool;
    delete mpZoomOutTool;
    delete mpPanTool;
    delete mpMapToolBar;
    delete mMapCanvas;
    delete mpLayout;
    delete mDataSourceManagerDialog;

}


void QgisApp::addDockWidget( Qt::DockWidgetArea area, QDockWidget *thepDockWidget )
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


void QgisApp::applyProjectSettingsToCanvas( QgsMapCanvas *canvas )
{
    canvas->setCanvasColor( QgsProject::instance()->backgroundColor() );
    canvas->setSelectionColor( QgsProject::instance()->selectionColor() );
}


void QgisApp::applyDefaultSettingsToCanvas( QgsMapCanvas *canvas )
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


void QgisApp::namSetup()
{
    QgsNetworkAccessManager *nam = QgsNetworkAccessManager::instance();

    connect( nam, &QNetworkAccessManager::proxyAuthenticationRequired,
             this, &QgisApp::namProxyAuthenticationRequired );

    connect( nam, qOverload< QgsNetworkRequestParameters >( &QgsNetworkAccessManager::requestTimedOut ),
             this, &QgisApp::namRequestTimedOut );

    nam->setAuthHandler( std::make_unique<QgsAppAuthRequestHandler>() );
#ifndef QT_NO_SSL
    nam->setSslErrorHandler( std::make_unique<QgsAppSslErrorHandler>() );
#endif
}


void QgisApp::masterPasswordSetup()
{
    connect( QgsApplication::authManager(), &QgsAuthManager::messageOut,
             this, &QgisApp::authMessageOut );
    connect( QgsApplication::authManager(), &QgsAuthManager::passwordHelperMessageOut,
             this, &QgisApp::authMessageOut );
    connect( QgsApplication::authManager(), &QgsAuthManager::authDatabaseEraseRequested,
             this, &QgisApp::eraseAuthenticationDatabase );
}


void QgisApp::namRequestTimedOut( const QgsNetworkRequestParameters &request )
{
    QLabel *msgLabel = new QLabel( tr( "Network request to %1 timed out, any data received is likely incomplete." ).arg( request.request().url().host() ) +
                                   tr( " Please check the <a href=\"#messageLog\">message log</a> for further info." ), messageBar() );
    msgLabel->setWordWrap( true );
    connect( msgLabel, &QLabel::linkActivated, mLogDock, &QWidget::show );
    messageBar()->pushItem( new QgsMessageBarItem( msgLabel, Qgis::MessageLevel::Warning, QgsMessageBar::defaultMessageTimeout() ) );
}


void QgisApp::namProxyAuthenticationRequired( const QNetworkProxy &proxy, QAuthenticator *auth )
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


void QgisApp::startProfile( const QString &name )
{
    QgsApplication::profiler()->start( name );
}


void QgisApp::displayMessage( const QString &title, const QString &message, Qgis::MessageLevel level )
{
    qDebug()<<title  + message;
}


void QgisApp::endProfile()
{
    QgsApplication::profiler()->end();
}


bool QgisApp::toggleEditing( QgsMapLayer *layer, bool allowCancel )
{
    switch ( layer->type() )
    {
    case QgsMapLayerType::VectorLayer:
        return toggleEditingVectorLayer( qobject_cast<QgsVectorLayer *>( layer ), allowCancel );
    case QgsMapLayerType::MeshLayer:
        return toggleEditingMeshLayer( qobject_cast<QgsMeshLayer *>( layer ), allowCancel );
    case QgsMapLayerType::RasterLayer:
    case QgsMapLayerType::PluginLayer:
    case QgsMapLayerType::VectorTileLayer:
    case QgsMapLayerType::AnnotationLayer:
    case QgsMapLayerType::PointCloudLayer:
        break;
    }
    return false;
}


bool QgisApp::toggleEditingVectorLayer( QgsVectorLayer *vlayer, bool allowCancel )
{
    if ( !vlayer )
    {
        return false;
    }

    bool res = true;

    QString connString = QgsTransaction::connectionString( vlayer->source() );
    QString key = vlayer->providerType();

    QMap< QPair< QString, QString>, QgsTransactionGroup *> transactionGroups = QgsProject::instance()->transactionGroups();
    QMap< QPair< QString, QString>, QgsTransactionGroup *>::iterator tIt = transactionGroups .find( qMakePair( key, connString ) );
    QgsTransactionGroup *tg = ( tIt != transactionGroups.end() ? tIt.value() : nullptr );

    bool isModified = false;

    // Assume changes if: a) the layer reports modifications or b) its transaction group was modified
    QString modifiedLayerNames;
    bool hasSeveralModifiedLayers = false;
    if ( tg && tg->layers().contains( vlayer ) && tg->modified() )
    {
        isModified = true;
        std::vector<QString> vectModifiedLayerNames;
        if ( vlayer->isModified() )
        {
            vectModifiedLayerNames.push_back( vlayer->name() );
        }
        for ( QgsVectorLayer *iterLayer : tg->layers() )
        {
            if ( iterLayer != vlayer && iterLayer->isModified() )
            {
                vectModifiedLayerNames.push_back( iterLayer->name() );
            }
        }
        if ( vectModifiedLayerNames.size() == 1 )
        {
            modifiedLayerNames = vectModifiedLayerNames[0];
        }
        else if ( vectModifiedLayerNames.size() == 2 )
        {
            modifiedLayerNames = tr( "%1 and %2" ).arg( vectModifiedLayerNames[0] ).arg( vectModifiedLayerNames[1] );
        }
        else if ( vectModifiedLayerNames.size() > 2 )
        {
            modifiedLayerNames = tr( "%1, %2, …" ).arg( vectModifiedLayerNames[0] ).arg( vectModifiedLayerNames[1] );
        }
        hasSeveralModifiedLayers = vectModifiedLayerNames.size() > 1;
    }
    else if ( vlayer->isModified() )
    {
        isModified  = true;
        modifiedLayerNames = vlayer->name();
    }

    if ( !vlayer->isEditable() && !vlayer->readOnly() )
    {
        if ( !vlayer->supportsEditing() )
        {
            mActionToggleEditing->setChecked( false );
            mActionToggleEditing->setEnabled( false );
            visibleMessageBar()->pushMessage( tr( "Start editing failed" ),
                                              tr( "Provider cannot be opened for editing" ),
                                              Qgis::MessageLevel::Warning );
            return false;
        }

        vlayer->startEditing();

        QString markerType = QgsSettingsRegistryCore::settingsDigitizingMarkerStyle.value();
        bool markSelectedOnly = QgsSettingsRegistryCore::settingsDigitizingMarkerOnlyForSelected.value();

        // redraw only if markers will be drawn
        if ( ( !markSelectedOnly || vlayer->selectedFeatureCount() > 0 ) &&
             ( markerType == QLatin1String( "Cross" ) || markerType == QLatin1String( "SemiTransparentCircle" ) ) )
        {
            vlayer->triggerRepaint();
        }
    }
    else if ( isModified )
    {
        QMessageBox::StandardButtons buttons = QMessageBox::Save | QMessageBox::Discard;
        if ( allowCancel )
            buttons |= QMessageBox::Cancel;

        switch ( QMessageBox::question( nullptr,
                                        tr( "Stop Editing" ),
                                        hasSeveralModifiedLayers ?
                                        tr( "Do you want to save the changes to layers %1?" ).arg( modifiedLayerNames ) :
                                        tr( "Do you want to save the changes to layer %1?" ).arg( modifiedLayerNames ),
                                        buttons ) )
        {
        case QMessageBox::Cancel:
            res = false;
            break;

        case QMessageBox::Save:
            QApplication::setOverrideCursor( Qt::WaitCursor );

            if ( !vlayer->commitChanges() )
            {
                commitError( vlayer );
                // Leave the in-memory editing state alone,
                // to give the user a chance to enter different values
                // and try the commit again later
                res = false;
            }

            vlayer->triggerRepaint();

            QApplication::restoreOverrideCursor();
            break;

        case QMessageBox::Discard:
        {
            QApplication::setOverrideCursor( Qt::WaitCursor );

            QgsCanvasRefreshBlocker refreshBlocker;
            if ( !vlayer->rollBack() )
            {
                visibleMessageBar()->pushMessage( tr( "Error" ),
                                                  tr( "Problems during roll back" ),
                                                  Qgis::MessageLevel::Critical );
                res = false;
            }

            vlayer->triggerRepaint();

            QApplication::restoreOverrideCursor();
            break;
        }

        default:
            break;
        }
    }
    else //layer not modified
    {
        QgsCanvasRefreshBlocker refreshBlocker;
        vlayer->rollBack();
        res = true;
        vlayer->triggerRepaint();
    }

    if ( !res && vlayer == activeLayer() )
    {
        // while also called when layer sends editingStarted/editingStopped signals,
        // this ensures correct restoring of gui state if toggling was canceled
        // or layer commit/rollback functions failed
        //    activateDeactivateLayerRelatedActions( vlayer );
    }

    return res;
}


bool QgisApp::toggleEditingMeshLayer( QgsMeshLayer *mlayer, bool allowCancel )
{
    if ( !mlayer )
        return false;

    if ( !mlayer->supportsEditing() )
        return false; //TODO: when adapted widget will be ready, ask the user if he want to create a new one based on this one

    bool res = false;

    QgsCoordinateTransform transform( mlayer->crs(), mMapCanvas->mapSettings().destinationCrs(), QgsProject::instance() );

    if ( !mlayer->isEditable() )
    {
        res = mlayer->startFrameEditing( transform );
        mActionToggleEditing->setChecked( res );

        if ( !res )
            QgsMessageLog::logMessage( tr( "Unable to start mesh editing for layer \"%1\"" ).arg( mlayer->name() ) );
    }
    else if ( mlayer->isModified() )
    {
        QMessageBox::StandardButtons buttons = QMessageBox::Save | QMessageBox::Discard;
        if ( allowCancel )
            buttons = buttons | QMessageBox::Cancel;
        switch ( QMessageBox::question( nullptr,
                                        tr( "Stop Editing" ),
                                        tr( "Do you want to save the changes to layer %1?" ).arg( mlayer->name() ),
                                        buttons ) )
        {
        case QMessageBox::Cancel:
            res = false;
            break;

        case QMessageBox::Save:
        {
            QgsTemporaryCursorOverride waitCursor( Qt::WaitCursor );
            QgsCanvasRefreshBlocker refreshBlocker;
            if ( !mlayer->commitFrameEditing( transform, false ) )
            {
                res = false;
            }

            mlayer->triggerRepaint();
        }
            break;
        case QMessageBox::Discard:
        {
            QgsTemporaryCursorOverride waitCursor( Qt::WaitCursor );
            QgsCanvasRefreshBlocker refreshBlocker;
            if ( !mlayer->rollBackFrameEditing( transform, false ) )
            {
                visibleMessageBar()->pushMessage( tr( "Error" ),
                                                  tr( "Problems during roll back" ),
                                                  Qgis::MessageLevel::Critical );
                res = false;
            }

            mlayer->triggerRepaint();
            break;
        }

        default:
            break;
        }
    }
    else //mesh layer not modified
    {
        QgsTemporaryCursorOverride waitCursor( Qt::WaitCursor );
        QgsCanvasRefreshBlocker refreshBlocker;
        mlayer->rollBackFrameEditing( transform, false );
        mlayer->triggerRepaint();
    }

    if ( !res && mlayer == activeLayer() )
    {
        // while also called when layer sends editingStarted/editingStopped signals,
        // this ensures correct restoring of gui state if toggling was canceled
        // or layer commit/rollback functions failed
        //    activateDeactivateLayerRelatedActions( mlayer );
    }

    return res;
}


void QgisApp::deleteSelected( QgsMapLayer *layer, QWidget *parent, bool checkFeaturesVisible )
{
    if ( !layer )
    {
        layer = mLayerTreeView->currentLayer();
    }

    if ( !parent )
    {
        parent = this;
    }

    if ( !layer )
    {
        visibleMessageBar()->pushMessage( tr( "No Layer Selected" ),
                                          tr( "To delete features, you must select a vector layer in the legend" ),
                                          Qgis::MessageLevel::Info );
        return;
    }

    QgsVectorLayer *vlayer = qobject_cast<QgsVectorLayer *>( layer );
    if ( !vlayer )
    {
        visibleMessageBar()->pushMessage( tr( "No Vector Layer Selected" ),
                                          tr( "Deleting features only works on vector layers" ),
                                          Qgis::MessageLevel::Info );
        return;
    }

    if ( !( vlayer->dataProvider()->capabilities() & QgsVectorDataProvider::DeleteFeatures ) )
    {
        visibleMessageBar()->pushMessage( tr( "Provider does not support deletion" ),
                                          tr( "Data provider does not support deleting features" ),
                                          Qgis::MessageLevel::Info );
        return;
    }

    if ( !vlayer->isEditable() )
    {
        visibleMessageBar()->pushMessage( tr( "Layer not editable" ),
                                          tr( "The current layer is not editable. Choose 'Start editing' in the digitizing toolbar." ),
                                          Qgis::MessageLevel::Info );
        return;
    }

    //validate selection
    const int numberOfSelectedFeatures = vlayer->selectedFeatureCount();
    if ( numberOfSelectedFeatures == 0 )
    {
        visibleMessageBar()->pushMessage( tr( "No Features Selected" ),
                                          tr( "The current layer has no selected features" ),
                                          Qgis::MessageLevel::Info );
        return;
    }
    //display a warning
    if ( checkFeaturesVisible )
    {
        QgsFeature feat;
        QgsFeatureIterator it = vlayer->getSelectedFeatures( QgsFeatureRequest().setNoAttributes() );
        bool allFeaturesInView = true;
        QgsRectangle viewRect = mMapCanvas->mapSettings().mapToLayerCoordinates( vlayer, mMapCanvas->extent() );

        while ( it.nextFeature( feat ) )
        {
            if ( allFeaturesInView && !viewRect.intersects( feat.geometry().boundingBox() ) )
            {
                allFeaturesInView = false;
                break;
            }
        }

        if ( !allFeaturesInView )
        {
            // for extra safety to make sure we are not removing geometries by accident
            int res = QMessageBox::warning( mMapCanvas, tr( "Delete %n feature(s) from layer \"%1\"", nullptr, numberOfSelectedFeatures ).arg( vlayer->name() ),
                                            tr( "Some of the selected features are outside of the current map view. Would you still like to continue?" ),
                                            QMessageBox::Yes | QMessageBox::No );
            if ( res != QMessageBox::Yes )
                return;
        }
    }

    QgsVectorLayerUtils::QgsDuplicateFeatureContext infoContext;
    if ( QgsVectorLayerUtils::impactsCascadeFeatures( vlayer, vlayer->selectedFeatureIds(), QgsProject::instance(), infoContext, QgsVectorLayerUtils::IgnoreAuxiliaryLayers ) )
    {
        QString childrenInfo;
        int childrenCount = 0;
        const auto infoContextLayers = infoContext.layers();
        for ( QgsVectorLayer *chl : infoContextLayers )
        {
            childrenCount += infoContext.duplicatedFeatures( chl ).size();
            childrenInfo += ( tr( "%1 feature(s) on layer \"%2\", " ).arg( infoContext.duplicatedFeatures( chl ).size() ).arg( chl->name() ) );
        }

        // for extra safety to make sure we know that the delete can have impact on children and joins
        int res = QMessageBox::question( mMapCanvas, tr( "Delete at least %1 feature(s) on other layer(s)" ).arg( childrenCount ),
                                         tr( "Delete %1 feature(s) on layer \"%2\", %3 as well\nand all of its other descendants.\nDelete these features?" ).arg( numberOfSelectedFeatures ).arg( vlayer->name() ).arg( childrenInfo ),
                                         QMessageBox::Yes | QMessageBox::No );
        if ( res != QMessageBox::Yes )
            return;
    }

    vlayer->beginEditCommand( tr( "Features deleted" ) );
    int deletedCount = 0;
    QgsVectorLayer::DeleteContext context( true, QgsProject::instance() );
    if ( !vlayer->deleteSelectedFeatures( &deletedCount, &context ) )
    {
        visibleMessageBar()->pushMessage( tr( "Problem deleting features" ),
                                          tr( "A problem occurred during deletion from layer \"%1\". %n feature(s) not deleted.", nullptr, numberOfSelectedFeatures - deletedCount ).arg( vlayer->name() ),
                                          Qgis::MessageLevel::Warning );
    }
    else
    {
        const QList<QgsVectorLayer *> contextLayers = context.handledLayers( false );
        // if it affects more than one non-auxiliary layer, print feedback for all descendants
        if ( contextLayers.size() > 1 )
        {
            deletedCount = 0;
            QString feedbackMessage;
            for ( QgsVectorLayer *contextLayer : contextLayers )
            {
                feedbackMessage += tr( "%1 on layer %2. " ).arg( context.handledFeatures( contextLayer ).size() ).arg( contextLayer->name() );
                deletedCount += context.handledFeatures( contextLayer ).size();
            }
            visibleMessageBar()->pushMessage( tr( "%1 features deleted: %2" ).arg( deletedCount ).arg( feedbackMessage ), Qgis::MessageLevel::Success );
        }

        showStatusMessage( tr( "%n feature(s) deleted.", "number of features deleted", deletedCount ) );
    }

    vlayer->endEditCommand();
}


void QgisApp::toggleEditing()
{
    const QList<QgsMapLayer *> layerList = layerTreeView()->selectedLayers();
    if ( !layerList.isEmpty() )
    {
        // if there are selected layers, try to toggle those.
        // mActionToggleEditing has already been triggered at this point so its checked status has changed
        const bool shouldStartEditing = mActionToggleEditing->isChecked();
        for ( const auto layer : layerList )
        {
            if ( layer->supportsEditing() &&
                 shouldStartEditing != layer->isEditable() )
            {
                toggleEditing( layer, true );
            }
        }
    }
    else
    {
        // if there are no selected layers, try to toggle the current layer
        QgsMapLayer *currentLayer =  activeLayer();
        if ( currentLayer && currentLayer->supportsEditing() )
        {
            toggleEditing( currentLayer, true );
        }
        else
        {
            // active although there's no layer active!?
            mActionToggleEditing->setChecked( false );
            mActionToggleEditing->setEnabled( false );
            visibleMessageBar()->pushMessage( tr( "Start editing failed" ),
                                              tr( "Layer cannot be edited" ),
                                              Qgis::MessageLevel::Warning );
        }
    }
}


QgsLayerTreeView *QgisApp::layerTreeView()
{
    return mLayerTreeView;
}


void QgisApp::panMode()
{
    mMapCanvas->setMapTool(mpPanTool);

}


void QgisApp::zoomInMode()
{
    mMapCanvas->setMapTool(mpZoomInTool);
}


void QgisApp::zoomOutMode()
{
    mMapCanvas->setMapTool(mpZoomOutTool);
}


bool QgisApp::addVectorLayers( const QStringList &layerQStringList, const QString &enc, const QString &dataSourceType )
{
    qDebug()<<"In add vector layers";
    return addVectorLayersPrivate( layerQStringList, enc, dataSourceType );
}


QgsVectorLayer *QgisApp::addVectorLayer( const QString &vectorLayerPath, const QString &name, const QString &providerKey )
{
    qDebug()<<"In add vector layer";
    return addLayerPrivate< QgsVectorLayer >( QgsMapLayerType::VectorLayer, vectorLayerPath, name, providerKey, true );
}


QgsMapCanvas *QgisApp::mapCanvas()
{
    Q_ASSERT( mMapCanvas );
    return mMapCanvas;
}


QList<QgsMapCanvas *> QgisApp::mapCanvases()
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


void QgisApp::refreshMapCanvas( bool redrawAllLayers )
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


void QgisApp::authMessageOut( const QString &message, const QString &authtag, QgsAuthManager::MessageLevel level )
{
    // Use system notifications if the main window is not the active one,
    // push message to the message bar if the main window is active

    qDebug()<< tr( "QGIS Authentication" ) + authtag + message;

}


void QgisApp::eraseAuthenticationDatabase()
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


bool QgisApp::addVectorLayersPrivate( const QStringList &layers, const QString &enc, const QString &dataSourceType, const bool guiWarning )
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


void QgisApp::addLayer()
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


QgsVectorTileLayer *QgisApp::addVectorTileLayer( const QString &url, const QString &baseName )
{
    return addVectorTileLayerPrivate( url, baseName );
}


QgsVectorTileLayer *QgisApp::addVectorTileLayerPrivate( const QString &url, const QString &baseName, const bool guiWarning )
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


QgsMessageBar *QgisApp::messageBar()
{
    // Q_ASSERT( mInfoBar );
    return mInfoBar;
}


QgsRasterLayer *QgisApp::addRasterLayer( QString const &uri, QString const &baseName, QString const &providerKey )
{
    qDebug()<<"yes";

    auto rasterLyr = addLayerPrivate< QgsRasterLayer >( QgsMapLayerType::RasterLayer, uri, baseName, providerKey, true );

    if(rasterLyr == nullptr)
    {
        qDebug()<<"Failed to create raster";

        return nullptr;
    }

    QList<QgsMapLayer *> rasterLst{rasterLyr};
    mMapCanvas->setLayers(rasterLst);

    refreshMapCanvas(true);

    mMapCanvas->setExtent(rasterLyr->extent());


    this->addMapLayer(rasterLyr);




    return rasterLyr;

//    qDebug()<<"yes";
//    auto rasterLyr = addLayerPrivate< QgsRasterLayer >( QgsMapLayerType::RasterLayer, uri, baseName, providerKey, true );

//    auto layers = mMapCanvas->layers();
//    layers.append(rasterLyr);
//    mMapCanvas->setLayers(layers);
//    mMapCanvas->setExtent(rasterLyr->extent());

//    refreshMapCanvas(true);

//    this->addMapLayer(rasterLyr);
}


QgsAbstractDataSourceWidget* QgisApp::createDataSourceWidget( QWidget *parent, Qt::WindowFlags fl, QgsProviderRegistry::WidgetMode widgetMode) const
{
    auto xyzSourceSelect = new QgsXyzSourceSelect( parent, fl, widgetMode );

    connect(xyzSourceSelect,&QgsXyzSourceSelect::addRasterLayer,this,&QgisApp::addRasterLayer);

    return xyzSourceSelect;
}


template<typename T>
T* QgisApp::addLayerPrivate( QgsMapLayerType type, const QString &uri, const QString &name, const QString &providerKey, bool guiWarnings )
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

//    QList<QgsMapLayer *> rasterLst{result};
//    mMapCanvas->setLayers(rasterLst);

//    refreshMapCanvas(true);

//    mMapCanvas->setExtent(result->extent());


    //  activateDeactivateLayerRelatedActions(activeLayer());
    return result;
}


QList< QgsMapLayer * > QgisApp::addSublayers(const QList<QgsProviderSublayerDetails> &layers, const QString &baseName, const QString &groupName)
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


void QgisApp::dataSourceManager( const QString &pageName )
{
    if (! mDataSourceManagerDialog )
    {
        mDataSourceManagerDialog = new QgsDataSourceManagerDialog( mBrowserModel, this, mMapCanvas);
        //    connect( this, &QgisApp::connectionsChanged, mDataSourceManagerDialog, &QgsDataSourceManagerDialog::refresh );
        //    connect( mDataSourceManagerDialog, &QgsDataSourceManagerDialog::connectionsChanged, this, &QgisApp::connectionsChanged );
        connect( mDataSourceManagerDialog, SIGNAL( addRasterLayer( QString const &, QString const &, QString const & ) ),
                 this, SLOT(addRasterLayer( QString const &, QString const &, QString const & ) ) );
        connect( mDataSourceManagerDialog, &QgsDataSourceManagerDialog::addRasterLayers, this, [ = ]( const QStringList & layersList ) { addRasterLayers( layersList ); } );
        connect( mDataSourceManagerDialog, SIGNAL( addVectorLayer( QString const &, QString const &, QString const & ) ),
                 this, SLOT(addVectorLayer( QString const &, QString const &, QString const & ) ) );
        connect( mDataSourceManagerDialog, SIGNAL( addVectorLayers( QStringList const &, QString const &, QString const & ) ),
                 this, SLOT(addVectorLayers( QStringList const &, QString const &, QString const & ) ) );
        connect( mDataSourceManagerDialog, &QgsDataSourceManagerDialog::addVectorTileLayer, this, &QgisApp::addVectorTileLayer );

        //        connect( mDataSourceManagerDialog, &QgsDataSourceManagerDialog::addMeshLayer, this, &QgisApp::addMeshLayer );
        //    connect( mDataSourceManagerDialog, &QgsDataSourceManagerDialog::addPointCloudLayer, this, &QgisApp::addPointCloudLayer );
        //    connect( mDataSourceManagerDialog, &QgsDataSourceManagerDialog::showStatusMessage, this, &QgisApp::showStatusMessage );
        //    connect( mDataSourceManagerDialog, &QgsDataSourceManagerDialog::addDatabaseLayers, this, &QgisApp::addDatabaseLayers );
        //    connect( mDataSourceManagerDialog, &QgsDataSourceManagerDialog::replaceSelectedVectorLayer, this, &QgisApp::replaceSelectedVectorLayer );
        //    connect( mDataSourceManagerDialog, &QgsDataSourceManagerDialog::handleDropUriList, this, &QgisApp::handleDropUriList );
        //    connect( this, &QgisApp::newProject, mDataSourceManagerDialog, &QgsDataSourceManagerDialog::updateProjectHome );
        //    connect( mDataSourceManagerDialog, &QgsDataSourceManagerDialog::openFile, this, &QgisApp::openFile );

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


bool QgisApp::askUserForDatumTransform( const QgsCoordinateReferenceSystem &sourceCrs, const QgsCoordinateReferenceSystem &destinationCrs, const QgsMapLayer *layer )
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


bool QgisApp::askUserForZipItemLayers(const QString &path, const QList< QgsMapLayerType > &acceptableTypes)
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


QgsMapLayer *QgisApp::activeLayer()
{
    return mLayerTreeView ? mLayerTreeView->currentLayer() : nullptr;
}


bool QgisApp::addRasterLayers(QStringList const &files, bool guiWarning)
{
    qDebug()<<"In add raster layers";

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


bool QgisApp::setActiveLayer( QgsMapLayer *layer )
{
    if ( !layer )
        return false;

    if ( !mLayerTreeView->layerTreeModel()->rootGroup()->findLayer( layer->id() ) )
        return false;

    mLayerTreeView->setCurrentLayer( layer );
    return true;
}


QgisApp::SublayerHandling QgisApp::shouldAskUserForSublayers( const QList<QgsProviderSublayerDetails> &layers, bool hasNonLayerItems ) const
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


void QgisApp::postProcessAddedLayer(QgsMapLayer *layer)
{

    switch (layer->type())
    {
    case QgsMapLayerType::VectorLayer:
    case QgsMapLayerType::RasterLayer:
    {
        bool ok = false;
        layer->loadDefaultStyle( ok );
        if ( !ok )
            qDebug()<< "Error loading style";
        layer->loadDefaultMetadata( ok );
        if ( !ok )
            qDebug()<< tr( "Error loading layer metadata" );
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


void QgisApp::showStatusMessage( const QString &message )
{
    qDebug()<<message;
}
