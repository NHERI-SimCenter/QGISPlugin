QT += core widgets gui xml network sql svg concurrent printsupport webengine webenginewidgets

DEFINES += Q_WS_MAC HAVE_STATIC_PROVIDERS #WITH_QTWEBKIT

DEFINES += TEST_DATA_DIR=\\\"$$PWD/tests/testdata\\\"

CONFIG += c++17

PATH_TO_QGIS=/Users/steve/Desktop/C++Libraries/QGIS/QGIS
PATH_TO_QGIS_SRC=$$PATH_TO_QGIS/src
PATH_TO_QGIS_DEPS=/opt/QGIS/qgis-deps-0.8.0/stage/include
PATH_TO_QGIS_BUILD=/Users/steve/Desktop/C++Libraries/QGIS/build

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    QGISVisualizationWidget.cpp \
        QgisApp.cpp \
        main.cpp \
        mainwindow.cpp \
        $$PATH_TO_QGIS_SRC/app/browser/qgsinbuiltdataitemproviders.cpp  \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolreverseline.cpp  \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolselectionhandler.cpp \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationcopyright.cpp \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationcopyrightdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationgrid.cpp \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationgriddialog.cpp \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationimage.cpp \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationimagedialog.cpp \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationitem.cpp \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationlayoutextent.cpp \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationlayoutextentdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationnortharrow.cpp \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationnortharrowdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationscalebar.cpp \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationscalebardialog.cpp \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationtitle.cpp \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationtitledialog.cpp \
        $$PATH_TO_QGIS_SRC/app/devtools/networklogger/qgsnetworklogger.cpp \
        $$PATH_TO_QGIS_SRC/app/devtools/networklogger/qgsnetworkloggernode.cpp \
        $$PATH_TO_QGIS_SRC/app/devtools/networklogger/qgsnetworkloggerpanelwidget.cpp \
        $$PATH_TO_QGIS_SRC/app/devtools/networklogger/qgsnetworkloggerwidgetfactory.cpp \
        $$PATH_TO_QGIS_SRC/app/devtools/profiler/qgsprofilerpanelwidget.cpp \
        $$PATH_TO_QGIS_SRC/app/devtools/profiler/qgsprofilerwidgetfactory.cpp \
        $$PATH_TO_QGIS_SRC/app/devtools/qgsappdevtoolutils.cpp \
        $$PATH_TO_QGIS_SRC/app/dwg/qgsdwgimportdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/dwg/qgsdwgimporter.cpp \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgcpcanvasitem.cpp \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgcplist.cpp \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgcplistmodel.cpp \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgcplistwidget.cpp \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgeorefconfigdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgeorefdatapoint.cpp \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgeorefdelegates.cpp \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgeorefmainwindow.cpp \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgeoreftooladdpoint.cpp \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgeoreftooldeletepoint.cpp \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgeoreftoolmovepoint.cpp \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgeoreftransform.cpp \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgeorefvalidators.cpp \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsimagewarper.cpp \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsmapcoordsdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsrasterchangecoords.cpp \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsresidualplotitem.cpp \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgstransformsettingsdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsvalidateddoublespinbox.cpp \
        $$PATH_TO_QGIS_SRC/app/labeling/qgslabelpropertydialog.cpp \
        $$PATH_TO_QGIS_SRC/app/labeling/qgsmaptoolchangelabelproperties.cpp \
        $$PATH_TO_QGIS_SRC/app/labeling/qgsmaptoollabel.cpp \
        $$PATH_TO_QGIS_SRC/app/labeling/qgsmaptoolmovelabel.cpp \
        $$PATH_TO_QGIS_SRC/app/labeling/qgsmaptoolpinlabels.cpp \
        $$PATH_TO_QGIS_SRC/app/labeling/qgsmaptoolrotatelabel.cpp \
        $$PATH_TO_QGIS_SRC/app/labeling/qgsmaptoolshowhidelabels.cpp \
        $$PATH_TO_QGIS_SRC/app/maptools/qgsappmaptools.cpp \
        $$PATH_TO_QGIS_SRC/app/mesh/qgsmaptooleditmeshframe.cpp \
        $$PATH_TO_QGIS_SRC/app/mesh/qgsnewmeshlayerdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/mesh/qgsmeshcalculatordialog.cpp \
        $$PATH_TO_QGIS_SRC/app/options/qgsoptions.cpp \
        $$PATH_TO_QGIS_SRC/app/options/qgsadvancedoptions.cpp \
        $$PATH_TO_QGIS_SRC/app/options/qgsoptionsutils.cpp \
        $$PATH_TO_QGIS_SRC/app/options/qgscodeeditoroptions.cpp \
        $$PATH_TO_QGIS_SRC/app/options/qgsgpsdeviceoptions.cpp \
        $$PATH_TO_QGIS_SRC/app/pluginmanager/qgsapppluginmanagerinterface.cpp \
        $$PATH_TO_QGIS_SRC/app/pluginmanager/qgspluginitemdelegate.cpp \
        $$PATH_TO_QGIS_SRC/app/pluginmanager/qgspluginmanager.cpp \
        $$PATH_TO_QGIS_SRC/app/pluginmanager/qgspluginmanager_texts.cpp \
        $$PATH_TO_QGIS_SRC/app/pluginmanager/qgspluginsortfilterproxymodel.cpp \
        $$PATH_TO_QGIS_SRC/app/pointcloud/qgspointcloudlayerproperties.cpp \
        $$PATH_TO_QGIS_SRC/app/qgisappinterface.cpp \
        $$PATH_TO_QGIS_SRC/app/qgisappstylesheet.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsabout.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsalignrasterdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsanimationexportdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsannotationwidget.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsappauthrequesthandler.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsappbrowserproviders.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsappcoordinateoperationhandlers.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsapplayertreeviewmenuprovider.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsappscreenshots.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsappsslerrorhandler.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsappwindowmanager.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsattributetabledialog.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsbookmarkeditordialog.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsbookmarks.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsclipboard.cpp \
        $$PATH_TO_QGIS_SRC/app/qgscrashhandler.cpp \
        $$PATH_TO_QGIS_SRC/app/qgscustomization.cpp \
        $$PATH_TO_QGIS_SRC/app/qgscustomprojectiondialog.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsdatumtransformtablewidget.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsdelattrdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsdevtoolspanelwidget.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsdiscoverrelationsdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsdisplayangle.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsdxfexportdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsfeatureaction.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsfirstrundialog.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsfixattributedialog.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsformannotationdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsgeometryvalidationdock.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsgeometryvalidationmodel.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsgeometryvalidationservice.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsguivectorlayertools.cpp \
        $$PATH_TO_QGIS_SRC/app/qgshandlebadlayers.cpp \
        $$PATH_TO_QGIS_SRC/app/qgshtmlannotationdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsidentifyresultsdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/qgslayercapabilitiesmodel.cpp \
        $$PATH_TO_QGIS_SRC/app/qgslayernotesmanager.cpp \
        $$PATH_TO_QGIS_SRC/app/qgslayerstylingwidget.cpp \
        $$PATH_TO_QGIS_SRC/app/qgslayertreeviewbadlayerindicator.cpp \
        $$PATH_TO_QGIS_SRC/app/qgslayertreeviewembeddedindicator.cpp \
        $$PATH_TO_QGIS_SRC/app/qgslayertreeviewfilterindicator.cpp \
        $$PATH_TO_QGIS_SRC/app/qgslayertreeviewindicatorprovider.cpp \
        $$PATH_TO_QGIS_SRC/app/qgslayertreeviewlowaccuracyindicator.cpp \
        $$PATH_TO_QGIS_SRC/app/qgslayertreeviewmemoryindicator.cpp \
        $$PATH_TO_QGIS_SRC/app/qgslayertreeviewnocrsindicator.cpp \
        $$PATH_TO_QGIS_SRC/app/qgslayertreeviewnonremovableindicator.cpp \
        $$PATH_TO_QGIS_SRC/app/qgslayertreeviewnotesindicator.cpp \
        $$PATH_TO_QGIS_SRC/app/qgslayertreeviewofflineindicator.cpp \
        $$PATH_TO_QGIS_SRC/app/qgslayertreeviewtemporalindicator.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmapcanvasdockwidget.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmapsavedialog.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmapthemes.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooladdabstract.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooladdcircle.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooladdcircularstring.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooladdellipse.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooladdfeature.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooladdpart.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooladdrectangle.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooladdregularpolygon.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooladdring.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolannotation.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolcircle2points.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolcircle2tangentspoint.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolcircle3points.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolcircle3tangents.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolcirclecenterpoint.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolcircularstringcurvepoint.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolcircularstringradius.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooldeletepart.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooldeletering.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolellipsecenter2points.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolellipsecenterpoint.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolellipseextent.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolellipsefoci.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolfeatureaction.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolfillring.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolformannotation.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolhtmlannotation.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolidentifyaction.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolmeasureangle.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolmeasurebearing.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolmovefeature.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooloffsetcurve.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooloffsetpointsymbol.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolpointsymbol.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolrectangle3points.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolrectanglecenter.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolrectangleextent.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolregularpolygon2points.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolregularpolygoncentercorner.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolregularpolygoncenterpoint.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolreshape.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolrotatefeature.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolrotatepointsymbols.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolscalefeature.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolselect.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolselectutils.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolsimplify.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolsplitfeatures.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolsplitparts.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolsvgannotation.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooltextannotation.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooltrimextendfeature.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmeasuredialog.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmeasuretool.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsmergeattributesdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsnewspatialitelayerdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/qgspluginmetadata.cpp \
        $$PATH_TO_QGIS_SRC/app/qgspluginregistry.cpp \
        $$PATH_TO_QGIS_SRC/app/qgspointmarkeritem.cpp \
        $$PATH_TO_QGIS_SRC/app/qgspointrotationitem.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsprojectlayergroupdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsprojectlistitemdelegate.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsprojectproperties.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsprovidersublayersdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/qgspuzzlewidget.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsrastercalcdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsrecentprojectsitemsmodel.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsrelationadddlg.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsrelationaddpolymorphicdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsrelationmanagerdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsselectbyformdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/qgssettingstree.cpp \
        $$PATH_TO_QGIS_SRC/app/qgssnappinglayertreemodel.cpp \
        $$PATH_TO_QGIS_SRC/app/qgssnappingwidget.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsstatisticalsummarydockwidget.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsstatusbarcoordinateswidget.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsstatusbarmagnifierwidget.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsstatusbarscalewidget.cpp \
        $$PATH_TO_QGIS_SRC/app/qgssvgannotationdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/qgstemplateprojectsmodel.cpp \
        $$PATH_TO_QGIS_SRC/app/qgstemporalcontrollerdockwidget.cpp \
        $$PATH_TO_QGIS_SRC/app/qgstextannotationdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsundowidget.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsvariantdelegate.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsvectorlayerdigitizingproperties.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsversioninfo.cpp \
        $$PATH_TO_QGIS_SRC/app/qgsversionmigration.cpp \
        $$PATH_TO_QGIS_SRC/app/qgswelcomepage.cpp \
        $$PATH_TO_QGIS_SRC/app/vectortile/qgsvectortilelayerproperties.cpp \
        $$PATH_TO_QGIS_SRC/app/vertextool/qgslockedfeature.cpp \
        $$PATH_TO_QGIS_SRC/app/vertextool/qgsvertexeditor.cpp \
        $$PATH_TO_QGIS_SRC/app/vertextool/qgsvertextool.cpp \
        $$PATH_TO_QGIS_SRC/core/network/qgsnetworkaccessmanager.cpp \
        $$PATH_TO_QGIS_SRC/core/network/qgsnetworkdiskcache.cpp \
        $$PATH_TO_QGIS_SRC/gui/auth/qgsauthsettingswidget.cpp \
        $$PATH_TO_QGIS_SRC/gui/qgsdatasourcemanagerdialog.cpp \
        $$PATH_TO_QGIS_SRC/gui/qgsdatumtransformdialog.cpp \
        $$PATH_TO_QGIS_SRC/providers/arcgisrest/qgsafsfeatureiterator.cpp \
        $$PATH_TO_QGIS_SRC/providers/arcgisrest/qgsafsprovider.cpp \
        $$PATH_TO_QGIS_SRC/providers/arcgisrest/qgsafsshareddata.cpp \
        $$PATH_TO_QGIS_SRC/providers/arcgisrest/qgsamsprovider.cpp \
        $$PATH_TO_QGIS_SRC/providers/arcgisrest/qgsarcgisrestdataitemguiprovider.cpp \
        $$PATH_TO_QGIS_SRC/providers/arcgisrest/qgsarcgisrestdataitems.cpp \
        $$PATH_TO_QGIS_SRC/providers/arcgisrest/qgsarcgisrestsourceselect.cpp \
        $$PATH_TO_QGIS_SRC/providers/arcgisrest/qgsarcgisrestsourcewidget.cpp \
        $$PATH_TO_QGIS_SRC/providers/arcgisrest/qgsnewarcgisrestconnection.cpp \
        $$PATH_TO_QGIS_SRC/providers/wms/qgstilescalewidget.cpp \
        $$PATH_TO_QGIS_SRC/providers/wms/qgswmscapabilities.cpp \
        $$PATH_TO_QGIS_SRC/providers/wms/qgswmsconnection.cpp \
        $$PATH_TO_QGIS_SRC/providers/wms/qgswmsdataitemguiproviders.cpp \
        $$PATH_TO_QGIS_SRC/providers/wms/qgswmsdataitems.cpp \
        $$PATH_TO_QGIS_SRC/providers/wms/qgswmsprovider.cpp \
        $$PATH_TO_QGIS_SRC/providers/wms/qgswmsprovidergui.cpp \
        $$PATH_TO_QGIS_SRC/providers/wms/qgswmssourceselect.cpp \
        $$PATH_TO_QGIS_SRC/providers/wms/qgswmstsettingswidget.cpp \
        $$PATH_TO_QGIS_SRC/providers/wms/qgswmtsdimensions.cpp \
        $$PATH_TO_QGIS_SRC/providers/wms/qgsxyzconnection.cpp \
        $$PATH_TO_QGIS_SRC/providers/wms/qgsxyzconnectiondialog.cpp \
        $$PATH_TO_QGIS_SRC/providers/wms/qgsxyzsourceselect.cpp \
        $$PATH_TO_QGIS_SRC/providers/wms/qgsxyzsourcewidget.cpp \
        $$PATH_TO_QGIS_SRC/app/pointcloud/qgspointcloudlayerstylewidget.cpp \
        $$PATH_TO_QGIS_SRC/app/pointcloud/qgspointcloudelevationpropertieswidget.cpp \
        $$PATH_TO_QGIS_SRC/app/locator/qgslayertreelocatorfilter.cpp \
        $$PATH_TO_QGIS_SRC/app/locator/qgsbookmarklocatorfilter.cpp \
        $$PATH_TO_QGIS_SRC/app/locator/qgsnominatimlocatorfilter.cpp \
        $$PATH_TO_QGIS_SRC/app/locator/qgsactionlocatorfilter.cpp \
        $$PATH_TO_QGIS_SRC/app/locator/qgsgotolocatorfilter.cpp \
        $$PATH_TO_QGIS_SRC/app/locator/qgsexpressioncalculatorlocatorfilter.cpp \
        $$PATH_TO_QGIS_SRC/app/locator/qgsactivelayerfeatureslocatorfilter.cpp \
        $$PATH_TO_QGIS_SRC/app/locator/qgsalllayersfeatureslocatorfilter.cpp \
        $$PATH_TO_QGIS_SRC/app/locator/qgssettingslocatorfilter.cpp \
        $$PATH_TO_QGIS_SRC/app/locator/qgslayoutlocatorfilter.cpp \
        $$PATH_TO_QGIS_SRC/app/locator/qgslocatoroptionswidget.cpp \
        $$PATH_TO_QGIS_SRC/app/layout/qgslayoutmanagerdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/layout/qgslayoutdesignerdialog.cpp \
        $$PATH_TO_QGIS_SRC/app/layout/qgsreportsectionmodel.cpp \
        $$PATH_TO_QGIS_SRC/app/layout/qgslayoutappmenuprovider.cpp \
        $$PATH_TO_QGIS_SRC/app/layout/qgslayoutimagedrophandler.cpp \
        $$PATH_TO_QGIS_SRC/app/layout/qgsreportfieldgroupsectionwidget.cpp \
        $$PATH_TO_QGIS_SRC/app/layout/qgsreportsectionwidget.cpp \
        $$PATH_TO_QGIS_SRC/app/layout/qgsreportlayoutsectionwidget.cpp \
        $$PATH_TO_QGIS_SRC/app/layout/qgsreportorganizerwidget.cpp \
        $$PATH_TO_QGIS_SRC/app/gps/qgsgpsbearingitem.cpp \
        $$PATH_TO_QGIS_SRC/app/gps/qgsgpsmarker.cpp \
        $$PATH_TO_QGIS_SRC/app/gps/qgsgpsinformationwidget.cpp \
        $$PATH_TO_QGIS/external/libdxfrw/intern/dwgreader21.cpp \
        $$PATH_TO_QGIS/external/libdxfrw/intern/dwgreader24.cpp \
        $$PATH_TO_QGIS/external/libdxfrw/intern/dwgreader15.cpp \
        $$PATH_TO_QGIS/external/libdxfrw/intern/dwgreader27.cpp \
        $$PATH_TO_QGIS/external/libdxfrw/intern/dwgreader18.cpp \
        $$PATH_TO_QGIS/external/libdxfrw/intern/rscodec.cpp \
        $$PATH_TO_QGIS/external/libdxfrw/intern/drw_textcodec.cpp \
        $$PATH_TO_QGIS/external/libdxfrw/intern/drw_dbg.cpp \
        $$PATH_TO_QGIS/external/libdxfrw/intern/dwgutil.cpp \
        $$PATH_TO_QGIS/external/libdxfrw/intern/dxfreader.cpp \
        $$PATH_TO_QGIS/external/libdxfrw/intern/dwgreader.cpp \
        $$PATH_TO_QGIS/external/libdxfrw/intern/dwgbuffer.cpp \
        $$PATH_TO_QGIS/external/libdxfrw/intern/dxfwriter.cpp \
        $$PATH_TO_QGIS/external/libdxfrw/drw_base.cpp \
        $$PATH_TO_QGIS/external/libdxfrw/drw_header.cpp \
        $$PATH_TO_QGIS/external/libdxfrw/libdwgr.cpp \
        $$PATH_TO_QGIS/external/libdxfrw/drw_entities.cpp \
        $$PATH_TO_QGIS/external/libdxfrw/drw_classes.cpp \
        $$PATH_TO_QGIS/external/libdxfrw/drw_objects.cpp \
        $$PATH_TO_QGIS/external/libdxfrw/libdxfrw.cpp \
        $$PATH_TO_QGIS/external/qt-unix-signals/sigwatch.cpp \

