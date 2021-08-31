#ifndef QgisApp_H
#define QgisApp_H


#include <QMainWindow>
#include <QNetworkProxy>
#include <QAction>
#include <QMenu>

#include <qgsprovidersublayerdetails.h>
#include <qgsproviderregistry.h>
#include <qgsnetworkaccessmanager.h>
#include <qgscustomdrophandler.h>
#include <qgsauthmanager.h>
#include <qgsvectorlayer.h>
#include <qgsgeometryengine.h>
#include <qgsfeaturerenderergenerator.h>
#include <qgsoptionswidgetfactory.h>
#include <qgsattributeeditorcontext.h>

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
class QgsStatusBar;
class QgsOptions;
class QgsStatusBarScaleWidget;
class QgsAppMapTools;
class QgsStatusBarMagnifierWidget;
class QgsAdvancedDigitizingDockWidget;
class QgsUserInputWidget;
class QgsClipboard;
class QgsMapLayerConfigWidgetFactory;
class QgsLayerStylingWidget;
class QgsHandleBadLayersHandler;
class QgsLegendFilterButton;

class QgisApp : public QMainWindow
{
    Q_OBJECT

public:
    QgisApp(QWidget* parent = nullptr,  Qt::WindowFlags f = Qt::WindowFlags());
    ~QgisApp();

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

    // Gets the mapcanvas object from the app
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

    /**
     * Add a dock widget to the given area and tabify it (if other dock widgets
     * exist in the same \a area). The new tab will be below other tabs unless
     * \a raiseTab is passed as TRUE.
     *
     * \a tabifyWith is a list of dock widget object names, ordered by
     * priority, with which the new dock widget should be tabified. Only the
     * first matching object name will be picked. If none of the given object
     * names is found in that \a area (or if \a tabifyWith is not given at
     * all), the new dock widget will be created anyways, but its location
     * within that \a area will be unpredictable.
     *
     * \since QGIS 3.14
     */
    void addTabifiedDockWidget( Qt::DockWidgetArea area, QDockWidget *dockWidget, const QStringList &tabifyWith = QStringList(), bool raiseTab = false );

    void dataSourceManager(const QString &pageName = QString());

    /**
             * This method will open a dialog so the user can select GDAL sublayers to load
             * \returns TRUE if any items were loaded
             */
    bool askUserForZipItemLayers( const QString &path, const QList<QgsMapLayerType> &acceptableTypes );

    /**
      * Returns the toolbar icon size. If \a dockedToolbar is TRUE, the icon size
      * for toolbars contained within docks is returned.
      */
    QSize iconSize( bool dockedToolbar = false ) const;

    //! Returns the active map layer.
    QgsMapLayer *activeLayer();

    void refreshMapCanvas(bool redrawAllLayers = false);

    /**
      * \param layerContainingSelection  The layer that the selection will be taken from
      *                                  (defaults to the active layer on the legend)
     */
    void cutSelectionToClipboard( QgsMapLayer *layerContainingSelection = nullptr );

    /**
      * Returns a list of all map canvases open in the app.
      */
    QList< QgsMapCanvas * > mapCanvases();

    static QgisApp *instance() { return sInstance; }

    QgsLayerTreeView *layerTreeView();


    /**
      * \param layerContainingSelection  The layer that the selection will be taken from
      *                                  (defaults to the active layer on the legend)
     */
    void copySelectionToClipboard( QgsMapLayer *layerContainingSelection = nullptr );

    /**
     * Save edits of a layer
     * \param leaveEditable leave the layer in editing mode when done
     * \param triggerRepaint send layer signal to repaint canvas when done
     */
    void saveEdits( QgsMapLayer *layer, bool leaveEditable = true, bool triggerRepaint = true );

    //! Save current edits for selected layer(s) and start new transaction(s)
    void saveEdits();

    // Opens the options dialog
    void showOptionsDialog( QWidget *parent = nullptr, const QString &currentPage = QString(), int pageNumber = -1 );

    void addMapLayer( QgsMapLayer *mapLayer );

    QgsStatusBar *statusBarIface() { return mStatusBar; }

    // Returns the CAD dock widget
    QgsAdvancedDigitizingDockWidget *cadDockWidget() { return mAdvancedDigitizingDockWidget; }

    void addUserInputWidget( QWidget *widget );

    // starts/stops editing mode of the current layer
    void toggleEditing();

    // starts/stops editing mode of a layer
    bool toggleEditing( QgsMapLayer *layer, bool allowCancel = true );

    // Deletes the selected attributes for the currently selected vector layer
    void deleteSelected( QgsMapLayer *layer = nullptr, QWidget *parent = nullptr, bool checkFeaturesVisible = false );

