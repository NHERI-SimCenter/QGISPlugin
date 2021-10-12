/********************************************************************************
** Form generated from reading UI file 'qgsrelationeditorconfigwidgetbase.ui'
**
** Created by: Qt User Interface Compiler version 5.15.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_QGSRELATIONEDITORCONFIGWIDGETBASE_H
#define UI_QGSRELATIONEDITORCONFIGWIDGETBASE_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_QgsRelationEditorConfigWidgetBase
{
public:
    QVBoxLayout *verticalLayout;
    QCheckBox *mRelationShowLinkCheckBox;
    QCheckBox *mRelationShowUnlinkCheckBox;
    QCheckBox *mRelationShowSaveChildEditsCheckBox;
    QCheckBox *mRelationShowAddChildCheckBox;
    QCheckBox *mRelationShowDuplicateChildFeatureCheckBox;
    QCheckBox *mRelationDeleteChildFeatureCheckBox;
    QCheckBox *mRelationShowZoomToFeatureCheckBox;

    void setupUi(QWidget *QgsRelationEditorConfigWidgetBase)
    {
        if (QgsRelationEditorConfigWidgetBase->objectName().isEmpty())
            QgsRelationEditorConfigWidgetBase->setObjectName(QString::fromUtf8("QgsRelationEditorConfigWidgetBase"));
        QgsRelationEditorConfigWidgetBase->resize(274, 215);
        verticalLayout = new QVBoxLayout(QgsRelationEditorConfigWidgetBase);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        mRelationShowLinkCheckBox = new QCheckBox(QgsRelationEditorConfigWidgetBase);
        mRelationShowLinkCheckBox->setObjectName(QString::fromUtf8("mRelationShowLinkCheckBox"));

        verticalLayout->addWidget(mRelationShowLinkCheckBox);

        mRelationShowUnlinkCheckBox = new QCheckBox(QgsRelationEditorConfigWidgetBase);
        mRelationShowUnlinkCheckBox->setObjectName(QString::fromUtf8("mRelationShowUnlinkCheckBox"));

        verticalLayout->addWidget(mRelationShowUnlinkCheckBox);

        mRelationShowSaveChildEditsCheckBox = new QCheckBox(QgsRelationEditorConfigWidgetBase);
        mRelationShowSaveChildEditsCheckBox->setObjectName(QString::fromUtf8("mRelationShowSaveChildEditsCheckBox"));

        verticalLayout->addWidget(mRelationShowSaveChildEditsCheckBox);

        mRelationShowAddChildCheckBox = new QCheckBox(QgsRelationEditorConfigWidgetBase);
        mRelationShowAddChildCheckBox->setObjectName(QString::fromUtf8("mRelationShowAddChildCheckBox"));

        verticalLayout->addWidget(mRelationShowAddChildCheckBox);

        mRelationShowDuplicateChildFeatureCheckBox = new QCheckBox(QgsRelationEditorConfigWidgetBase);
        mRelationShowDuplicateChildFeatureCheckBox->setObjectName(QString::fromUtf8("mRelationShowDuplicateChildFeatureCheckBox"));

        verticalLayout->addWidget(mRelationShowDuplicateChildFeatureCheckBox);

        mRelationDeleteChildFeatureCheckBox = new QCheckBox(QgsRelationEditorConfigWidgetBase);
        mRelationDeleteChildFeatureCheckBox->setObjectName(QString::fromUtf8("mRelationDeleteChildFeatureCheckBox"));

        verticalLayout->addWidget(mRelationDeleteChildFeatureCheckBox);

        mRelationShowZoomToFeatureCheckBox = new QCheckBox(QgsRelationEditorConfigWidgetBase);
        mRelationShowZoomToFeatureCheckBox->setObjectName(QString::fromUtf8("mRelationShowZoomToFeatureCheckBox"));

        verticalLayout->addWidget(mRelationShowZoomToFeatureCheckBox);


        retranslateUi(QgsRelationEditorConfigWidgetBase);

        QMetaObject::connectSlotsByName(QgsRelationEditorConfigWidgetBase);
    } // setupUi

    void retranslateUi(QWidget *QgsRelationEditorConfigWidgetBase)
    {
        QgsRelationEditorConfigWidgetBase->setWindowTitle(QCoreApplication::translate("QgsRelationEditorConfigWidgetBase", "Attribute Widget Relation Edit Widget", nullptr));
        mRelationShowLinkCheckBox->setText(QCoreApplication::translate("QgsRelationEditorConfigWidgetBase", "Show link button", nullptr));
        mRelationShowUnlinkCheckBox->setText(QCoreApplication::translate("QgsRelationEditorConfigWidgetBase", "Show unlink button", nullptr));
        mRelationShowSaveChildEditsCheckBox->setText(QCoreApplication::translate("QgsRelationEditorConfigWidgetBase", "Show save child layer edits button", nullptr));
        mRelationShowAddChildCheckBox->setText(QCoreApplication::translate("QgsRelationEditorConfigWidgetBase", "Add child feature", nullptr));
        mRelationShowDuplicateChildFeatureCheckBox->setText(QCoreApplication::translate("QgsRelationEditorConfigWidgetBase", "Duplicate child feature", nullptr));
        mRelationDeleteChildFeatureCheckBox->setText(QCoreApplication::translate("QgsRelationEditorConfigWidgetBase", "Delete child feature", nullptr));
        mRelationShowZoomToFeatureCheckBox->setText(QCoreApplication::translate("QgsRelationEditorConfigWidgetBase", "Zoom to child feature", nullptr));
    } // retranslateUi

};

namespace Ui {
    class QgsRelationEditorConfigWidgetBase: public Ui_QgsRelationEditorConfigWidgetBase {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_QGSRELATIONEDITORCONFIGWIDGETBASE_H