#ifdef3d
#$$PATH_TO_QGIS_SRC/app/layout/qgslayout3dmapwidget.cpp \


HEADERS += \
    QGISVisualizationWidget.h \
        QgisApp.h \
        mainwindow.h \
        /Users/steve/Desktop/C++Libraries/QGIS/Install/include/qgis_app.h \
        $$PATH_TO_QGIS_SRC/app/browser/qgsinbuiltdataitemproviders.h  \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolreverseline.h  \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolselectionhandler.h \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationcopyright.h \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationcopyrightdialog.h \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationgrid.h \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationgriddialog.h \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationimage.h \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationimagedialog.h \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationitem.h \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationlayoutextent.h \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationlayoutextentdialog.h \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationnortharrow.h \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationnortharrowdialog.h \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationscalebar.h \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationscalebardialog.h \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationtitle.h \
        $$PATH_TO_QGIS_SRC/app/decorations/qgsdecorationtitledialog.h \
        $$PATH_TO_QGIS_SRC/app/devtools/networklogger/qgsnetworklogger.h \
        $$PATH_TO_QGIS_SRC/app/devtools/networklogger/qgsnetworkloggernode.h \
        $$PATH_TO_QGIS_SRC/app/devtools/networklogger/qgsnetworkloggerpanelwidget.h \
        $$PATH_TO_QGIS_SRC/app/devtools/networklogger/qgsnetworkloggerwidgetfactory.h \
        $$PATH_TO_QGIS_SRC/app/devtools/profiler/qgsprofilerpanelwidget.h \
        $$PATH_TO_QGIS_SRC/app/devtools/profiler/qgsprofilerwidgetfactory.h \
        $$PATH_TO_QGIS_SRC/app/devtools/qgsappdevtoolutils.h \
        $$PATH_TO_QGIS_SRC/app/dwg/qgsdwgimportdialog.h \
        $$PATH_TO_QGIS_SRC/app/dwg/qgsdwgimporter.h \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgcpcanvasitem.h \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgcplist.h \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgcplistmodel.h \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgcplistwidget.h \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgeorefconfigdialog.h \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgeorefdatapoint.h \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgeorefdelegates.h \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgeorefmainwindow.h \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgeoreftooladdpoint.h \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgeoreftooldeletepoint.h \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgeoreftoolmovepoint.h \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgeoreftransform.h \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsgeorefvalidators.h \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsimagewarper.h \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsmapcoordsdialog.h \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsrasterchangecoords.h \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsresidualplotitem.h \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgstransformsettingsdialog.h \
        $$PATH_TO_QGIS_SRC/app/georeferencer/qgsvalidateddoublespinbox.h \
        $$PATH_TO_QGIS_SRC/app/labeling/qgslabelpropertydialog.h \
        $$PATH_TO_QGIS_SRC/app/labeling/qgsmaptoolchangelabelproperties.h \
        $$PATH_TO_QGIS_SRC/app/labeling/qgsmaptoollabel.h \
        $$PATH_TO_QGIS_SRC/app/labeling/qgsmaptoolmovelabel.h \
        $$PATH_TO_QGIS_SRC/app/labeling/qgsmaptoolpinlabels.h \
        $$PATH_TO_QGIS_SRC/app/labeling/qgsmaptoolrotatelabel.h \
        $$PATH_TO_QGIS_SRC/app/labeling/qgsmaptoolshowhidelabels.h \
        $$PATH_TO_QGIS_SRC/app/maptools/qgsappmaptools.h \
        $$PATH_TO_QGIS_SRC/app/mesh/qgsmaptooleditmeshframe.h \
        $$PATH_TO_QGIS_SRC/app/mesh/qgsnewmeshlayerdialog.h \
        $$PATH_TO_QGIS_SRC/app/mesh/qgsmeshcalculatordialog.h \
        $$PATH_TO_QGIS_SRC/app/options/qgsoptions.h \
        $$PATH_TO_QGIS_SRC/app/options/qgsadvancedoptions.h \
        $$PATH_TO_QGIS_SRC/app/options/qgsoptionsutils.h \
        $$PATH_TO_QGIS_SRC/app/options/qgscodeeditoroptions.h \
        $$PATH_TO_QGIS_SRC/app/options/qgsgpsdeviceoptions.h \
        $$PATH_TO_QGIS_SRC/app/pluginmanager/qgsapppluginmanagerinterface.h \
        $$PATH_TO_QGIS_SRC/app/pluginmanager/qgspluginitemdelegate.h \
        $$PATH_TO_QGIS_SRC/app/pluginmanager/qgspluginmanager.h \
        $$PATH_TO_QGIS_SRC/app/pluginmanager/qgspluginsortfilterproxymodel.h \
        $$PATH_TO_QGIS_SRC/app/pointcloud/qgspointcloudlayerproperties.h \
        $$PATH_TO_QGIS_SRC/app/qgisappinterface.h \
        $$PATH_TO_QGIS_SRC/app/qgisappstylesheet.h \
        $$PATH_TO_QGIS_SRC/app/qgsabout.h \
        $$PATH_TO_QGIS_SRC/app/qgsalignrasterdialog.h \
        $$PATH_TO_QGIS_SRC/app/qgsanimationexportdialog.h \
        $$PATH_TO_QGIS_SRC/app/qgsannotationwidget.h \
        $$PATH_TO_QGIS_SRC/app/qgsappauthrequesthandler.h \
        $$PATH_TO_QGIS_SRC/app/qgsappbrowserproviders.h \
        $$PATH_TO_QGIS_SRC/app/qgsappcoordinateoperationhandlers.h \
        $$PATH_TO_QGIS_SRC/app/qgsapplayertreeviewmenuprovider.h \
        $$PATH_TO_QGIS_SRC/app/qgsappscreenshots.h \
        $$PATH_TO_QGIS_SRC/app/qgsappsslerrorhandler.h \
        $$PATH_TO_QGIS_SRC/app/qgsappwindowmanager.h \
        $$PATH_TO_QGIS_SRC/app/qgsattributetabledialog.h \
        $$PATH_TO_QGIS_SRC/app/qgsbookmarkeditordialog.h \
        $$PATH_TO_QGIS_SRC/app/qgsbookmarks.h \
        $$PATH_TO_QGIS_SRC/app/qgsclipboard.h \
        $$PATH_TO_QGIS_SRC/app/qgscrashhandler.h \
        $$PATH_TO_QGIS_SRC/app/qgscustomization.h \
        $$PATH_TO_QGIS_SRC/app/qgscustomprojectiondialog.h \
        $$PATH_TO_QGIS_SRC/app/qgsdatumtransformtablewidget.h \
        $$PATH_TO_QGIS_SRC/app/qgsdelattrdialog.h \
        $$PATH_TO_QGIS_SRC/app/qgsdevtoolspanelwidget.h \
        $$PATH_TO_QGIS_SRC/app/qgsdiscoverrelationsdialog.h \
        $$PATH_TO_QGIS_SRC/app/qgsdisplayangle.h \
        $$PATH_TO_QGIS_SRC/app/qgsdxfexportdialog.h \
        $$PATH_TO_QGIS_SRC/app/qgsfeatureaction.h \
        $$PATH_TO_QGIS_SRC/app/qgsfirstrundialog.h \
        $$PATH_TO_QGIS_SRC/app/qgsfixattributedialog.h \
        $$PATH_TO_QGIS_SRC/app/qgsformannotationdialog.h \
        $$PATH_TO_QGIS_SRC/app/qgsgeometryvalidationdock.h \
        $$PATH_TO_QGIS_SRC/app/qgsgeometryvalidationmodel.h \
        $$PATH_TO_QGIS_SRC/app/qgsgeometryvalidationservice.h \
        $$PATH_TO_QGIS_SRC/app/qgsguivectorlayertools.h \
        $$PATH_TO_QGIS_SRC/app/qgshandlebadlayers.h \
        $$PATH_TO_QGIS_SRC/app/qgshtmlannotationdialog.h \
        $$PATH_TO_QGIS_SRC/app/qgsidentifyresultsdialog.h \
        $$PATH_TO_QGIS_SRC/app/qgslayercapabilitiesmodel.h \
        $$PATH_TO_QGIS_SRC/app/qgslayernotesmanager.h \
        $$PATH_TO_QGIS_SRC/app/qgslayerstylingwidget.h \
        $$PATH_TO_QGIS_SRC/app/qgslayertreeviewbadlayerindicator.h \
        $$PATH_TO_QGIS_SRC/app/qgslayertreeviewembeddedindicator.h \
        $$PATH_TO_QGIS_SRC/app/qgslayertreeviewfilterindicator.h \
        $$PATH_TO_QGIS_SRC/app/qgslayertreeviewindicatorprovider.h \
        $$PATH_TO_QGIS_SRC/app/qgslayertreeviewlowaccuracyindicator.h \
        $$PATH_TO_QGIS_SRC/app/qgslayertreeviewmemoryindicator.h \
        $$PATH_TO_QGIS_SRC/app/qgslayertreeviewnocrsindicator.h \
        $$PATH_TO_QGIS_SRC/app/qgslayertreeviewnonremovableindicator.h \
        $$PATH_TO_QGIS_SRC/app/qgslayertreeviewnotesindicator.h \
        $$PATH_TO_QGIS_SRC/app/qgslayertreeviewofflineindicator.h \
        $$PATH_TO_QGIS_SRC/app/qgslayertreeviewtemporalindicator.h \
        $$PATH_TO_QGIS_SRC/app/qgsmapcanvasdockwidget.h \
        $$PATH_TO_QGIS_SRC/app/qgsmapsavedialog.h \
        $$PATH_TO_QGIS_SRC/app/qgsmapthemes.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooladdabstract.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooladdcircle.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooladdcircularstring.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooladdellipse.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooladdfeature.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooladdpart.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooladdrectangle.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooladdregularpolygon.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooladdring.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolannotation.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolcircle2points.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolcircle2tangentspoint.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolcircle3points.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolcircle3tangents.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolcirclecenterpoint.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolcircularstringcurvepoint.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolcircularstringradius.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooldeletepart.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooldeletering.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolellipsecenter2points.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolellipsecenterpoint.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolellipseextent.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolellipsefoci.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolfeatureaction.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolfillring.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolformannotation.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolhtmlannotation.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolidentifyaction.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolmeasureangle.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolmeasurebearing.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolmovefeature.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooloffsetcurve.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooloffsetpointsymbol.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolpointsymbol.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolrectangle3points.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolrectanglecenter.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolrectangleextent.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolregularpolygon2points.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolregularpolygoncentercorner.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolregularpolygoncenterpoint.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolreshape.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolrotatefeature.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolrotatepointsymbols.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolscalefeature.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolselect.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolselectutils.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolsimplify.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolsplitfeatures.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolsplitparts.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptoolsvgannotation.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooltextannotation.h \
        $$PATH_TO_QGIS_SRC/app/qgsmaptooltrimextendfeature.h \
        $$PATH_TO_QGIS_SRC/app/qgsmeasuredialog.h \
        $$PATH_TO_QGIS_SRC/app/qgsmeasuretool.h \
        $$PATH_TO_QGIS_SRC/app/qgsmergeattributesdialog.h \
        $$PATH_TO_QGIS_SRC/app/qgsnewspatialitelayerdialog.h \
        $$PATH_TO_QGIS_SRC/app/qgspluginmetadata.h \
        $$PATH_TO_QGIS_SRC/app/qgspluginregistry.h \
        $$PATH_TO_QGIS_SRC/app/qgspointmarkeritem.h \
        $$PATH_TO_QGIS_SRC/app/qgspointrotationitem.h \
        $$PATH_TO_QGIS_SRC/app/qgsprojectlayergroupdialog.h \
        $$PATH_TO_QGIS_SRC/app/qgsprojectlistitemdelegate.h \
        $$PATH_TO_QGIS_SRC/app/qgsprojectproperties.h \
        $$PATH_TO_QGIS_SRC/app/qgsprovidersublayersdialog.h \
        $$PATH_TO_QGIS_SRC/app/qgspuzzlewidget.h \
        $$PATH_TO_QGIS_SRC/app/qgsrastercalcdialog.h \
        $$PATH_TO_QGIS_SRC/app/qgsrecentprojectsitemsmodel.h \
        $$PATH_TO_QGIS_SRC/app/qgsrelationadddlg.h \
        $$PATH_TO_QGIS_SRC/app/qgsrelationaddpolymorphicdialog.h \
        $$PATH_TO_QGIS_SRC/app/qgsrelationmanagerdialog.h \
        $$PATH_TO_QGIS_SRC/app/qgsselectbyformdialog.h \
        $$PATH_TO_QGIS_SRC/app/qgssettingstree.h \
        $$PATH_TO_QGIS_SRC/app/qgssnappinglayertreemodel.h \
        $$PATH_TO_QGIS_SRC/app/qgssnappingwidget.h \
        $$PATH_TO_QGIS_SRC/app/qgsstatisticalsummarydockwidget.h \
        $$PATH_TO_QGIS_SRC/app/qgsstatusbarcoordinateswidget.h \
        $$PATH_TO_QGIS_SRC/app/qgsstatusbarmagnifierwidget.h \
        $$PATH_TO_QGIS_SRC/app/qgsstatusbarscalewidget.h \
        $$PATH_TO_QGIS_SRC/app/qgssvgannotationdialog.h \
        $$PATH_TO_QGIS_SRC/app/qgssvgannotationitemdialog.h \
        $$PATH_TO_QGIS_SRC/app/qgstemplateprojectsmodel.h \
        $$PATH_TO_QGIS_SRC/app/qgstemporalcontrollerdockwidget.h \
        $$PATH_TO_QGIS_SRC/app/qgstextannotationdialog.h \
        $$PATH_TO_QGIS_SRC/app/qgsundowidget.h \
        $$PATH_TO_QGIS_SRC/app/qgsvariantdelegate.h \
        $$PATH_TO_QGIS_SRC/app/qgsvectorlayerdigitizingproperties.h \
        $$PATH_TO_QGIS_SRC/app/qgsversioninfo.h \
        $$PATH_TO_QGIS_SRC/app/qgsversionmigration.h \
        $$PATH_TO_QGIS_SRC/app/qgswelcomepage.h \
        $$PATH_TO_QGIS_SRC/app/vectortile/qgsvectortilelayerproperties.h \
        $$PATH_TO_QGIS_SRC/app/vertextool/qgslockedfeature.h \
        $$PATH_TO_QGIS_SRC/app/vertextool/qgsvertexeditor.h \
        $$PATH_TO_QGIS_SRC/app/vertextool/qgsvertextool.h \
        $$PATH_TO_QGIS_SRC/core/network/qgsnetworkaccessmanager.h \
        $$PATH_TO_QGIS_SRC/core/network/qgsnetworkdiskcache.h \
        $$PATH_TO_QGIS_SRC/core/qgswebview.h \
        $$PATH_TO_QGIS_SRC/gui/auth/qgsauthsettingswidget.h \
        $$PATH_TO_QGIS_SRC/gui/qgsdatasourcemanagerdialog.h \
        $$PATH_TO_QGIS_SRC/gui/qgsdatumtransformdialog.h \
        $$PATH_TO_QGIS_SRC/providers/arcgisrest/qgsafsfeatureiterator.h \
        $$PATH_TO_QGIS_SRC/providers/arcgisrest/qgsafsprovider.h \
        $$PATH_TO_QGIS_SRC/providers/arcgisrest/qgsafsshareddata.h \
        $$PATH_TO_QGIS_SRC/providers/arcgisrest/qgsamsprovider.h \
        $$PATH_TO_QGIS_SRC/providers/arcgisrest/qgsarcgisrestdataitemguiprovider.h \
        $$PATH_TO_QGIS_SRC/providers/arcgisrest/qgsarcgisrestdataitems.h \
        $$PATH_TO_QGIS_SRC/providers/arcgisrest/qgsarcgisrestsourceselect.h \
        $$PATH_TO_QGIS_SRC/providers/arcgisrest/qgsarcgisrestsourcewidget.h \
        $$PATH_TO_QGIS_SRC/providers/arcgisrest/qgsnewarcgisrestconnection.h \
        $$PATH_TO_QGIS_SRC/providers/wms/qgstilescalewidget.h \
        $$PATH_TO_QGIS_SRC/providers/wms/qgswmscapabilities.h \
        $$PATH_TO_QGIS_SRC/providers/wms/qgswmsconnection.h \
        $$PATH_TO_QGIS_SRC/providers/wms/qgswmsdataitemguiproviders.h \
        $$PATH_TO_QGIS_SRC/providers/wms/qgswmsdataitems.h \
        $$PATH_TO_QGIS_SRC/providers/wms/qgswmsprovider.h \
        $$PATH_TO_QGIS_SRC/providers/wms/qgswmsprovidergui.h \
        $$PATH_TO_QGIS_SRC/providers/wms/qgswmssourceselect.h \
        $$PATH_TO_QGIS_SRC/providers/wms/qgswmstsettingswidget.h \
        $$PATH_TO_QGIS_SRC/providers/wms/qgswmtsdimensions.h \
        $$PATH_TO_QGIS_SRC/providers/wms/qgsxyzconnection.h \
        $$PATH_TO_QGIS_SRC/providers/wms/qgsxyzconnectiondialog.h \
        $$PATH_TO_QGIS_SRC/providers/wms/qgsxyzsourceselect.h \
        $$PATH_TO_QGIS_SRC/providers/wms/qgsxyzsourcewidget.h \
        $$PATH_TO_QGIS_SRC/app/pointcloud/qgspointcloudlayerstylewidget.h \
        $$PATH_TO_QGIS_SRC/app/pointcloud/qgspointcloudelevationpropertieswidget.h \
        $$PATH_TO_QGIS_SRC/app/locator/qgslayertreelocatorfilter.h \
        $$PATH_TO_QGIS_SRC/app/locator/qgsbookmarklocatorfilter.h \
        $$PATH_TO_QGIS_SRC/app/locator/qgsnominatimlocatorfilter.h \
        $$PATH_TO_QGIS_SRC/app/locator/qgsactionlocatorfilter.h \
        $$PATH_TO_QGIS_SRC/app/locator/qgsgotolocatorfilter.h \
        $$PATH_TO_QGIS_SRC/app/locator/qgsexpressioncalculatorlocatorfilter.h \
        $$PATH_TO_QGIS_SRC/app/locator/qgsactivelayerfeatureslocatorfilter.h \
        $$PATH_TO_QGIS_SRC/app/locator/qgsalllayersfeatureslocatorfilter.h \
        $$PATH_TO_QGIS_SRC/app/locator/qgssettingslocatorfilter.h \
        $$PATH_TO_QGIS_SRC/app/locator/qgslayoutlocatorfilter.h \
        $$PATH_TO_QGIS_SRC/app/locator/qgslocatoroptionswidget.h \
        $$PATH_TO_QGIS_SRC/app/layout/qgslayoutmanagerdialog.h \
        $$PATH_TO_QGIS_SRC/app/layout/qgslayoutdesignerdialog.h \
        $$PATH_TO_QGIS_SRC/app/layout/qgsreportsectionmodel.h \
        $$PATH_TO_QGIS_SRC/app/layout/qgslayoutappmenuprovider.h \
        $$PATH_TO_QGIS_SRC/app/layout/qgslayoutimagedrophandler.h \
        $$PATH_TO_QGIS_SRC/app/layout/qgsreportfieldgroupsectionwidget.h \
        $$PATH_TO_QGIS_SRC/app/layout/qgsreportsectionwidget.h \
        $$PATH_TO_QGIS_SRC/app/layout/qgsreportlayoutsectionwidget.h \
        $$PATH_TO_QGIS_SRC/app/layout/qgsreportorganizerwidget.h \
        $$PATH_TO_QGIS_SRC/app/gps/qgsgpsbearingitem.h \
        $$PATH_TO_QGIS_SRC/app/gps/qgsgpsmarker.h \
        $$PATH_TO_QGIS_SRC/app/gps/qgsgpsinformationwidget.h \
        $$PATH_TO_QGIS/external/libdxfrw/intern/drw_cptable950.h \
        $$PATH_TO_QGIS/external/libdxfrw/intern/dwgreader21.h \
        $$PATH_TO_QGIS/external/libdxfrw/intern/drw_cptable932.h \
        $$PATH_TO_QGIS/external/libdxfrw/intern/dwgreader24.h \
        $$PATH_TO_QGIS/external/libdxfrw/intern/dwgreader15.h \
        $$PATH_TO_QGIS/external/libdxfrw/intern/drw_cptable936.h \
        $$PATH_TO_QGIS/external/libdxfrw/intern/dwgreader27.h \
        $$PATH_TO_QGIS/external/libdxfrw/intern/dwgreader18.h \
        $$PATH_TO_QGIS/external/libdxfrw/intern/drw_cptable949.h \
        $$PATH_TO_QGIS/external/libdxfrw/intern/rscodec.h \
        $$PATH_TO_QGIS/external/libdxfrw/intern/drw_textcodec.h \
        $$PATH_TO_QGIS/external/libdxfrw/intern/drw_dbg.h \
        $$PATH_TO_QGIS/external/libdxfrw/intern/dwgutil.h \
        $$PATH_TO_QGIS/external/libdxfrw/intern/dxfreader.h \
        $$PATH_TO_QGIS/external/libdxfrw/intern/dwgreader.h \
        $$PATH_TO_QGIS/external/libdxfrw/intern/dwgbuffer.h \
        $$PATH_TO_QGIS/external/libdxfrw/intern/dxfwriter.h \
        $$PATH_TO_QGIS/external/libdxfrw/intern/drw_cptables.h \
        $$PATH_TO_QGIS/external/libdxfrw/drw_interface.h \
        $$PATH_TO_QGIS/external/libdxfrw/drw_base.h \
        $$PATH_TO_QGIS/external/libdxfrw/drw_header.h \
        $$PATH_TO_QGIS/external/libdxfrw/libdwgr.h \
        $$PATH_TO_QGIS/external/libdxfrw/drw_entities.h \
        $$PATH_TO_QGIS/external/libdxfrw/drw_classes.h \
        $$PATH_TO_QGIS/external/libdxfrw/drw_objects.h \
        $$PATH_TO_QGIS/external/libdxfrw/libdxfrw.h \
        $$PATH_TO_QGIS/external/qt-unix-signals/sigwatch.h \


