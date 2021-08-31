#ifndef QGISVISUALIZATIONWIDGET_H
#define QGISVISUALIZATIONWIDGET_H

#include <QSplitter>

class QgisApp;
class QgsLayerTreeView;

class QGISVisualizationWidget : public QWidget
{
public:
    QGISVisualizationWidget(QWidget *parent = nullptr);
    ~QGISVisualizationWidget();

private:
    QgsLayerTreeView * layerTreeView = nullptr;
    QgisApp *qgis = nullptr;
};

#endif // QGISVISUALIZATIONWIDGET_H