    // Sets the active layer
    bool setActiveLayer( QgsMapLayer * );

    // Create the option dialog
    QgsOptions *createOptionsDialog( QWidget *parent = nullptr );


    // destinationLayer = The layer that the clipboard will be pasted to (defaults to the active layer on the legend)
    void pasteFromClipboard( QgsMapLayer *destinationLayer = nullptr );

    // Pastes the \a features to the \a pasteVectorLayer and gives feedback to the user according to \a invalidGeometryCount and \a nTotalFeatures
    void pasteFeatures( QgsVectorLayer *pasteVectorLayer, int invalidGeometriesCount, int nTotalFeatures, QgsFeatureList &features );



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

    // Open the project file corresponding to the
    // path at the given index in mRecentProjectPaths
    void openProject(const QString &fileName  );

    QAction *actionToggleEditing() { return nullptr; }
    QAction *actionShowPinnedLabels() { return nullptr; }


    //! Alerts user when commit errors occurred
    void commitError( QgsVectorLayer *vlayer );

signals:

    void activeLayerChanged( QgsMapLayer *layer );

    /*
         * Emitted when starting an entirely new project
         * \note
         * This is similar to projectRead(); plug-ins might want to be notified
         * that they're in a new project.  Yes, projectRead() could have been
         * overloaded to be used in the case of new projects instead.  However,
         * it's probably more semantically correct to have an entirely separate
         * signal for when this happens.
         */

    void newProject();

    /**
     * Emitted when a project file is successfully read
     * \note This is useful for plug-ins that store properties with project files.  A
     * plug-in can connect to this signal.  When it is emitted, the plug-in
     * knows to then check the project properties for any relevant state.
      */
    void projectRead();

    // show layer properties
    void showLayerProperties( QgsMapLayer *mapLayer, const QString &page = QString() );

    /**
      * Open a raster or vector file; ignore other files.
      * Used to process a commandline argument, FileOpen or Drop event.
      * Set \a allowInteractive to TRUE if it is OK to ask the user for information (mostly for
      * when a vector layer has sublayers and we want to ask which sublayers to use).
      * \returns TRUE if the file is successfully opened
      */
    bool openLayer( const QString &fileName, bool allowInteractive = false );

    /**
     * Opens a QGIS project file
     * \returns FALSE if unable to open the project
     */
    bool addProject( const QString &projectFile );

private slots:
    void namProxyAuthenticationRequired( const QNetworkProxy &proxy, QAuthenticator *auth );
    void namRequestTimedOut( const QgsNetworkRequestParameters &request );
    void markDirty();
    void authMessageOut( const QString &message, const QString &authtag, QgsAuthManager::MessageLevel level );
    void eraseAuthenticationDatabase(); //! Schedule and erase of the authentication database upon confirmation

private:

    QgisApp::SublayerHandling shouldAskUserForSublayers(const QList<QgsProviderSublayerDetails> &layers, bool hasNonLayerItems = false) const;
    template<typename T> T *addLayerPrivate(QgsMapLayerType type, const QString &uri, const QString &baseName, const QString &providerKey, bool guiWarnings = true);

    bool addVectorLayersPrivate( const QStringList &layers, const QString &enc, const QString &dataSourceType, bool guiWarning = true );
    /**
        * Access the vector layer tools. This will be an instance of {\see QgsGuiVectorLayerTools}
        * by default.
        * \returns  The vector layer tools
        */
    QgsVectorLayerTools *vectorLayerTools() { return mVectorLayerTools; }


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
    QgsVectorLayerTools *mVectorLayerTools = nullptr;
    QgsLayerStylingWidget *mMapStyleWidget = nullptr;
    QgsHandleBadLayersHandler *mAppBadLayersHandler = nullptr;

    // Helper class that connects layer tree with map canvas
    QgsLayerTreeMapCanvasBridge *mLayerTreeCanvasBridge = nullptr;

    // zoom widget
    QgsStatusBarMagnifierWidget *mMagnifierWidget = nullptr;

    QVector<QPointer<QgsCustomDropHandler>> mCustomDropHandlers;

    // Returns a pointer to the internal clipboard
    QgsClipboard *clipboard();

    // Table of contents (legend) for the map
    QgsLayerTreeView *mLayerTreeView = nullptr;

    static QgisApp *sInstance;
    QgsDockWidget *mLogDock = nullptr;

    QgsMessageLogViewer *mLogViewer = nullptr;

    QgisAppStyleSheet *mStyleSheetBuilder = nullptr;
    QgsPluginManager *mPluginManager = nullptr;

    QgsStatusBarScaleWidget *mScaleWidget = nullptr;