#ifdef 3d
#$$PATH_TO_QGIS_SRC/app/layout/qgslayout3dmapwidget.h \

FORMS += \
    mainwindow.ui


INCLUDEPATH +=  $$PATH_TO_QGIS_BUILD \
                $$PATH_TO_QGIS/external \
                $$PATH_TO_QGIS/external/astyle \
                $$PATH_TO_QGIS/external/inja \
                $$PATH_TO_QGIS/external/kdbush \
                $$PATH_TO_QGIS/external/nmea \
                $$PATH_TO_QGIS/external/libdxfrw \
                $$PATH_TO_QGIS/external/libdxfrw/intern \
                $$PATH_TO_QGIS/external/qt-unix-signals \
                $$PATH_TO_QGIS_BUILD/src/app \
                $$PATH_TO_QGIS_BUILD/src/ui \
                $$PATH_TO_QGIS_DEPS \
                $$PATH_TO_QGIS_DEPS \
                $$PATH_TO_QGIS_SRC/analysis \
                $$PATH_TO_QGIS_SRC/app \
                $$PATH_TO_QGIS_SRC/app/browser \
                $$PATH_TO_QGIS_SRC/app/decorations \
                $$PATH_TO_QGIS_SRC/app/devtools \
                $$PATH_TO_QGIS_SRC/app/devtools/networklogger \
                $$PATH_TO_QGIS_SRC/app/devtools/profiler \
                $$PATH_TO_QGIS_SRC/app/dwg \
                $$PATH_TO_QGIS_SRC/app/georeferencer \
                $$PATH_TO_QGIS_SRC/app/gps \
                $$PATH_TO_QGIS_SRC/app/labeling \
                $$PATH_TO_QGIS_SRC/app/layout \
                $$PATH_TO_QGIS_SRC/app/locator \
                $$PATH_TO_QGIS_SRC/app/mesh \
                $$PATH_TO_QGIS_SRC/app/maptools \
                $$PATH_TO_QGIS_SRC/app/options \
                $$PATH_TO_QGIS_SRC/app/pointcloud \
                $$PATH_TO_QGIS_SRC/app/pluginmanager \
                $$PATH_TO_QGIS_SRC/app/vectortile \
                $$PATH_TO_QGIS_SRC/core \
                $$PATH_TO_QGIS_SRC/core/labeling \
                $$PATH_TO_QGIS_SRC/core/raster \
                $$PATH_TO_QGIS_SRC/core/scalebar \
                $$PATH_TO_QGIS_SRC/gui \
                $$PATH_TO_QGIS_SRC/gui/attributetable \
                $$PATH_TO_QGIS_SRC/gui/layout \
                $$PATH_TO_QGIS_SRC/providers/arcgisrest \
                $$PATH_TO_QGIS_SRC/providers/wms \




# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target



INCLUDEPATH += $$PWD/../../../C++Libraries/QGIS/Install/include/qgis
INCLUDEPATH += $$PWD/../../../C++Libraries/QGIS/Install/include
DEPENDPATH += $$PWD/../../../C++Libraries/QGIS/Install/include

INCLUDEPATH += $$PWD/../../../../../../opt/QGIS/qgis-deps-0.8.0/stage/include/qt5keychain

#INCLUDEPATH += $$PWD/../../../../../../opt/QGIS/qgis-deps-0.8.0/stage/include


# Frameworks
QMAKE_LFLAGS += -F/opt/QGIS/qgis-deps-0.8.0/stage/lib
INCLUDEPATH += /opt/QGIS/qgis-deps-0.8.0/stage/lib/qca-qt5.framework/Headers
LIBS += -framework qca-qt5

QMAKE_LFLAGS += -F/opt/QGIS/qgis-deps-0.8.0/stage/lib
INCLUDEPATH += /opt/QGIS/qgis-deps-0.8.0/stage/lib/qwt.framework/Headers
LIBS += -framework qwt


QMAKE_LFLAGS += -F/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/System/Library/Frameworks
INCLUDEPATH += /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/System/Library/Frameworks/OpenCL.framework/Headers
LIBS += -framework opencl


