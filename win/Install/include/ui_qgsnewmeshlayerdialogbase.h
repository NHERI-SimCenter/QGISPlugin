/********************************************************************************
** Form generated from reading UI file 'qgsnewmeshlayerdialogbase.ui'
**
** Created by: Qt User Interface Compiler version 5.15.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_QGSNEWMESHLAYERDIALOGBASE_H
#define UI_QGSNEWMESHLAYERDIALOGBASE_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QTextBrowser>
#include <qgsmaplayercombobox.h>
#include <qgsprojectionselectionwidget.h>
#include "qgsfilewidget.h"

QT_BEGIN_NAMESPACE

class Ui_QgsNewMeshLayerDialogBase
{
public:
    QGridLayout *gridLayout1;
    QLabel *label_3;
    QLineEdit *mLayerNameLineEdit;
    QLabel *label_2;
    QgsFileWidget *mFileWidget;
    QLabel *label;
    QComboBox *mFormatComboBox;
    QgsProjectionSelectionWidget *mProjectionSelectionWidget;
    QGroupBox *groupBox;
    QGridLayout *gridLayout;
    QRadioButton *mMeshFileRadioButton;
    QRadioButton *mMeshProjectRadioButton;
    QRadioButton *mEmptyMeshRadioButton;
    QgsFileWidget *mMeshFromFileWidget;
    QgsMapLayerComboBox *mMeshProjectComboBox;
    QTextBrowser *mInformationTextBrowser;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *QgsNewMeshLayerDialogBase)
    {
        if (QgsNewMeshLayerDialogBase->objectName().isEmpty())
            QgsNewMeshLayerDialogBase->setObjectName(QString::fromUtf8("QgsNewMeshLayerDialogBase"));
        QgsNewMeshLayerDialogBase->resize(477, 450);
        gridLayout1 = new QGridLayout(QgsNewMeshLayerDialogBase);
        gridLayout1->setObjectName(QString::fromUtf8("gridLayout1"));
        label_3 = new QLabel(QgsNewMeshLayerDialogBase);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        gridLayout1->addWidget(label_3, 0, 0, 1, 1);

        mLayerNameLineEdit = new QLineEdit(QgsNewMeshLayerDialogBase);
        mLayerNameLineEdit->setObjectName(QString::fromUtf8("mLayerNameLineEdit"));

        gridLayout1->addWidget(mLayerNameLineEdit, 0, 1, 1, 1);

        label_2 = new QLabel(QgsNewMeshLayerDialogBase);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout1->addWidget(label_2, 1, 0, 1, 1);

        mFileWidget = new QgsFileWidget(QgsNewMeshLayerDialogBase);
        mFileWidget->setObjectName(QString::fromUtf8("mFileWidget"));

        gridLayout1->addWidget(mFileWidget, 1, 1, 1, 1);

        label = new QLabel(QgsNewMeshLayerDialogBase);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout1->addWidget(label, 2, 0, 1, 1);

        mFormatComboBox = new QComboBox(QgsNewMeshLayerDialogBase);
        mFormatComboBox->setObjectName(QString::fromUtf8("mFormatComboBox"));

        gridLayout1->addWidget(mFormatComboBox, 2, 1, 1, 1);

        mProjectionSelectionWidget = new QgsProjectionSelectionWidget(QgsNewMeshLayerDialogBase);
        mProjectionSelectionWidget->setObjectName(QString::fromUtf8("mProjectionSelectionWidget"));

        gridLayout1->addWidget(mProjectionSelectionWidget, 3, 1, 1, 1);

        groupBox = new QGroupBox(QgsNewMeshLayerDialogBase);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(groupBox->sizePolicy().hasHeightForWidth());
        groupBox->setSizePolicy(sizePolicy);
        gridLayout = new QGridLayout(groupBox);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        gridLayout->setContentsMargins(0, 0, 0, 0);
        mMeshFileRadioButton = new QRadioButton(groupBox);
        mMeshFileRadioButton->setObjectName(QString::fromUtf8("mMeshFileRadioButton"));

        gridLayout->addWidget(mMeshFileRadioButton, 2, 0, 1, 1);

        mMeshProjectRadioButton = new QRadioButton(groupBox);
        mMeshProjectRadioButton->setObjectName(QString::fromUtf8("mMeshProjectRadioButton"));

        gridLayout->addWidget(mMeshProjectRadioButton, 1, 0, 1, 1);

        mEmptyMeshRadioButton = new QRadioButton(groupBox);
        mEmptyMeshRadioButton->setObjectName(QString::fromUtf8("mEmptyMeshRadioButton"));
        mEmptyMeshRadioButton->setChecked(true);

        gridLayout->addWidget(mEmptyMeshRadioButton, 0, 0, 1, 1);

        mMeshFromFileWidget = new QgsFileWidget(groupBox);
        mMeshFromFileWidget->setObjectName(QString::fromUtf8("mMeshFromFileWidget"));

        gridLayout->addWidget(mMeshFromFileWidget, 2, 1, 1, 1);

        mMeshProjectComboBox = new QgsMapLayerComboBox(groupBox);
        mMeshProjectComboBox->setObjectName(QString::fromUtf8("mMeshProjectComboBox"));

        gridLayout->addWidget(mMeshProjectComboBox, 1, 1, 1, 1);

        mInformationTextBrowser = new QTextBrowser(groupBox);
        mInformationTextBrowser->setObjectName(QString::fromUtf8("mInformationTextBrowser"));

        gridLayout->addWidget(mInformationTextBrowser, 3, 0, 1, 2);


        gridLayout1->addWidget(groupBox, 4, 0, 1, 2);

        buttonBox = new QDialogButtonBox(QgsNewMeshLayerDialogBase);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Help|QDialogButtonBox::Ok);

        gridLayout1->addWidget(buttonBox, 5, 0, 1, 2);

        QWidget::setTabOrder(mLayerNameLineEdit, mFormatComboBox);
        QWidget::setTabOrder(mFormatComboBox, mEmptyMeshRadioButton);
        QWidget::setTabOrder(mEmptyMeshRadioButton, mMeshProjectRadioButton);
        QWidget::setTabOrder(mMeshProjectRadioButton, mMeshProjectComboBox);
        QWidget::setTabOrder(mMeshProjectComboBox, mMeshFileRadioButton);
        QWidget::setTabOrder(mMeshFileRadioButton, mInformationTextBrowser);

        retranslateUi(QgsNewMeshLayerDialogBase);
        QObject::connect(buttonBox, SIGNAL(accepted()), QgsNewMeshLayerDialogBase, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), QgsNewMeshLayerDialogBase, SLOT(reject()));

        QMetaObject::connectSlotsByName(QgsNewMeshLayerDialogBase);
    } // setupUi

    void retranslateUi(QDialog *QgsNewMeshLayerDialogBase)
    {
        QgsNewMeshLayerDialogBase->setWindowTitle(QCoreApplication::translate("QgsNewMeshLayerDialogBase", "New Mesh Layer", nullptr));
        label_3->setText(QCoreApplication::translate("QgsNewMeshLayerDialogBase", "Layer name", nullptr));
        mLayerNameLineEdit->setText(QCoreApplication::translate("QgsNewMeshLayerDialogBase", "New mesh layer", nullptr));
        label_2->setText(QCoreApplication::translate("QgsNewMeshLayerDialogBase", "File name", nullptr));
        label->setText(QCoreApplication::translate("QgsNewMeshLayerDialogBase", "File format", nullptr));
        groupBox->setTitle(QCoreApplication::translate("QgsNewMeshLayerDialogBase", "Initialize Mesh Using", nullptr));
        mMeshFileRadioButton->setText(QCoreApplication::translate("QgsNewMeshLayerDialogBase", "Mesh from file", nullptr));
        mMeshProjectRadioButton->setText(QCoreApplication::translate("QgsNewMeshLayerDialogBase", "Mesh from the current project", nullptr));
        mEmptyMeshRadioButton->setText(QCoreApplication::translate("QgsNewMeshLayerDialogBase", "Empty mesh", nullptr));
    } // retranslateUi

};

namespace Ui {
    class QgsNewMeshLayerDialogBase: public Ui_QgsNewMeshLayerDialogBase {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_QGSNEWMESHLAYERDIALOGBASE_H
