/********************************************************************************
** Form generated from reading UI file 'qgsmeshcalculatordialogbase.ui'
**
** Created by: Qt User Interface Compiler version 5.15.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_QGSMESHCALCULATORDIALOGBASE_H
#define UI_QGSMESHCALCULATORDIALOGBASE_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListView>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSplitter>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>
#include "qgscollapsiblegroupbox.h"
#include "qgsdoublespinbox.h"
#include "qgsfilewidget.h"
#include "qgsmaplayercombobox.h"

QT_BEGIN_NAMESPACE

class Ui_QgsMeshCalculatorDialogBase
{
public:
    QVBoxLayout *verticalLayout_3;
    QSplitter *splitter_2;
    QSplitter *splitter;
    QGroupBox *mRasterBandsGroupBox;
    QGridLayout *gridLayout_2;
    QListView *mDatasetsListWidget;
    QGroupBox *mResultGroupBox;
    QVBoxLayout *verticalLayout_4;
    QGridLayout *gridLayout_5;
    QLabel *mOutputFormatLabel_2;
    QLabel *mOutputFormatLabel;
    QRadioButton *mOutputOnFileRadioButton;
    QgsFileWidget *mOutputDatasetFileWidget;
    QLabel *mOutputDatasetLabel;
    QComboBox *mOutputFormatComboBox;
    QRadioButton *mOutputVirtualRadioButton;
    QLineEdit *mOutputGroupNameLineEdit;
    QLabel *label_4;
    QWidget *horizontalWidget;
    QHBoxLayout *horizontalLayout_5;
    QCheckBox *useExtentCb;
    QCheckBox *useMaskCb;
    QWidget *maskBox;
    QHBoxLayout *maskBoxLayout;
    QLabel *label_3;
    QgsMapLayerComboBox *cboLayerMask;
    QWidget *extendBox;
    QGridLayout *gridLayout_3;
    QLabel *mXMinLabel;
    QgsDoubleSpinBox *mXMaxSpinBox;
    QLabel *mXMaxLabel;
    QLabel *mYMaxLabel;
    QgsDoubleSpinBox *mXMinSpinBox;
    QgsDoubleSpinBox *mYMaxSpinBox;
    QLabel *mYMinLabel;
    QgsDoubleSpinBox *mYMinSpinBox;
    QPushButton *mCurrentLayerExtentButton;
    QSpacerItem *verticalSpacer_3;
    QSpacerItem *verticalSpacer;
    QHBoxLayout *horizontalLayout_2;
    QPushButton *mAllTimesButton;
    QSpacerItem *horizontalSpacer_4;
    QGridLayout *gridLayout_4;
    QComboBox *mEndTimeComboBox;
    QLabel *label_2;
    QLabel *label;
    QSpacerItem *horizontalSpacer;
    QComboBox *mStartTimeComboBox;
    QSpacerItem *verticalSpacer_2;
    QWidget *verticalLayoutWidget;
    QVBoxLayout *verticalLayout;
    QGroupBox *groupBox;
    QVBoxLayout *verticalLayout_2;
    QgsCollapsibleGroupBox *mOperatorsGroupBox;
    QGridLayout *gridLayout;
    QPushButton *mLesserEqualButton;
    QPushButton *mGreaterEqualButton;
    QPushButton *mDividePushButton;
    QPushButton *mMultiplyPushButton;
    QPushButton *mPlusPushButton;
    QPushButton *mMaxButton;
    QPushButton *mEqualButton;
    QPushButton *mGreaterButton;
    QPushButton *mLessButton;
    QPushButton *mAbsButton;
    QPushButton *mNotEqualButton;
    QPushButton *mMinButton;
    QPushButton *mOpenBracketPushButton;
    QPushButton *mCloseBracketPushButton;
    QPushButton *mIfButton;
    QPushButton *mAndButton;
    QPushButton *mOrButton;
    QPushButton *mNotButton;
    QPushButton *mPowButton;
    QPushButton *mSumAggrButton;
    QPushButton *mMaxAggrButton;
    QPushButton *mMinAggrButton;
    QPushButton *mAverageAggrButton;
    QPushButton *mMinusPushButton;
    QPushButton *mNoDataButton;
    QTextEdit *mExpressionTextEdit;
    QLabel *mExpressionValidLabel;
    QDialogButtonBox *mButtonBox;
    QButtonGroup *buttonGroup;

    void setupUi(QDialog *QgsMeshCalculatorDialogBase)
    {
        if (QgsMeshCalculatorDialogBase->objectName().isEmpty())
            QgsMeshCalculatorDialogBase->setObjectName(QString::fromUtf8("QgsMeshCalculatorDialogBase"));
        QgsMeshCalculatorDialogBase->resize(912, 864);
        verticalLayout_3 = new QVBoxLayout(QgsMeshCalculatorDialogBase);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        splitter_2 = new QSplitter(QgsMeshCalculatorDialogBase);
        splitter_2->setObjectName(QString::fromUtf8("splitter_2"));
        splitter_2->setOrientation(Qt::Vertical);
        splitter = new QSplitter(splitter_2);
        splitter->setObjectName(QString::fromUtf8("splitter"));
        splitter->setOrientation(Qt::Horizontal);
        mRasterBandsGroupBox = new QGroupBox(splitter);
        mRasterBandsGroupBox->setObjectName(QString::fromUtf8("mRasterBandsGroupBox"));
        gridLayout_2 = new QGridLayout(mRasterBandsGroupBox);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        mDatasetsListWidget = new QListView(mRasterBandsGroupBox);
        mDatasetsListWidget->setObjectName(QString::fromUtf8("mDatasetsListWidget"));

        gridLayout_2->addWidget(mDatasetsListWidget, 0, 0, 1, 1);

        splitter->addWidget(mRasterBandsGroupBox);
        mResultGroupBox = new QGroupBox(splitter);
        mResultGroupBox->setObjectName(QString::fromUtf8("mResultGroupBox"));
        verticalLayout_4 = new QVBoxLayout(mResultGroupBox);
        verticalLayout_4->setObjectName(QString::fromUtf8("verticalLayout_4"));
        gridLayout_5 = new QGridLayout();
        gridLayout_5->setObjectName(QString::fromUtf8("gridLayout_5"));
        mOutputFormatLabel_2 = new QLabel(mResultGroupBox);
        mOutputFormatLabel_2->setObjectName(QString::fromUtf8("mOutputFormatLabel_2"));

        gridLayout_5->addWidget(mOutputFormatLabel_2, 3, 0, 1, 1);

        mOutputFormatLabel = new QLabel(mResultGroupBox);
        mOutputFormatLabel->setObjectName(QString::fromUtf8("mOutputFormatLabel"));

        gridLayout_5->addWidget(mOutputFormatLabel, 2, 0, 1, 1);

        mOutputOnFileRadioButton = new QRadioButton(mResultGroupBox);
        mOutputOnFileRadioButton->setObjectName(QString::fromUtf8("mOutputOnFileRadioButton"));
        mOutputOnFileRadioButton->setChecked(true);

        gridLayout_5->addWidget(mOutputOnFileRadioButton, 0, 1, 1, 1);

        mOutputDatasetFileWidget = new QgsFileWidget(mResultGroupBox);
        mOutputDatasetFileWidget->setObjectName(QString::fromUtf8("mOutputDatasetFileWidget"));

        gridLayout_5->addWidget(mOutputDatasetFileWidget, 1, 1, 1, 2);

        mOutputDatasetLabel = new QLabel(mResultGroupBox);
        mOutputDatasetLabel->setObjectName(QString::fromUtf8("mOutputDatasetLabel"));

        gridLayout_5->addWidget(mOutputDatasetLabel, 0, 0, 1, 1);

        mOutputFormatComboBox = new QComboBox(mResultGroupBox);
        mOutputFormatComboBox->setObjectName(QString::fromUtf8("mOutputFormatComboBox"));

        gridLayout_5->addWidget(mOutputFormatComboBox, 2, 1, 1, 2);

        mOutputVirtualRadioButton = new QRadioButton(mResultGroupBox);
        mOutputVirtualRadioButton->setObjectName(QString::fromUtf8("mOutputVirtualRadioButton"));

        gridLayout_5->addWidget(mOutputVirtualRadioButton, 0, 2, 1, 1);

        mOutputGroupNameLineEdit = new QLineEdit(mResultGroupBox);
        mOutputGroupNameLineEdit->setObjectName(QString::fromUtf8("mOutputGroupNameLineEdit"));

        gridLayout_5->addWidget(mOutputGroupNameLineEdit, 3, 1, 1, 2);

        label_4 = new QLabel(mResultGroupBox);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        gridLayout_5->addWidget(label_4, 1, 0, 1, 1);


        verticalLayout_4->addLayout(gridLayout_5);

        horizontalWidget = new QWidget(mResultGroupBox);
        horizontalWidget->setObjectName(QString::fromUtf8("horizontalWidget"));
        horizontalLayout_5 = new QHBoxLayout(horizontalWidget);
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        useExtentCb = new QCheckBox(horizontalWidget);
        buttonGroup = new QButtonGroup(QgsMeshCalculatorDialogBase);
        buttonGroup->setObjectName(QString::fromUtf8("buttonGroup"));
        buttonGroup->addButton(useExtentCb);
        useExtentCb->setObjectName(QString::fromUtf8("useExtentCb"));
        useExtentCb->setChecked(true);

        horizontalLayout_5->addWidget(useExtentCb);

        useMaskCb = new QCheckBox(horizontalWidget);
        buttonGroup->addButton(useMaskCb);
        useMaskCb->setObjectName(QString::fromUtf8("useMaskCb"));

        horizontalLayout_5->addWidget(useMaskCb);


        verticalLayout_4->addWidget(horizontalWidget);

        maskBox = new QWidget(mResultGroupBox);
        maskBox->setObjectName(QString::fromUtf8("maskBox"));
        maskBoxLayout = new QHBoxLayout(maskBox);
        maskBoxLayout->setSpacing(6);
        maskBoxLayout->setObjectName(QString::fromUtf8("maskBoxLayout"));
        maskBoxLayout->setContentsMargins(0, -1, 0, -1);
        label_3 = new QLabel(maskBox);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setMinimumSize(QSize(206, 0));

        maskBoxLayout->addWidget(label_3);

        cboLayerMask = new QgsMapLayerComboBox(maskBox);
        cboLayerMask->setObjectName(QString::fromUtf8("cboLayerMask"));
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(cboLayerMask->sizePolicy().hasHeightForWidth());
        cboLayerMask->setSizePolicy(sizePolicy);
        cboLayerMask->setEditable(false);

        maskBoxLayout->addWidget(cboLayerMask);


        verticalLayout_4->addWidget(maskBox);

        extendBox = new QWidget(mResultGroupBox);
        extendBox->setObjectName(QString::fromUtf8("extendBox"));
        QSizePolicy sizePolicy1(QSizePolicy::Minimum, QSizePolicy::Minimum);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(extendBox->sizePolicy().hasHeightForWidth());
        extendBox->setSizePolicy(sizePolicy1);
        gridLayout_3 = new QGridLayout(extendBox);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        mXMinLabel = new QLabel(extendBox);
        mXMinLabel->setObjectName(QString::fromUtf8("mXMinLabel"));

        gridLayout_3->addWidget(mXMinLabel, 1, 0, 1, 1);

        mXMaxSpinBox = new QgsDoubleSpinBox(extendBox);
        mXMaxSpinBox->setObjectName(QString::fromUtf8("mXMaxSpinBox"));
        mXMaxSpinBox->setDecimals(5);
        mXMaxSpinBox->setMinimum(-999999999.000000000000000);
        mXMaxSpinBox->setMaximum(999999999.000000000000000);

        gridLayout_3->addWidget(mXMaxSpinBox, 1, 3, 1, 1);

        mXMaxLabel = new QLabel(extendBox);
        mXMaxLabel->setObjectName(QString::fromUtf8("mXMaxLabel"));

        gridLayout_3->addWidget(mXMaxLabel, 1, 2, 1, 1);

        mYMaxLabel = new QLabel(extendBox);
        mYMaxLabel->setObjectName(QString::fromUtf8("mYMaxLabel"));

        gridLayout_3->addWidget(mYMaxLabel, 2, 2, 1, 1);

        mXMinSpinBox = new QgsDoubleSpinBox(extendBox);
        mXMinSpinBox->setObjectName(QString::fromUtf8("mXMinSpinBox"));
        mXMinSpinBox->setDecimals(5);
        mXMinSpinBox->setMinimum(-999999999.000000000000000);
        mXMinSpinBox->setMaximum(999999999.000000000000000);

        gridLayout_3->addWidget(mXMinSpinBox, 1, 1, 1, 1);

        mYMaxSpinBox = new QgsDoubleSpinBox(extendBox);
        mYMaxSpinBox->setObjectName(QString::fromUtf8("mYMaxSpinBox"));
        mYMaxSpinBox->setDecimals(5);
        mYMaxSpinBox->setMinimum(-999999999.000000000000000);
        mYMaxSpinBox->setMaximum(999999999.000000000000000);

        gridLayout_3->addWidget(mYMaxSpinBox, 2, 3, 1, 1);

        mYMinLabel = new QLabel(extendBox);
        mYMinLabel->setObjectName(QString::fromUtf8("mYMinLabel"));

        gridLayout_3->addWidget(mYMinLabel, 2, 0, 1, 1);

        mYMinSpinBox = new QgsDoubleSpinBox(extendBox);
        mYMinSpinBox->setObjectName(QString::fromUtf8("mYMinSpinBox"));
        mYMinSpinBox->setDecimals(5);
        mYMinSpinBox->setMinimum(-999999999.000000000000000);
        mYMinSpinBox->setMaximum(999999999.000000000000000);

        gridLayout_3->addWidget(mYMinSpinBox, 2, 1, 1, 1);

        mCurrentLayerExtentButton = new QPushButton(extendBox);
        mCurrentLayerExtentButton->setObjectName(QString::fromUtf8("mCurrentLayerExtentButton"));

        gridLayout_3->addWidget(mCurrentLayerExtentButton, 0, 0, 1, 2);


        verticalLayout_4->addWidget(extendBox);

        verticalSpacer_3 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_4->addItem(verticalSpacer_3);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_4->addItem(verticalSpacer);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        mAllTimesButton = new QPushButton(mResultGroupBox);
        mAllTimesButton->setObjectName(QString::fromUtf8("mAllTimesButton"));

        horizontalLayout_2->addWidget(mAllTimesButton);

        horizontalSpacer_4 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer_4);


        verticalLayout_4->addLayout(horizontalLayout_2);

        gridLayout_4 = new QGridLayout();
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        mEndTimeComboBox = new QComboBox(mResultGroupBox);
        mEndTimeComboBox->setObjectName(QString::fromUtf8("mEndTimeComboBox"));

        gridLayout_4->addWidget(mEndTimeComboBox, 2, 4, 1, 1);

        label_2 = new QLabel(mResultGroupBox);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout_4->addWidget(label_2, 2, 3, 1, 1);

        label = new QLabel(mResultGroupBox);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout_4->addWidget(label, 2, 0, 1, 1);

        horizontalSpacer = new QSpacerItem(10, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_4->addItem(horizontalSpacer, 2, 2, 1, 1);

        mStartTimeComboBox = new QComboBox(mResultGroupBox);
        mStartTimeComboBox->setObjectName(QString::fromUtf8("mStartTimeComboBox"));

        gridLayout_4->addWidget(mStartTimeComboBox, 2, 1, 1, 1);


        verticalLayout_4->addLayout(gridLayout_4);

        verticalSpacer_2 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_4->addItem(verticalSpacer_2);

        splitter->addWidget(mResultGroupBox);
        maskBox->raise();
        extendBox->raise();
        horizontalWidget->raise();
        splitter_2->addWidget(splitter);
        verticalLayoutWidget = new QWidget(splitter_2);
        verticalLayoutWidget->setObjectName(QString::fromUtf8("verticalLayoutWidget"));
        verticalLayout = new QVBoxLayout(verticalLayoutWidget);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        groupBox = new QGroupBox(verticalLayoutWidget);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        verticalLayout_2 = new QVBoxLayout(groupBox);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        verticalLayout_2->setContentsMargins(0, -1, 0, 0);
        mOperatorsGroupBox = new QgsCollapsibleGroupBox(groupBox);
        mOperatorsGroupBox->setObjectName(QString::fromUtf8("mOperatorsGroupBox"));
        gridLayout = new QGridLayout(mOperatorsGroupBox);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        gridLayout->setContentsMargins(0, -1, 0, 0);
        mLesserEqualButton = new QPushButton(mOperatorsGroupBox);
        mLesserEqualButton->setObjectName(QString::fromUtf8("mLesserEqualButton"));

        gridLayout->addWidget(mLesserEqualButton, 3, 0, 1, 1);

        mGreaterEqualButton = new QPushButton(mOperatorsGroupBox);
        mGreaterEqualButton->setObjectName(QString::fromUtf8("mGreaterEqualButton"));

        gridLayout->addWidget(mGreaterEqualButton, 3, 1, 1, 1);

        mDividePushButton = new QPushButton(mOperatorsGroupBox);
        mDividePushButton->setObjectName(QString::fromUtf8("mDividePushButton"));

        gridLayout->addWidget(mDividePushButton, 1, 1, 1, 1);

        mMultiplyPushButton = new QPushButton(mOperatorsGroupBox);
        mMultiplyPushButton->setObjectName(QString::fromUtf8("mMultiplyPushButton"));

        gridLayout->addWidget(mMultiplyPushButton, 0, 1, 1, 1);

        mPlusPushButton = new QPushButton(mOperatorsGroupBox);
        mPlusPushButton->setObjectName(QString::fromUtf8("mPlusPushButton"));

        gridLayout->addWidget(mPlusPushButton, 0, 0, 1, 1);

        mMaxButton = new QPushButton(mOperatorsGroupBox);
        mMaxButton->setObjectName(QString::fromUtf8("mMaxButton"));

        gridLayout->addWidget(mMaxButton, 1, 5, 1, 1);

        mEqualButton = new QPushButton(mOperatorsGroupBox);
        mEqualButton->setObjectName(QString::fromUtf8("mEqualButton"));

        gridLayout->addWidget(mEqualButton, 2, 4, 1, 1);

        mGreaterButton = new QPushButton(mOperatorsGroupBox);
        mGreaterButton->setObjectName(QString::fromUtf8("mGreaterButton"));

        gridLayout->addWidget(mGreaterButton, 2, 1, 1, 1);

        mLessButton = new QPushButton(mOperatorsGroupBox);
        mLessButton->setObjectName(QString::fromUtf8("mLessButton"));

        gridLayout->addWidget(mLessButton, 2, 0, 1, 1);

        mAbsButton = new QPushButton(mOperatorsGroupBox);
        mAbsButton->setObjectName(QString::fromUtf8("mAbsButton"));

        gridLayout->addWidget(mAbsButton, 2, 5, 1, 1);

        mNotEqualButton = new QPushButton(mOperatorsGroupBox);
        mNotEqualButton->setObjectName(QString::fromUtf8("mNotEqualButton"));

        gridLayout->addWidget(mNotEqualButton, 3, 4, 1, 1);

        mMinButton = new QPushButton(mOperatorsGroupBox);
        mMinButton->setObjectName(QString::fromUtf8("mMinButton"));

        gridLayout->addWidget(mMinButton, 0, 5, 1, 1);

        mOpenBracketPushButton = new QPushButton(mOperatorsGroupBox);
        mOpenBracketPushButton->setObjectName(QString::fromUtf8("mOpenBracketPushButton"));

        gridLayout->addWidget(mOpenBracketPushButton, 0, 4, 1, 1);

        mCloseBracketPushButton = new QPushButton(mOperatorsGroupBox);
        mCloseBracketPushButton->setObjectName(QString::fromUtf8("mCloseBracketPushButton"));

        gridLayout->addWidget(mCloseBracketPushButton, 1, 4, 1, 1);

        mIfButton = new QPushButton(mOperatorsGroupBox);
        mIfButton->setObjectName(QString::fromUtf8("mIfButton"));

        gridLayout->addWidget(mIfButton, 0, 6, 1, 1);

        mAndButton = new QPushButton(mOperatorsGroupBox);
        mAndButton->setObjectName(QString::fromUtf8("mAndButton"));

        gridLayout->addWidget(mAndButton, 1, 6, 1, 1);

        mOrButton = new QPushButton(mOperatorsGroupBox);
        mOrButton->setObjectName(QString::fromUtf8("mOrButton"));

        gridLayout->addWidget(mOrButton, 2, 6, 1, 1);

        mNotButton = new QPushButton(mOperatorsGroupBox);
        mNotButton->setObjectName(QString::fromUtf8("mNotButton"));

        gridLayout->addWidget(mNotButton, 3, 6, 1, 1);

        mPowButton = new QPushButton(mOperatorsGroupBox);
        mPowButton->setObjectName(QString::fromUtf8("mPowButton"));

        gridLayout->addWidget(mPowButton, 3, 5, 1, 1);

        mSumAggrButton = new QPushButton(mOperatorsGroupBox);
        mSumAggrButton->setObjectName(QString::fromUtf8("mSumAggrButton"));

        gridLayout->addWidget(mSumAggrButton, 0, 13, 1, 1);

        mMaxAggrButton = new QPushButton(mOperatorsGroupBox);
        mMaxAggrButton->setObjectName(QString::fromUtf8("mMaxAggrButton"));

        gridLayout->addWidget(mMaxAggrButton, 1, 13, 1, 1);

        mMinAggrButton = new QPushButton(mOperatorsGroupBox);
        mMinAggrButton->setObjectName(QString::fromUtf8("mMinAggrButton"));

        gridLayout->addWidget(mMinAggrButton, 2, 13, 1, 1);

        mAverageAggrButton = new QPushButton(mOperatorsGroupBox);
        mAverageAggrButton->setObjectName(QString::fromUtf8("mAverageAggrButton"));

        gridLayout->addWidget(mAverageAggrButton, 3, 13, 1, 1);

        mMinusPushButton = new QPushButton(mOperatorsGroupBox);
        mMinusPushButton->setObjectName(QString::fromUtf8("mMinusPushButton"));

        gridLayout->addWidget(mMinusPushButton, 1, 0, 1, 1);


        verticalLayout_2->addWidget(mOperatorsGroupBox);

        mNoDataButton = new QPushButton(groupBox);
        mNoDataButton->setObjectName(QString::fromUtf8("mNoDataButton"));

        verticalLayout_2->addWidget(mNoDataButton);

        mExpressionTextEdit = new QTextEdit(groupBox);
        mExpressionTextEdit->setObjectName(QString::fromUtf8("mExpressionTextEdit"));

        verticalLayout_2->addWidget(mExpressionTextEdit);


        verticalLayout->addWidget(groupBox);

        splitter_2->addWidget(verticalLayoutWidget);

        verticalLayout_3->addWidget(splitter_2);

        mExpressionValidLabel = new QLabel(QgsMeshCalculatorDialogBase);
        mExpressionValidLabel->setObjectName(QString::fromUtf8("mExpressionValidLabel"));

        verticalLayout_3->addWidget(mExpressionValidLabel);

        mButtonBox = new QDialogButtonBox(QgsMeshCalculatorDialogBase);
        mButtonBox->setObjectName(QString::fromUtf8("mButtonBox"));
        mButtonBox->setOrientation(Qt::Horizontal);
        mButtonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        verticalLayout_3->addWidget(mButtonBox);

        mButtonBox->raise();
        mExpressionValidLabel->raise();
        splitter_2->raise();
        QWidget::setTabOrder(mDatasetsListWidget, mOutputOnFileRadioButton);
        QWidget::setTabOrder(mOutputOnFileRadioButton, mOutputVirtualRadioButton);
        QWidget::setTabOrder(mOutputVirtualRadioButton, mOutputFormatComboBox);
        QWidget::setTabOrder(mOutputFormatComboBox, mOutputGroupNameLineEdit);
        QWidget::setTabOrder(mOutputGroupNameLineEdit, useExtentCb);
        QWidget::setTabOrder(useExtentCb, useMaskCb);
        QWidget::setTabOrder(useMaskCb, cboLayerMask);
        QWidget::setTabOrder(cboLayerMask, mCurrentLayerExtentButton);
        QWidget::setTabOrder(mCurrentLayerExtentButton, mXMinSpinBox);
        QWidget::setTabOrder(mXMinSpinBox, mXMaxSpinBox);
        QWidget::setTabOrder(mXMaxSpinBox, mYMinSpinBox);
        QWidget::setTabOrder(mYMinSpinBox, mYMaxSpinBox);
        QWidget::setTabOrder(mYMaxSpinBox, mAllTimesButton);
        QWidget::setTabOrder(mAllTimesButton, mStartTimeComboBox);
        QWidget::setTabOrder(mStartTimeComboBox, mEndTimeComboBox);
        QWidget::setTabOrder(mEndTimeComboBox, mPlusPushButton);
        QWidget::setTabOrder(mPlusPushButton, mMultiplyPushButton);
        QWidget::setTabOrder(mMultiplyPushButton, mOpenBracketPushButton);
        QWidget::setTabOrder(mOpenBracketPushButton, mMinButton);
        QWidget::setTabOrder(mMinButton, mIfButton);
        QWidget::setTabOrder(mIfButton, mSumAggrButton);
        QWidget::setTabOrder(mSumAggrButton, mMinusPushButton);
        QWidget::setTabOrder(mMinusPushButton, mDividePushButton);
        QWidget::setTabOrder(mDividePushButton, mCloseBracketPushButton);
        QWidget::setTabOrder(mCloseBracketPushButton, mMaxButton);
        QWidget::setTabOrder(mMaxButton, mAndButton);
        QWidget::setTabOrder(mAndButton, mMaxAggrButton);
        QWidget::setTabOrder(mMaxAggrButton, mLessButton);
        QWidget::setTabOrder(mLessButton, mGreaterButton);
        QWidget::setTabOrder(mGreaterButton, mEqualButton);
        QWidget::setTabOrder(mEqualButton, mAbsButton);
        QWidget::setTabOrder(mAbsButton, mOrButton);
        QWidget::setTabOrder(mOrButton, mMinAggrButton);
        QWidget::setTabOrder(mMinAggrButton, mLesserEqualButton);
        QWidget::setTabOrder(mLesserEqualButton, mGreaterEqualButton);
        QWidget::setTabOrder(mGreaterEqualButton, mNotEqualButton);
        QWidget::setTabOrder(mNotEqualButton, mPowButton);
        QWidget::setTabOrder(mPowButton, mNotButton);
        QWidget::setTabOrder(mNotButton, mAverageAggrButton);
        QWidget::setTabOrder(mAverageAggrButton, mNoDataButton);
        QWidget::setTabOrder(mNoDataButton, mExpressionTextEdit);

        retranslateUi(QgsMeshCalculatorDialogBase);
        QObject::connect(mButtonBox, SIGNAL(accepted()), QgsMeshCalculatorDialogBase, SLOT(accept()));
        QObject::connect(mButtonBox, SIGNAL(rejected()), QgsMeshCalculatorDialogBase, SLOT(reject()));

        QMetaObject::connectSlotsByName(QgsMeshCalculatorDialogBase);
    } // setupUi

    void retranslateUi(QDialog *QgsMeshCalculatorDialogBase)
    {
        QgsMeshCalculatorDialogBase->setWindowTitle(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "Mesh calculator", nullptr));
        mRasterBandsGroupBox->setTitle(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "Datasets", nullptr));
        mResultGroupBox->setTitle(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "Result Layer", nullptr));
        mOutputFormatLabel_2->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "Group Name", nullptr));
        mOutputFormatLabel->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "Output Format", nullptr));
        mOutputOnFileRadioButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "On File", nullptr));
        mOutputDatasetLabel->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "Output Dataset", nullptr));
        mOutputVirtualRadioButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "Virtual", nullptr));
        label_4->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "Output File", nullptr));
        useExtentCb->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "Current Extent", nullptr));
        useMaskCb->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "Mask Layer", nullptr));
        label_3->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "Mask Layer       ", nullptr));
        mXMinLabel->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "X min", nullptr));
        mXMaxLabel->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "X max", nullptr));
        mYMaxLabel->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "Y max", nullptr));
        mYMinLabel->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "Y min", nullptr));
        mCurrentLayerExtentButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "Selected Layer Extent", nullptr));
        mAllTimesButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "All Selected Dataset Times ", nullptr));
        label_2->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "End time", nullptr));
        label->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "Start time", nullptr));
        groupBox->setTitle(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "Mesh Calculator Expression", nullptr));
        mOperatorsGroupBox->setTitle(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "Operators", nullptr));
        mLesserEqualButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "<=", nullptr));
        mGreaterEqualButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", ">=", nullptr));
        mDividePushButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "/", nullptr));
        mMultiplyPushButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "*", nullptr));
        mPlusPushButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "+", nullptr));
        mMaxButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "max", nullptr));
        mEqualButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "=", nullptr));
        mGreaterButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", ">", nullptr));
        mLessButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "<", nullptr));
        mAbsButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "abs", nullptr));
        mNotEqualButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "!=", nullptr));
        mMinButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "min", nullptr));
        mOpenBracketPushButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "(", nullptr));
        mCloseBracketPushButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", ")", nullptr));
        mIfButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "IF", nullptr));
        mAndButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "AND", nullptr));
        mOrButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "OR", nullptr));
        mNotButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "NOT", nullptr));
        mPowButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "^", nullptr));
        mSumAggrButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "sum (aggr)", nullptr));
        mMaxAggrButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "max (aggr)", nullptr));
        mMinAggrButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "min (aggr)", nullptr));
        mAverageAggrButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "average (aggr)", nullptr));
        mMinusPushButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "-", nullptr));
        mNoDataButton->setText(QCoreApplication::translate("QgsMeshCalculatorDialogBase", "NODATA", nullptr));
        mExpressionValidLabel->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class QgsMeshCalculatorDialogBase: public Ui_QgsMeshCalculatorDialogBase {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_QGSMESHCALCULATORDIALOGBASE_H