#QMAKE_LFLAGS += -F/opt/QGIS/qgis-deps-0.8.0/stage/lib
#INCLUDEPATH += /opt/QGIS/qgis-deps-0.8.0/stage/lib/QtWebKit.framework/Headers
#LIBS += -framework qtwebkit

#QMAKE_LFLAGS += -F/opt/QGIS/qgis-deps-0.8.0/stage/lib
#INCLUDEPATH += /opt/QGIS/qgis-deps-0.8.0/stage/lib/QtWebKitWidgets.framework/Headers
#LIBS += -framework qtwebkitwidgets

# QGIS libs
win32:CONFIG(release, debug|release): LIBS += -L$$PWD/../../../C++Libraries/QGIS/Install/lib/release/ -lqgis_core.3.21.0
else:win32:CONFIG(debug, debug|release): LIBS += -L$$PWD/../../../C++Libraries/QGIS/Install/lib/debug/ -lqgis_core.3.21.0
else:unix: LIBS += -L$$PWD/../../../C++Libraries/QGIS/Install/lib/ -lqgis_core.3.21.0

win32:CONFIG(release, debug|release): LIBS += -L$$PWD/../../../C++Libraries/QGIS/Install/lib/release/ -lqgis_gui.3.21.0
else:win32:CONFIG(debug, debug|release): LIBS += -L$$PWD/../../../C++Libraries/QGIS/Install/lib/debug/ -lqgis_gui.3.21.0
else:unix: LIBS += -L$$PWD/../../../C++Libraries/QGIS/Install/lib/ -lqgis_gui.3.21.0 -lqgis_analysis.3.21.0