    // True if we are blocking the activeLayerChanged signal from being emitted
    bool mBlockActiveLayerChanged = false;

    QgsAttributeEditorContext createAttributeEditorContext();

    /**
     * String containing supporting raster file formats
     * Suitable for a QFileDialog file filter.  Build in ctor.
     */
    QString mRasterFileFilter;

    QgsMessageBar* visibleMessageBar();

    QString crsAndFormatAdjustedLayerUri( const QString &uri, const QStringList &supportedCrs, const QStringList &supportedFormats ) const;

    void onActiveLayerChanged( QgsMapLayer *layer );

    QgsAdvancedDigitizingDockWidget *mAdvancedDigitizingDockWidget = nullptr;

    QList<QPointer<QgsOptionsWidgetFactory>> mOptionsWidgetFactories;
    QList<const QgsMapLayerConfigWidgetFactory *> mMapLayerPanelFactories;

    std::unique_ptr< QgsAppMapTools > mMapTools;

    QgsStatusBar *mStatusBar = nullptr;

    //! QGIS-internal vector feature clipboard
    QgsClipboard *mInternalClipboard = nullptr;

    // A tool bar for user input
    QgsUserInputWidget *mUserInputDockWidget = nullptr;

    QAction* mActionToggleEditing = nullptr;

    QAction *mFilterLegendByMapContentAction = nullptr;

    QgsLegendFilterButton *mLegendExpressionFilterButton = nullptr;

    //! the user has trusted the project macros
    bool mPythonMacrosEnabled = false;

    /**
      * starts/stops for a vector layer \a vlayer
      */
    bool toggleEditingVectorLayer( QgsVectorLayer *vlayer, bool allowCancel = true );

    /**
      * Starts/stops for a mesh layer \a mlayer
      */
    bool toggleEditingMeshLayer( QgsMeshLayer *vlayer, bool allowCancel = true );

    void showStatusMessage( const QString &message );

    // Configure layer tree view according to the user options from QgsSettings
    void setupLayerTreeViewFromSettings();


    /**
     * Saves edits of a vector layer
     * \param leaveEditable leave the layer in editing mode when done
     * \param triggerRepaint send layer signal to repaint canvas when done
     */
    void saveVectorLayerEdits( QgsMapLayer *layer, bool leaveEditable = true, bool triggerRepaint = true );

    /**
     * Saves edits of a mesh layer
     * \param leaveEditable leave the layer in editing mode when done
     * \param triggerRepaint send layer signal to repaint canvas when done
     */
    void saveMeshLayerEdits( QgsMapLayer *layer, bool leaveEditable = true, bool triggerRepaint = true );

    // Flag to indicate an edits save/rollback for active layer is in progress
    bool mSaveRollbackInProgress = false;

    // Checks for running tasks dependent on the open project
    bool checkTasksDependOnProject();

    /**
     * Checks for unsaved changes in open layers and prompts the user to save
     * or discard these changes for each layer.
     *
     * Returns TRUE if there are no unsaved layer edits remaining, or the user
     * opted to discard them all. Returns FALSE if the user opted to cancel
     * on any layer.
     */
    bool checkUnsavedLayerEdits();


    /**
     * Check to see if the current project file is dirty and if so, prompt the user to save it.
     * \returns TRUE if saved or discarded, FALSE if canceled
     */
    bool saveDirty();


    /**
     * Checks whether memory layers (with features) exist in the project, and if so
     * shows a warning to users that their contents will be lost on
     * project unload.
     *
     * Returns TRUE if there are no memory layers present, or if the
     * user opted to discard their contents. Returns FALSE if there
     * are memory layers present and the user clicked 'Cancel' on
     * the warning dialog.
     */
    bool checkMemoryLayers();

    //! clear out any stuff from project
    void closeProject();

    class QgsCanvasRefreshBlocker
    {
    public:

        QgsCanvasRefreshBlocker()
        {
            if ( QgisApp::instance()->mFreezeCount++ == 0 )
            {
                // going from unfrozen to frozen, so freeze canvases
                QgisApp::instance()->freezeCanvases( true );
            }
        }
        QgsCanvasRefreshBlocker( const QgsCanvasRefreshBlocker &other ) = delete;
        QgsCanvasRefreshBlocker &operator=( const QgsCanvasRefreshBlocker &other ) = delete;

        void release()
        {
            if ( mReleased )
                return;

            mReleased = true;
            if ( --QgisApp::instance()->mFreezeCount == 0 )
            {
                // going from frozen to unfrozen, so unfreeze canvases
                QgisApp::instance()->freezeCanvases( false );
                QgisApp::instance()->refreshMapCanvas();
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

#endif // QgisApp_H
