#ifndef QGISVISUALIZATIONWIDGET_H
#define QGISVISUALIZATIONWIDGET_H


#include <QMainWindow>
#include <QNetworkProxy>

#include <qgsprovidersublayerdetails.h>
#include <qgsproviderregistry.h>
#include <qgsnetworkaccessmanager.h>
#include <qgscustomdrophandler.h>
#include <qgsauthmanager.h>
#include <qgsvectorlayer.h>
//#include "qgsoptionswidgetfactory.h"

class QSplitter;
class QToolBar;
class QgsMapCanvasDockWidget;

//Local Includes
class QgsPluginManager;
class QgsMapLayer;
class QgsVectorTileLayer;
class QgsAbstractDataSourceWidget;
class QgsMessageBar;
class QgsDataSourceManagerDialog;
class QgsBrowserGuiModel;
class QgsLayerTreeView;
class QgsMapCanvas;
class QgsRasterLayer;
class QgsMapTool;
class QgsNetworkLogger;
class QgsDockWidget;
class QgsMessageLogViewer;
class QgsLayerTreeMapCanvasBridge;
class QgisAppStyleSheet;
class QgsLocatorWidget;
//class QgsOptions;
class QgsStatusBarScaleWidget;
class QgsAppMapTools;
class QgsStatusBarMagnifierWidget;

class QGISVisualizationWidget : public QMainWindow
{
    Q_OBJECT

public:
    QGISVisualizationWidget(QWidget* parent = nullptr,  Qt::WindowFlags f = Qt::WindowFlags());
    ~QGISVisualizationWidget();

    /**
             * Adds a vector tile layer directly without prompting user for location
             * The caller must provide information needed for layer construction
             * using the \a url and \a baseName. The \a baseName parameter is used
             * in the Map Legend so it should be formed in a meaningful way.
             * \since QGIS 3.14
             */
    QgsVectorTileLayer* addVectorTileLayerPrivate( const QString &url, const QString &baseName, const bool guiWarning = true);

    void postProcessAddedLayer(QgsMapLayer *layer);

    QgsAbstractDataSourceWidget* createDataSourceWidget(QWidget *parent = nullptr, Qt::WindowFlags fl = Qt::Widget, QgsProviderRegistry::WidgetMode widgetMode = QgsProviderRegistry::WidgetMode::Embedded ) const;

    QList<QgsMapLayer*> addSublayers(const QList<QgsProviderSublayerDetails> &layers, const QString &baseName, const QString &groupName);

    bool askUserForDatumTransform(const QgsCoordinateReferenceSystem &sourceCrs, const QgsCoordinateReferenceSystem &destinationCrs, const QgsMapLayer *layer);

    //! Gets the mapcanvas object from the app
    QgsMapCanvas *mapCanvas();

    QgsVectorTileLayer* addVectorTileLayer(const QString &url, const QString &baseName);

    enum class SublayerHandling
    {
        AskUser,
        LoadAll,
        AbortLoading
    };

    void addDockWidget( Qt::DockWidgetArea area, QDockWidget *thepDockWidget );

    QgsMessageBar* messageBar();

    void namSetup();

    void freezeCanvases(bool frozen);

    QgsBrowserGuiModel* browserModel();

    void dataSourceManager(const QString &pageName = QString());

    /**
             * This method will open a dialog so the user can select GDAL sublayers to load
             * \returns TRUE if any items were loaded
             */
    bool askUserForZipItemLayers( const QString &path, const QList<QgsMapLayerType> &acceptableTypes );

    //! Returns the active map layer.
    QgsMapLayer *activeLayer();

    void refreshMapCanvas(bool redrawAllLayers = false);

    /**
      * Returns a list of all map canvases open in the app.
      */
    QList< QgsMapCanvas * > mapCanvases();

    static QGISVisualizationWidget *instance() { return sInstance; }

    QgsLayerTreeView *layerTreeView() const;

    //! Opens the options dialog
    void showOptionsDialog( QWidget *parent = nullptr, const QString &currentPage = QString(), int pageNumber = -1 );

    void addMapLayer( QgsMapLayer *mapLayer );

public slots:
    void zoomInMode();
    void zoomOutMode();
    void panMode();
    void addLayer();

    void displayMessage( const QString &title, const QString &message, Qgis::MessageLevel level );
    QgsRasterLayer* addRasterLayer(QString const &uri, QString const &baseName, QString const &providerKey);

    /**
             * \brief overloaded version of the private addLayer method that takes a list of
             * file names instead of prompting user with a dialog.
             * \param enc encoding type for the layer
             * \param dataSourceType type of ogr datasource
             * \returns TRUE if successfully added layer
             */
    bool addVectorLayers( const QStringList &layerQStringList, const QString &enc, const QString &dataSourceType );

    /**
             * Add a vector layer directly without prompting user for location
             * The caller must provide information compatible with the provider plugin
             * using the \a vectorLayerPath and \a baseName. The provider can use these
             * parameters in any way necessary to initialize the layer. The \a baseName
             * parameter is used in the Map Legend so it should be formed in a meaningful
             * way.
             */
    QgsVectorLayer* addVectorLayer(const QString &vectorLayerPath, const QString &name, const QString &providerKey);

    /**
             * Overloaded version of the private addRasterLayer()
             * Method that takes a list of file names instead of prompting
             * user with a dialog.
             * \returns TRUE if successfully added layer(s)
             */
    bool addRasterLayers( const QStringList &files, bool guiWarning = true );