# External libs
win32:CONFIG(release, debug|release): LIBS += -L$$PWD/../../../../../../usr/local/Cellar/gdal/3.3.1_3/lib/release/ -lgdal.29
else:win32:CONFIG(debug, debug|release): LIBS += -L$$PWD/../../../../../../usr/local/Cellar/gdal/3.3.1_3/lib/debug/ -lgdal.29
else:unix: LIBS += -L$$PWD/../../../../../../usr/local/Cellar/gdal/3.3.1_3/lib/ -lgdal.29

INCLUDEPATH += $$PWD/../../../../../../usr/local/Cellar/gdal/3.3.1_3/include
DEPENDPATH += $$PWD/../../../../../../usr/local/Cellar/gdal/3.3.1_3/include

win32:CONFIG(release, debug|release): LIBS += -L$$PWD/../../../../../../usr/local/Cellar/qscintilla2/2.12.1/lib/release/ -lqscintilla2_qt5.15.0.1
else:win32:CONFIG(debug, debug|release): LIBS += -L$$PWD/../../../../../../usr/local/Cellar/qscintilla2/2.12.1/lib/debug/ -lqscintilla2_qt5.15.0.1
else:unix: LIBS += -L$$PWD/../../../../../../usr/local/Cellar/qscintilla2/2.12.1/lib/ -lqscintilla2_qt5.15.0.1

