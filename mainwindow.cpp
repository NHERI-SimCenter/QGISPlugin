#include "mainwindow.h"
#include "QGISVisualizationWidget.h"

#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    auto visWidget = new QGISVisualizationWidget(this);
    this->setCentralWidget(visWidget);
}

MainWindow::~MainWindow()
{
    delete ui;
}

