/********************************************************************************
** Form generated from reading UI file 'qgsvectorelevationpropertieswidgetbase.ui'
**
** Created by: Qt User Interface Compiler version 5.15.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_QGSVECTORELEVATIONPROPERTIESWIDGETBASE_H
#define UI_QGSVECTORELEVATIONPROPERTIESWIDGETBASE_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>
#include "qgsdoublespinbox.h"
#include "qgspropertyoverridebutton.h"
#include "qgssymbolbutton.h"

QT_BEGIN_NAMESPACE

class Ui_QgsVectorElevationPropertiesWidgetBase
{
public:
    QVBoxLayout *verticalLayout;
    QGroupBox *mElevationGroupBox;
    QGridLayout *gridLayout_2;
    QLabel *mLabelScale;
    QLabel *mLabelClampingExplanation;
    QLabel *mOffsetLabel;
    QgsDoubleSpinBox *mOffsetZSpinBox;
    QgsDoubleSpinBox *mScaleZSpinBox;
    QgsPropertyOverrideButton *mOffsetDDBtn;
    QComboBox *mComboClamping;
    QGroupBox *mExtrusionGroupBox;
    QGridLayout *gridLayout_4;
    QFrame *line_5;
    QLabel *label_3;
    QgsDoubleSpinBox *mExtrusionSpinBox;
    QgsPropertyOverrideButton *mExtrusionDDBtn;
    QLabel *mLabelBindingExplanation_2;
    QGroupBox *mBindingGroupBox;
    QGridLayout *gridLayout_3;
    QComboBox *mComboBinding;
    QFrame *line_4;
    QLabel *mLabelBindingExplanation;
    QGroupBox *groupBox;
    QGridLayout *gridLayout;
    QgsSymbolButton *mLineStyleButton;
    QLabel *label_4;
    QLabel *label_5;
    QgsSymbolButton *mFillStyleButton;
    QLabel *label_6;
    QgsSymbolButton *mMarkerStyleButton;
    QCheckBox *mCheckRespectLayerSymbology;
    QSpacerItem *verticalSpacer;

    void setupUi(QWidget *QgsVectorElevationPropertiesWidgetBase)
    {
        if (QgsVectorElevationPropertiesWidgetBase->objectName().isEmpty())
            QgsVectorElevationPropertiesWidgetBase->setObjectName(QString::fromUtf8("QgsVectorElevationPropertiesWidgetBase"));
        QgsVectorElevationPropertiesWidgetBase->resize(555, 555);
        verticalLayout = new QVBoxLayout(QgsVectorElevationPropertiesWidgetBase);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        mElevationGroupBox = new QGroupBox(QgsVectorElevationPropertiesWidgetBase);
        mElevationGroupBox->setObjectName(QString::fromUtf8("mElevationGroupBox"));
        mElevationGroupBox->setFocusPolicy(Qt::StrongFocus);
        mElevationGroupBox->setCheckable(false);
        mElevationGroupBox->setProperty("syncGroup", QVariant(QString::fromUtf8("vectorgeneral")));
        gridLayout_2 = new QGridLayout(mElevationGroupBox);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        mLabelScale = new QLabel(mElevationGroupBox);
        mLabelScale->setObjectName(QString::fromUtf8("mLabelScale"));

        gridLayout_2->addWidget(mLabelScale, 2, 0, 1, 1);

        mLabelClampingExplanation = new QLabel(mElevationGroupBox);
        mLabelClampingExplanation->setObjectName(QString::fromUtf8("mLabelClampingExplanation"));
        mLabelClampingExplanation->setWordWrap(true);

        gridLayout_2->addWidget(mLabelClampingExplanation, 1, 0, 1, 3);

        mOffsetLabel = new QLabel(mElevationGroupBox);
        mOffsetLabel->setObjectName(QString::fromUtf8("mOffsetLabel"));

        gridLayout_2->addWidget(mOffsetLabel, 3, 0, 1, 1);

        mOffsetZSpinBox = new QgsDoubleSpinBox(mElevationGroupBox);
        mOffsetZSpinBox->setObjectName(QString::fromUtf8("mOffsetZSpinBox"));
        mOffsetZSpinBox->setDecimals(6);
        mOffsetZSpinBox->setMinimum(-99999999999.000000000000000);
        mOffsetZSpinBox->setMaximum(99999999999.000000000000000);

        gridLayout_2->addWidget(mOffsetZSpinBox, 3, 1, 1, 2);

        mScaleZSpinBox = new QgsDoubleSpinBox(mElevationGroupBox);
        mScaleZSpinBox->setObjectName(QString::fromUtf8("mScaleZSpinBox"));
        mScaleZSpinBox->setDecimals(6);
        mScaleZSpinBox->setMinimum(0.000000000000000);
        mScaleZSpinBox->setMaximum(99999999999.000000000000000);
        mScaleZSpinBox->setValue(1.000000000000000);

        gridLayout_2->addWidget(mScaleZSpinBox, 2, 1, 1, 2);

        mOffsetDDBtn = new QgsPropertyOverrideButton(mElevationGroupBox);
        mOffsetDDBtn->setObjectName(QString::fromUtf8("mOffsetDDBtn"));

        gridLayout_2->addWidget(mOffsetDDBtn, 3, 3, 1, 1);

        mComboClamping = new QComboBox(mElevationGroupBox);
        mComboClamping->setObjectName(QString::fromUtf8("mComboClamping"));

        gridLayout_2->addWidget(mComboClamping, 0, 0, 1, 4);

        gridLayout_2->setColumnStretch(1, 1);

        verticalLayout->addWidget(mElevationGroupBox);

        mExtrusionGroupBox = new QGroupBox(QgsVectorElevationPropertiesWidgetBase);
        mExtrusionGroupBox->setObjectName(QString::fromUtf8("mExtrusionGroupBox"));
        mExtrusionGroupBox->setFocusPolicy(Qt::StrongFocus);
        mExtrusionGroupBox->setCheckable(true);
        mExtrusionGroupBox->setProperty("syncGroup", QVariant(QString::fromUtf8("vectorgeneral")));
        gridLayout_4 = new QGridLayout(mExtrusionGroupBox);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        line_5 = new QFrame(mExtrusionGroupBox);
        line_5->setObjectName(QString::fromUtf8("line_5"));
        line_5->setFrameShape(QFrame::VLine);
        line_5->setFrameShadow(QFrame::Sunken);

        gridLayout_4->addWidget(line_5, 3, 0, 1, 1);

        label_3 = new QLabel(mExtrusionGroupBox);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        gridLayout_4->addWidget(label_3, 1, 0, 1, 1);

        mExtrusionSpinBox = new QgsDoubleSpinBox(mExtrusionGroupBox);
        mExtrusionSpinBox->setObjectName(QString::fromUtf8("mExtrusionSpinBox"));
        mExtrusionSpinBox->setDecimals(6);
        mExtrusionSpinBox->setMinimum(-99999999999.000000000000000);
        mExtrusionSpinBox->setMaximum(99999999999.000000000000000);

        gridLayout_4->addWidget(mExtrusionSpinBox, 1, 1, 1, 1);

        mExtrusionDDBtn = new QgsPropertyOverrideButton(mExtrusionGroupBox);
        mExtrusionDDBtn->setObjectName(QString::fromUtf8("mExtrusionDDBtn"));

        gridLayout_4->addWidget(mExtrusionDDBtn, 1, 2, 1, 1);

        mLabelBindingExplanation_2 = new QLabel(mExtrusionGroupBox);
        mLabelBindingExplanation_2->setObjectName(QString::fromUtf8("mLabelBindingExplanation_2"));
        mLabelBindingExplanation_2->setTextFormat(Qt::PlainText);
        mLabelBindingExplanation_2->setWordWrap(true);

        gridLayout_4->addWidget(mLabelBindingExplanation_2, 0, 0, 1, 3);


        verticalLayout->addWidget(mExtrusionGroupBox);

        mBindingGroupBox = new QGroupBox(QgsVectorElevationPropertiesWidgetBase);
        mBindingGroupBox->setObjectName(QString::fromUtf8("mBindingGroupBox"));
        mBindingGroupBox->setFocusPolicy(Qt::StrongFocus);
        mBindingGroupBox->setCheckable(false);
        mBindingGroupBox->setProperty("syncGroup", QVariant(QString::fromUtf8("vectorgeneral")));
        gridLayout_3 = new QGridLayout(mBindingGroupBox);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        mComboBinding = new QComboBox(mBindingGroupBox);
        mComboBinding->setObjectName(QString::fromUtf8("mComboBinding"));

        gridLayout_3->addWidget(mComboBinding, 0, 0, 1, 2);

        line_4 = new QFrame(mBindingGroupBox);
        line_4->setObjectName(QString::fromUtf8("line_4"));
        line_4->setFrameShape(QFrame::VLine);
        line_4->setFrameShadow(QFrame::Sunken);

        gridLayout_3->addWidget(line_4, 2, 0, 1, 1);

        mLabelBindingExplanation = new QLabel(mBindingGroupBox);
        mLabelBindingExplanation->setObjectName(QString::fromUtf8("mLabelBindingExplanation"));
        mLabelBindingExplanation->setWordWrap(true);

        gridLayout_3->addWidget(mLabelBindingExplanation, 1, 0, 1, 2);


        verticalLayout->addWidget(mBindingGroupBox);

        groupBox = new QGroupBox(QgsVectorElevationPropertiesWidgetBase);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        gridLayout = new QGridLayout(groupBox);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        mLineStyleButton = new QgsSymbolButton(groupBox);
        mLineStyleButton->setObjectName(QString::fromUtf8("mLineStyleButton"));
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(mLineStyleButton->sizePolicy().hasHeightForWidth());
        mLineStyleButton->setSizePolicy(sizePolicy);

        gridLayout->addWidget(mLineStyleButton, 2, 1, 1, 1);

        label_4 = new QLabel(groupBox);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        gridLayout->addWidget(label_4, 2, 0, 1, 1);

        label_5 = new QLabel(groupBox);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        gridLayout->addWidget(label_5, 1, 0, 1, 1);

        mFillStyleButton = new QgsSymbolButton(groupBox);
        mFillStyleButton->setObjectName(QString::fromUtf8("mFillStyleButton"));
        sizePolicy.setHeightForWidth(mFillStyleButton->sizePolicy().hasHeightForWidth());
        mFillStyleButton->setSizePolicy(sizePolicy);

        gridLayout->addWidget(mFillStyleButton, 3, 1, 1, 1);

        label_6 = new QLabel(groupBox);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        gridLayout->addWidget(label_6, 3, 0, 1, 1);

        mMarkerStyleButton = new QgsSymbolButton(groupBox);
        mMarkerStyleButton->setObjectName(QString::fromUtf8("mMarkerStyleButton"));
        sizePolicy.setHeightForWidth(mMarkerStyleButton->sizePolicy().hasHeightForWidth());
        mMarkerStyleButton->setSizePolicy(sizePolicy);

        gridLayout->addWidget(mMarkerStyleButton, 1, 1, 1, 1);

        mCheckRespectLayerSymbology = new QCheckBox(groupBox);
        mCheckRespectLayerSymbology->setObjectName(QString::fromUtf8("mCheckRespectLayerSymbology"));

        gridLayout->addWidget(mCheckRespectLayerSymbology, 0, 0, 1, 2);


        verticalLayout->addWidget(groupBox);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer);

        QWidget::setTabOrder(mElevationGroupBox, mComboClamping);
        QWidget::setTabOrder(mComboClamping, mScaleZSpinBox);
        QWidget::setTabOrder(mScaleZSpinBox, mOffsetZSpinBox);
        QWidget::setTabOrder(mOffsetZSpinBox, mOffsetDDBtn);
        QWidget::setTabOrder(mOffsetDDBtn, mExtrusionGroupBox);
        QWidget::setTabOrder(mExtrusionGroupBox, mExtrusionSpinBox);
        QWidget::setTabOrder(mExtrusionSpinBox, mExtrusionDDBtn);
        QWidget::setTabOrder(mExtrusionDDBtn, mBindingGroupBox);
        QWidget::setTabOrder(mBindingGroupBox, mComboBinding);
        QWidget::setTabOrder(mComboBinding, mCheckRespectLayerSymbology);
        QWidget::setTabOrder(mCheckRespectLayerSymbology, mMarkerStyleButton);
        QWidget::setTabOrder(mMarkerStyleButton, mLineStyleButton);
        QWidget::setTabOrder(mLineStyleButton, mFillStyleButton);

        retranslateUi(QgsVectorElevationPropertiesWidgetBase);

        QMetaObject::connectSlotsByName(QgsVectorElevationPropertiesWidgetBase);
    } // setupUi

    void retranslateUi(QWidget *QgsVectorElevationPropertiesWidgetBase)
    {
        QgsVectorElevationPropertiesWidgetBase->setWindowTitle(QCoreApplication::translate("QgsVectorElevationPropertiesWidgetBase", "Vector Elevation Properties", nullptr));
        mElevationGroupBox->setTitle(QCoreApplication::translate("QgsVectorElevationPropertiesWidgetBase", "Elevation Clamping", nullptr));
        mLabelScale->setText(QCoreApplication::translate("QgsVectorElevationPropertiesWidgetBase", "Scale", nullptr));
        mLabelClampingExplanation->setText(QString());
        mOffsetLabel->setText(QCoreApplication::translate("QgsVectorElevationPropertiesWidgetBase", "Offset", nullptr));
        mOffsetDDBtn->setText(QCoreApplication::translate("QgsVectorElevationPropertiesWidgetBase", "\342\200\246", nullptr));
        mExtrusionGroupBox->setTitle(QCoreApplication::translate("QgsVectorElevationPropertiesWidgetBase", "Enable Extrusion", nullptr));
        label_3->setText(QCoreApplication::translate("QgsVectorElevationPropertiesWidgetBase", "Height", nullptr));
        mExtrusionDDBtn->setText(QCoreApplication::translate("QgsVectorElevationPropertiesWidgetBase", "\342\200\246", nullptr));
        mLabelBindingExplanation_2->setText(QCoreApplication::translate("QgsVectorElevationPropertiesWidgetBase", "Extrusion controls how high features extend vertically above their base.", nullptr));
        mBindingGroupBox->setTitle(QCoreApplication::translate("QgsVectorElevationPropertiesWidgetBase", "Elevation Binding", nullptr));
        mLabelBindingExplanation->setText(QString());
        groupBox->setTitle(QCoreApplication::translate("QgsVectorElevationPropertiesWidgetBase", "Profile Chart Appearance", nullptr));
        mLineStyleButton->setText(QString());
        label_4->setText(QCoreApplication::translate("QgsVectorElevationPropertiesWidgetBase", "Line style", nullptr));
        label_5->setText(QCoreApplication::translate("QgsVectorElevationPropertiesWidgetBase", "Marker style", nullptr));
        mFillStyleButton->setText(QString());
        label_6->setText(QCoreApplication::translate("QgsVectorElevationPropertiesWidgetBase", "Fill style", nullptr));
        mMarkerStyleButton->setText(QString());
#if QT_CONFIG(tooltip)
        mCheckRespectLayerSymbology->setToolTip(QCoreApplication::translate("QgsVectorElevationPropertiesWidgetBase", "If checked, then features will be shown in profile charts using the same symbols or colors as they use on 2D maps.", nullptr));
#endif // QT_CONFIG(tooltip)
        mCheckRespectLayerSymbology->setText(QCoreApplication::translate("QgsVectorElevationPropertiesWidgetBase", "Respect layer's symbology", nullptr));
    } // retranslateUi

};

namespace Ui {
    class QgsVectorElevationPropertiesWidgetBase: public Ui_QgsVectorElevationPropertiesWidgetBase {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_QGSVECTORELEVATIONPROPERTIESWIDGETBASE_H