INCLUDEPATH += $$PWD/../../../../../../usr/local/Cellar/qscintilla2/2.12.1/include
DEPENDPATH += $$PWD/../../../../../../usr/local/Cellar/qscintilla2/2.12.1/include

win32:CONFIG(release, debug|release): LIBS += -L$$PWD/../../../C++Libraries/QGIS/Install/lib/release/ -lqgis_native.3.21.0
else:win32:CONFIG(debug, debug|release): LIBS += -L$$PWD/../../../C++Libraries/QGIS/Install/lib/debug/ -lqgis_native.3.21.0
else:unix: LIBS += -L$$PWD/../../../C++Libraries/QGIS/Install/lib/ -lqgis_native.3.21.0

INCLUDEPATH += $$PWD/../../../C++Libraries/QGIS/Install/include
DEPENDPATH += $$PWD/../../../C++Libraries/QGIS/Install/include

win32:CONFIG(release, debug|release): LIBS += -L$$PWD/../../../C++Libraries/QGIS/Install/lib/release/ -lqgisgrass7.3.21.0
else:win32:CONFIG(debug, debug|release): LIBS += -L$$PWD/../../../C++Libraries/QGIS/Install/lib/debug/ -lqgisgrass7.3.21.0
else:unix: LIBS += -L$$PWD/../../../C++Libraries/QGIS/Install/lib/ -lqgisgrass7.3.21.0