    //! save current vector layer
    QString saveAsFile( QgsMapLayer *layer = nullptr, bool onlySelected = false, bool defaultToAddToMap = true );
    //! save current raster layer
    QString saveAsRasterFile( QgsRasterLayer *layer = nullptr, bool defaultAddToCanvas = true );

    //! Process the list of URIs that have been dropped in QGIS
    void handleDropUriList( const QgsMimeDataUtils::UriList &lst );

    void openProject(const QString &fileName  );

signals:

    void activeLayerChanged( QgsMapLayer *layer );

private slots:
    void namProxyAuthenticationRequired( const QNetworkProxy &proxy, QAuthenticator *auth );
    void namRequestTimedOut( const QgsNetworkRequestParameters &request );
    void markDirty();
    void authMessageOut( const QString &message, const QString &authtag, QgsAuthManager::MessageLevel level );
    void eraseAuthenticationDatabase(); //! Schedule and erase of the authentication database upon confirmation

private:

    QGISVisualizationWidget::SublayerHandling shouldAskUserForSublayers(const QList<QgsProviderSublayerDetails> &layers, bool hasNonLayerItems = false) const;
    template<typename T> T *addLayerPrivate(QgsMapLayerType type, const QString &uri, const QString &baseName, const QString &providerKey, bool guiWarnings = true);

    bool addVectorLayersPrivate( const QStringList &layers, const QString &enc, const QString &dataSourceType, bool guiWarning = true );

    void startProfile(const QString &name);
    void endProfile();

    QgsMapCanvasDockWidget* createNewMapCanvasDock( const QString &name );
    QgsMapCanvas * createNewMapCanvas( const QString &name );
    void setupDockWidget( QDockWidget *dockWidget, bool isFloating = false, QRect dockGeometry = QRect(),Qt::DockWidgetArea area = Qt::RightDockWidgetArea );
    void applyProjectSettingsToCanvas( QgsMapCanvas *canvas );
    void applyDefaultSettingsToCanvas( QgsMapCanvas *canvas );
    void masterPasswordSetup();

    QgsNetworkLogger *mNetworkLogger = nullptr;
    QgsMessageBar *mInfoBar = nullptr;
    QgsMapCanvas * mMapCanvas = nullptr;
    QSplitter  * mpLayout = nullptr;
    QToolBar * mpMapToolBar = nullptr;
    QgsMapTool * mpPanTool = nullptr;
    QgsMapTool * mpZoomInTool = nullptr;
    QgsMapTool * mpZoomOutTool = nullptr;
    QgsDataSourceManagerDialog* mDataSourceManagerDialog = nullptr;
    QgsBrowserGuiModel *mBrowserModel = nullptr;
    QgsLocatorWidget *mLocatorWidget = nullptr;

    // Helper class that connects layer tree with map canvas
    QgsLayerTreeMapCanvasBridge *mLayerTreeCanvasBridge = nullptr;

    //! zoom widget
    QgsStatusBarMagnifierWidget *mMagnifierWidget = nullptr;

    QVector<QPointer<QgsCustomDropHandler>> mCustomDropHandlers;

    // Table of contents (legend) for the map
    QgsLayerTreeView *mLayerTreeView = nullptr;

    static QGISVisualizationWidget *sInstance;
    QgsDockWidget *mLogDock = nullptr;

    QgsMessageLogViewer *mLogViewer = nullptr;

    QgisAppStyleSheet *mStyleSheetBuilder = nullptr;
    QgsPluginManager *mPluginManager = nullptr;

    QgsStatusBarScaleWidget *mScaleWidget = nullptr;

    // True if we are blocking the activeLayerChanged signal from being emitted
    bool mBlockActiveLayerChanged = false;

    /**
     * String containing supporting raster file formats
     * Suitable for a QFileDialog file filter.  Build in ctor.
     */
    QString mRasterFileFilter;

    QgsMessageBar* visibleMessageBar();

    QString crsAndFormatAdjustedLayerUri( const QString &uri, const QStringList &supportedCrs, const QStringList &supportedFormats ) const;

    void onActiveLayerChanged( QgsMapLayer *layer );

//    QgsOptions* createOptionsDialog( QWidget *parent );

//    QList<QPointer<QgsOptionsWidgetFactory>> mOptionsWidgetFactories;

    std::unique_ptr< QgsAppMapTools > mMapTools;

    class QgsCanvasRefreshBlocker
    {
    public:

        QgsCanvasRefreshBlocker()
        {
            if ( QGISVisualizationWidget::instance()->mFreezeCount++ == 0 )
            {
                // going from unfrozen to frozen, so freeze canvases
                QGISVisualizationWidget::instance()->freezeCanvases( true );
            }
        }
        QgsCanvasRefreshBlocker( const QgsCanvasRefreshBlocker &other ) = delete;
        QgsCanvasRefreshBlocker &operator=( const QgsCanvasRefreshBlocker &other ) = delete;

        void release()
        {
            if ( mReleased )
                return;

            mReleased = true;
            if ( --QGISVisualizationWidget::instance()->mFreezeCount == 0 )
            {
                // going from frozen to unfrozen, so unfreeze canvases
                QGISVisualizationWidget::instance()->freezeCanvases( false );
                QGISVisualizationWidget::instance()->refreshMapCanvas();
            }
        }

        ~QgsCanvasRefreshBlocker()
        {
            if ( !mReleased )
                release();
        }

    private:

        bool mReleased = false;
    };

    int mFreezeCount = 0;
    friend class QgsCanvasRefreshBlocker;

    friend class QgisAppInterface;
    friend class QgsAppScreenShots;

};

#endif // QGISVISUALIZATIONWIDGET_H
