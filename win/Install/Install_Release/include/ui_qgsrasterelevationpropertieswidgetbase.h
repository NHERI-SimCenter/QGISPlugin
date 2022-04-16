/********************************************************************************
** Form generated from reading UI file 'qgsrasterelevationpropertieswidgetbase.ui'
**
** Created by: Qt User Interface Compiler version 5.15.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_QGSRASTERELEVATIONPROPERTIESWIDGETBASE_H
#define UI_QGSRASTERELEVATIONPROPERTIESWIDGETBASE_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>
#include "qgsdoublespinbox.h"
#include "qgssymbolbutton.h"
#include "raster/qgsrasterbandcombobox.h"

QT_BEGIN_NAMESPACE

class Ui_QgsRasterElevationPropertiesWidgetBase
{
public:
    QVBoxLayout *verticalLayout;
    QGroupBox *mElevationGroupBox;
    QGridLayout *gridLayout_2;
    QLabel *label_2;
    QgsDoubleSpinBox *mScaleZSpinBox;
    QgsDoubleSpinBox *mOffsetZSpinBox;
    QLabel *label_3;
    QLabel *label;
    QLabel *label_5;
    QgsRasterBandComboBox *mBandComboBox;
    QGroupBox *groupBox;
    QGridLayout *gridLayout;
    QLabel *label_4;
    QgsSymbolButton *mLineStyleButton;
    QSpacerItem *verticalSpacer;

    void setupUi(QWidget *QgsRasterElevationPropertiesWidgetBase)
    {
        if (QgsRasterElevationPropertiesWidgetBase->objectName().isEmpty())
            QgsRasterElevationPropertiesWidgetBase->setObjectName(QString::fromUtf8("QgsRasterElevationPropertiesWidgetBase"));
        QgsRasterElevationPropertiesWidgetBase->resize(400, 278);
        verticalLayout = new QVBoxLayout(QgsRasterElevationPropertiesWidgetBase);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        mElevationGroupBox = new QGroupBox(QgsRasterElevationPropertiesWidgetBase);
        mElevationGroupBox->setObjectName(QString::fromUtf8("mElevationGroupBox"));
        mElevationGroupBox->setFocusPolicy(Qt::StrongFocus);
        mElevationGroupBox->setCheckable(true);
        mElevationGroupBox->setProperty("syncGroup", QVariant(QString::fromUtf8("vectorgeneral")));
        gridLayout_2 = new QGridLayout(mElevationGroupBox);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        label_2 = new QLabel(mElevationGroupBox);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout_2->addWidget(label_2, 1, 0, 1, 1);

        mScaleZSpinBox = new QgsDoubleSpinBox(mElevationGroupBox);
        mScaleZSpinBox->setObjectName(QString::fromUtf8("mScaleZSpinBox"));
        mScaleZSpinBox->setDecimals(6);
        mScaleZSpinBox->setMinimum(0.000000000000000);
        mScaleZSpinBox->setMaximum(99999999999.000000000000000);
        mScaleZSpinBox->setValue(1.000000000000000);

        gridLayout_2->addWidget(mScaleZSpinBox, 1, 1, 1, 2);

        mOffsetZSpinBox = new QgsDoubleSpinBox(mElevationGroupBox);
        mOffsetZSpinBox->setObjectName(QString::fromUtf8("mOffsetZSpinBox"));
        mOffsetZSpinBox->setDecimals(6);
        mOffsetZSpinBox->setMinimum(-99999999999.000000000000000);
        mOffsetZSpinBox->setMaximum(99999999999.000000000000000);

        gridLayout_2->addWidget(mOffsetZSpinBox, 2, 1, 1, 2);

        label_3 = new QLabel(mElevationGroupBox);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setWordWrap(true);

        gridLayout_2->addWidget(label_3, 0, 0, 1, 3);

        label = new QLabel(mElevationGroupBox);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout_2->addWidget(label, 2, 0, 1, 1);

        label_5 = new QLabel(mElevationGroupBox);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        gridLayout_2->addWidget(label_5, 3, 0, 1, 1);

        mBandComboBox = new QgsRasterBandComboBox(mElevationGroupBox);
        mBandComboBox->setObjectName(QString::fromUtf8("mBandComboBox"));

        gridLayout_2->addWidget(mBandComboBox, 3, 1, 1, 2);


        verticalLayout->addWidget(mElevationGroupBox);

        groupBox = new QGroupBox(QgsRasterElevationPropertiesWidgetBase);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        gridLayout = new QGridLayout(groupBox);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        label_4 = new QLabel(groupBox);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        gridLayout->addWidget(label_4, 0, 0, 1, 1);

        mLineStyleButton = new QgsSymbolButton(groupBox);
        mLineStyleButton->setObjectName(QString::fromUtf8("mLineStyleButton"));
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(mLineStyleButton->sizePolicy().hasHeightForWidth());
        mLineStyleButton->setSizePolicy(sizePolicy);

        gridLayout->addWidget(mLineStyleButton, 0, 1, 1, 1);


        verticalLayout->addWidget(groupBox);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer);

        QWidget::setTabOrder(mElevationGroupBox, mScaleZSpinBox);
        QWidget::setTabOrder(mScaleZSpinBox, mOffsetZSpinBox);

        retranslateUi(QgsRasterElevationPropertiesWidgetBase);

        QMetaObject::connectSlotsByName(QgsRasterElevationPropertiesWidgetBase);
    } // setupUi

    void retranslateUi(QWidget *QgsRasterElevationPropertiesWidgetBase)
    {
        QgsRasterElevationPropertiesWidgetBase->setWindowTitle(QCoreApplication::translate("QgsRasterElevationPropertiesWidgetBase", "Raster Elevation Properties", nullptr));
        mElevationGroupBox->setTitle(QCoreApplication::translate("QgsRasterElevationPropertiesWidgetBase", "Represents Elevation Surface", nullptr));
        label_2->setText(QCoreApplication::translate("QgsRasterElevationPropertiesWidgetBase", "Scale", nullptr));
        label_3->setText(QCoreApplication::translate("QgsRasterElevationPropertiesWidgetBase", "<html><head/><body><p><span style=\" font-weight:600;\">Elevation scaling and offset can be used to manually correct elevation values from the layer.</span></p><p>The scale is applied to the raster values before adding the offset.</p></body></html>", nullptr));
        label->setText(QCoreApplication::translate("QgsRasterElevationPropertiesWidgetBase", "Offset", nullptr));
        label_5->setText(QCoreApplication::translate("QgsRasterElevationPropertiesWidgetBase", "Band", nullptr));
        groupBox->setTitle(QCoreApplication::translate("QgsRasterElevationPropertiesWidgetBase", "Profile Chart Appearance", nullptr));
        label_4->setText(QCoreApplication::translate("QgsRasterElevationPropertiesWidgetBase", "Line style", nullptr));
        mLineStyleButton->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class QgsRasterElevationPropertiesWidgetBase: public Ui_QgsRasterElevationPropertiesWidgetBase {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_QGSRASTERELEVATIONPROPERTIESWIDGETBASE_H
