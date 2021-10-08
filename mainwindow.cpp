#include "mainwindow.h"
#include "QGISVisualizationWidget.h"

#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    visWidget = std::make_unique<QGISVisualizationWidget>(this);
    this->setCentralWidget(visWidget.get());
}

MainWindow::~MainWindow()
{
    delete ui;
}

