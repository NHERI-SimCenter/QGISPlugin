#include "QGISVisualizationWidget.h"
#include "qgsuserprofilemanager.h"
#include "qgslayertreeview.h"
#include "qgisapp.h"

#include <QStandardPaths>
#include <QSplitter>

QGISVisualizationWidget::QGISVisualizationWidget(QWidget *parent) : QWidget(parent)
{
    bool mySkipVersionCheck = true;
    bool myRestorePlugins = true;
    auto profileName = QLatin1String( "default" );
    auto configLocalStorageLocation = QStandardPaths::standardLocations( QStandardPaths::AppDataLocation ).value( 0 );
    QString rootProfileFolder = QgsUserProfileManager::resolveProfilesFolder( configLocalStorageLocation );

    qgis = new QgisApp(nullptr, myRestorePlugins, mySkipVersionCheck, rootProfileFolder, profileName, nullptr, Qt::Widget);
    qgis->setObjectName( QStringLiteral( "QgisApp" ) );

    qgis->setVisible(true);

    qgis->setSizePolicy(QSizePolicy::Expanding,QSizePolicy::Expanding);

    QHBoxLayout* thisLayout = new QHBoxLayout(this);

    layerTreeView = qgis->layerTreeView();

    thisLayout->addWidget(layerTreeView);
    thisLayout->addWidget(qgis);

    this->setSizePolicy(QSizePolicy::Expanding,QSizePolicy::Expanding);

}

QGISVisualizationWidget::~QGISVisualizationWidget()
{
    delete qgis;

}