INCLUDEPATH += $$PWD/../../../C++Libraries/QGIS/Install/include
DEPENDPATH += $$PWD/../../../C++Libraries/QGIS/Install/include

win32:CONFIG(release, debug|release): LIBS += -L$$PWD/../../../../../../usr/local/Cellar/proj/8.1.0/lib/release/ -lproj.22
else:win32:CONFIG(debug, debug|release): LIBS += -L$$PWD/../../../../../../usr/local/Cellar/proj/8.1.0/lib/debug/ -lproj.22
else:unix: LIBS += -L$$PWD/../../../../../../usr/local/Cellar/proj/8.1.0/lib/ -lproj.22

INCLUDEPATH += $$PWD/../../../../../../usr/local/Cellar/proj/8.1.0/include
DEPENDPATH += $$PWD/../../../../../../usr/local/Cellar/proj/8.1.0/include


win32:CONFIG(release, debug|release): LIBS += -L$$PWD/../../../C++Libraries/sqlite/Install/lib/release/ -lsqlite3.0
else:win32:CONFIG(debug, debug|release): LIBS += -L$$PWD/../../../C++Libraries/sqlite/Install/lib/debug/ -lsqlite3.0
else:unix: LIBS += -L/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/lib -lsqlite3



win32:CONFIG(release, debug|release): LIBS += -L$$PWD/../../../../../../usr/local/Cellar/qtkeychain/0.12.0_1/lib/release/ -lqt5keychain.0.12.0
else:win32:CONFIG(debug, debug|release): LIBS += -L$$PWD/../../../../../../usr/local/Cellar/qtkeychain/0.12.0_1/lib/debug/ -lqt5keychain.0.12.0
else:unix: LIBS += -L$$PWD/../../../../../../usr/local/Cellar/qtkeychain/0.12.0_1/lib/ -lqt5keychain.0.12.0

INCLUDEPATH += $$PWD/../../../../../../usr/local/Cellar/qtkeychain/0.12.0_1/include
DEPENDPATH += $$PWD/../../../../../../usr/local/Cellar/qtkeychain/0.12.0_1/include
