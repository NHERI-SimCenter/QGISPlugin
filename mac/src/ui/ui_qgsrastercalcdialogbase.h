/********************************************************************************
** Form generated from reading UI file 'qgsrastercalcdialogbase.ui'
**
** Created by: Qt User Interface Compiler version 5.15.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_QGSRASTERCALCDIALOGBASE_H
#define UI_QGSRASTERCALCDIALOGBASE_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSplitter>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>
#include "qgscollapsiblegroupbox.h"
#include "qgsdoublespinbox.h"
#include "qgsfilewidget.h"
#include "qgsprojectionselectionwidget.h"
#include "qgsspinbox.h"

QT_BEGIN_NAMESPACE

class Ui_QgsRasterCalcDialogBase
{
public:
    QVBoxLayout *verticalLayout_3;
    QSplitter *splitter_2;
    QSplitter *splitter;
    QGroupBox *mRasterBandsGroupBox;
    QGridLayout *gridLayout_2;
    QListWidget *mRasterBandsListWidget;
    QGroupBox *mResultGroupBox;
    QGridLayout *gridLayout_4;
    QGridLayout *gridLayout_3;
    QLabel *mRowsLabel;
    QgsSpinBox *mNRowsSpinBox;
    QgsDoubleSpinBox *mYMinSpinBox;
    QLabel *mYMinLabel;
    QLabel *mXMinLabel;
    QLabel *mXMaxLabel;
    QLabel *mColumnsLabel;
    QgsSpinBox *mNColumnsSpinBox;
    QLabel *mYMaxLabel;
    QgsDoubleSpinBox *mYMaxSpinBox;
    QgsDoubleSpinBox *mXMinSpinBox;
    QgsDoubleSpinBox *mXMaxSpinBox;
    QSpacerItem *horizontalSpacer_2;
    QgsFileWidget *mOutputLayer;
    QLabel *mOutputFormatLabel;
    QPushButton *mCurrentLayerExtentButton;
    QLabel *mOutputLayerLabel;
    QCheckBox *mAddResultToProjectCheckBox;
    QComboBox *mOutputFormatComboBox;
    QSpacerItem *verticalSpacer;
    QLabel *label;
    QgsProjectionSelectionWidget *mCrsSelector;
    QSpacerItem *verticalSpacer_2;
    QWidget *verticalLayoutWidget;
    QVBoxLayout *verticalLayout;
    QgsCollapsibleGroupBox *mOperatorsGroupBox;
    QGridLayout *gridLayout;
    QPushButton *mOrButton;
    QPushButton *mLnButton;
    QPushButton *mLesserEqualButton;
    QPushButton *mAndButton;
    QPushButton *mLogButton;
    QPushButton *mLessButton;
    QPushButton *mGreaterEqualButton;
    QPushButton *mTanButton;
    QPushButton *mPlusPushButton;
    QPushButton *mMultiplyPushButton;
    QPushButton *mCosButton;
    QPushButton *mGreaterButton;
    QSpacerItem *horizontalSpacer_3;
    QPushButton *mATanButton;
    QPushButton *mACosButton;
    QPushButton *mASinButton;
    QPushButton *mNotEqualButton;
    QPushButton *mCloseBracketPushButton;
    QPushButton *mEqualButton;
    QPushButton *mMinusPushButton;
    QPushButton *mOpenBracketPushButton;
    QPushButton *mDividePushButton;
    QPushButton *mExpButton;
    QPushButton *mSinButton;
    QPushButton *mSqrtButton;
    QPushButton *mAbsButton;
    QPushButton *mMinButton;
    QPushButton *mMaxButton;
    QGroupBox *groupBox;
    QVBoxLayout *verticalLayout_2;
    QTextEdit *mExpressionTextEdit;
    QLabel *mExpressionValidLabel;
    QDialogButtonBox *mButtonBox;

    void setupUi(QDialog *QgsRasterCalcDialogBase)
    {
        if (QgsRasterCalcDialogBase->objectName().isEmpty())
            QgsRasterCalcDialogBase->setObjectName(QString::fromUtf8("QgsRasterCalcDialogBase"));
        QgsRasterCalcDialogBase->resize(756, 644);
        verticalLayout_3 = new QVBoxLayout(QgsRasterCalcDialogBase);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        splitter_2 = new QSplitter(QgsRasterCalcDialogBase);
        splitter_2->setObjectName(QString::fromUtf8("splitter_2"));
        splitter_2->setOrientation(Qt::Vertical);
        splitter = new QSplitter(splitter_2);
        splitter->setObjectName(QString::fromUtf8("splitter"));
        splitter->setOrientation(Qt::Horizontal);
        mRasterBandsGroupBox = new QGroupBox(splitter);
        mRasterBandsGroupBox->setObjectName(QString::fromUtf8("mRasterBandsGroupBox"));
        gridLayout_2 = new QGridLayout(mRasterBandsGroupBox);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        mRasterBandsListWidget = new QListWidget(mRasterBandsGroupBox);
        mRasterBandsListWidget->setObjectName(QString::fromUtf8("mRasterBandsListWidget"));

        gridLayout_2->addWidget(mRasterBandsListWidget, 0, 0, 1, 1);

        splitter->addWidget(mRasterBandsGroupBox);
        mResultGroupBox = new QGroupBox(splitter);
        mResultGroupBox->setObjectName(QString::fromUtf8("mResultGroupBox"));
        gridLayout_4 = new QGridLayout(mResultGroupBox);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        gridLayout_3 = new QGridLayout();
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        mRowsLabel = new QLabel(mResultGroupBox);
        mRowsLabel->setObjectName(QString::fromUtf8("mRowsLabel"));

        gridLayout_3->addWidget(mRowsLabel, 3, 3, 1, 1);

        mNRowsSpinBox = new QgsSpinBox(mResultGroupBox);
        mNRowsSpinBox->setObjectName(QString::fromUtf8("mNRowsSpinBox"));
        mNRowsSpinBox->setMaximum(999999999);

        gridLayout_3->addWidget(mNRowsSpinBox, 3, 4, 1, 1);

        mYMinSpinBox = new QgsDoubleSpinBox(mResultGroupBox);
        mYMinSpinBox->setObjectName(QString::fromUtf8("mYMinSpinBox"));
        mYMinSpinBox->setDecimals(5);
        mYMinSpinBox->setMinimum(-999999999.000000000000000);
        mYMinSpinBox->setMaximum(999999999.000000000000000);

        gridLayout_3->addWidget(mYMinSpinBox, 2, 1, 1, 1);

        mYMinLabel = new QLabel(mResultGroupBox);
        mYMinLabel->setObjectName(QString::fromUtf8("mYMinLabel"));

        gridLayout_3->addWidget(mYMinLabel, 2, 0, 1, 1);

        mXMinLabel = new QLabel(mResultGroupBox);
        mXMinLabel->setObjectName(QString::fromUtf8("mXMinLabel"));

        gridLayout_3->addWidget(mXMinLabel, 1, 0, 1, 1);

        mXMaxLabel = new QLabel(mResultGroupBox);
        mXMaxLabel->setObjectName(QString::fromUtf8("mXMaxLabel"));

        gridLayout_3->addWidget(mXMaxLabel, 1, 3, 1, 1);

        mColumnsLabel = new QLabel(mResultGroupBox);
        mColumnsLabel->setObjectName(QString::fromUtf8("mColumnsLabel"));

        gridLayout_3->addWidget(mColumnsLabel, 3, 0, 1, 1);

        mNColumnsSpinBox = new QgsSpinBox(mResultGroupBox);
        mNColumnsSpinBox->setObjectName(QString::fromUtf8("mNColumnsSpinBox"));
        mNColumnsSpinBox->setMaximum(999999999);

        gridLayout_3->addWidget(mNColumnsSpinBox, 3, 1, 1, 1);

        mYMaxLabel = new QLabel(mResultGroupBox);
        mYMaxLabel->setObjectName(QString::fromUtf8("mYMaxLabel"));

        gridLayout_3->addWidget(mYMaxLabel, 2, 3, 1, 1);

        mYMaxSpinBox = new QgsDoubleSpinBox(mResultGroupBox);
        mYMaxSpinBox->setObjectName(QString::fromUtf8("mYMaxSpinBox"));
        mYMaxSpinBox->setDecimals(5);
        mYMaxSpinBox->setMinimum(-999999999.000000000000000);
        mYMaxSpinBox->setMaximum(999999999.000000000000000);

        gridLayout_3->addWidget(mYMaxSpinBox, 2, 4, 1, 1);

        mXMinSpinBox = new QgsDoubleSpinBox(mResultGroupBox);
        mXMinSpinBox->setObjectName(QString::fromUtf8("mXMinSpinBox"));
        mXMinSpinBox->setDecimals(5);
        mXMinSpinBox->setMinimum(-999999999.000000000000000);
        mXMinSpinBox->setMaximum(999999999.000000000000000);

        gridLayout_3->addWidget(mXMinSpinBox, 1, 1, 1, 1);

        mXMaxSpinBox = new QgsDoubleSpinBox(mResultGroupBox);
        mXMaxSpinBox->setObjectName(QString::fromUtf8("mXMaxSpinBox"));
        mXMaxSpinBox->setDecimals(5);
        mXMaxSpinBox->setMinimum(-999999999.000000000000000);
        mXMaxSpinBox->setMaximum(999999999.000000000000000);

        gridLayout_3->addWidget(mXMaxSpinBox, 1, 4, 1, 1);

        horizontalSpacer_2 = new QSpacerItem(10, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_3->addItem(horizontalSpacer_2, 1, 2, 1, 1);


        gridLayout_4->addLayout(gridLayout_3, 3, 0, 1, 4);

        mOutputLayer = new QgsFileWidget(mResultGroupBox);
        mOutputLayer->setObjectName(QString::fromUtf8("mOutputLayer"));

        gridLayout_4->addWidget(mOutputLayer, 0, 1, 1, 3);

        mOutputFormatLabel = new QLabel(mResultGroupBox);
        mOutputFormatLabel->setObjectName(QString::fromUtf8("mOutputFormatLabel"));

        gridLayout_4->addWidget(mOutputFormatLabel, 1, 0, 1, 1);

        mCurrentLayerExtentButton = new QPushButton(mResultGroupBox);
        mCurrentLayerExtentButton->setObjectName(QString::fromUtf8("mCurrentLayerExtentButton"));

        gridLayout_4->addWidget(mCurrentLayerExtentButton, 2, 0, 1, 1);

        mOutputLayerLabel = new QLabel(mResultGroupBox);
        mOutputLayerLabel->setObjectName(QString::fromUtf8("mOutputLayerLabel"));

        gridLayout_4->addWidget(mOutputLayerLabel, 0, 0, 1, 1);

        mAddResultToProjectCheckBox = new QCheckBox(mResultGroupBox);
        mAddResultToProjectCheckBox->setObjectName(QString::fromUtf8("mAddResultToProjectCheckBox"));
        mAddResultToProjectCheckBox->setChecked(true);

        gridLayout_4->addWidget(mAddResultToProjectCheckBox, 6, 0, 1, 4);

        mOutputFormatComboBox = new QComboBox(mResultGroupBox);
        mOutputFormatComboBox->setObjectName(QString::fromUtf8("mOutputFormatComboBox"));

        gridLayout_4->addWidget(mOutputFormatComboBox, 1, 1, 1, 3);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_4->addItem(verticalSpacer, 5, 1, 1, 1);

        label = new QLabel(mResultGroupBox);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout_4->addWidget(label, 4, 0, 1, 1);

        mCrsSelector = new QgsProjectionSelectionWidget(mResultGroupBox);
        mCrsSelector->setObjectName(QString::fromUtf8("mCrsSelector"));
        mCrsSelector->setFocusPolicy(Qt::StrongFocus);

        gridLayout_4->addWidget(mCrsSelector, 4, 1, 1, 3);

        verticalSpacer_2 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_4->addItem(verticalSpacer_2, 7, 0, 1, 1);

        gridLayout_4->setColumnStretch(1, 1);
        gridLayout_4->setColumnStretch(2, 1);
        splitter->addWidget(mResultGroupBox);
        splitter_2->addWidget(splitter);
        verticalLayoutWidget = new QWidget(splitter_2);
        verticalLayoutWidget->setObjectName(QString::fromUtf8("verticalLayoutWidget"));
        verticalLayout = new QVBoxLayout(verticalLayoutWidget);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        mOperatorsGroupBox = new QgsCollapsibleGroupBox(verticalLayoutWidget);
        mOperatorsGroupBox->setObjectName(QString::fromUtf8("mOperatorsGroupBox"));
        gridLayout = new QGridLayout(mOperatorsGroupBox);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        gridLayout->setContentsMargins(0, -1, 0, 0);
        mOrButton = new QPushButton(mOperatorsGroupBox);
        mOrButton->setObjectName(QString::fromUtf8("mOrButton"));
        mOrButton->setText(QString::fromUtf8("OR"));

        gridLayout->addWidget(mOrButton, 2, 11, 1, 1);

        mLnButton = new QPushButton(mOperatorsGroupBox);
        mLnButton->setObjectName(QString::fromUtf8("mLnButton"));
        mLnButton->setText(QString::fromUtf8("ln"));

        gridLayout->addWidget(mLnButton, 1, 10, 1, 1);

        mLesserEqualButton = new QPushButton(mOperatorsGroupBox);
        mLesserEqualButton->setObjectName(QString::fromUtf8("mLesserEqualButton"));
        mLesserEqualButton->setText(QString::fromUtf8("<="));

        gridLayout->addWidget(mLesserEqualButton, 2, 6, 1, 1);

        mAndButton = new QPushButton(mOperatorsGroupBox);
        mAndButton->setObjectName(QString::fromUtf8("mAndButton"));
        mAndButton->setText(QString::fromUtf8("AND"));

        gridLayout->addWidget(mAndButton, 2, 10, 1, 1);

        mLogButton = new QPushButton(mOperatorsGroupBox);
        mLogButton->setObjectName(QString::fromUtf8("mLogButton"));
        mLogButton->setText(QString::fromUtf8("log10"));

        gridLayout->addWidget(mLogButton, 0, 10, 1, 1);

        mLessButton = new QPushButton(mOperatorsGroupBox);
        mLessButton->setObjectName(QString::fromUtf8("mLessButton"));
        mLessButton->setText(QString::fromUtf8("<"));

        gridLayout->addWidget(mLessButton, 2, 0, 1, 1);

        mGreaterEqualButton = new QPushButton(mOperatorsGroupBox);
        mGreaterEqualButton->setObjectName(QString::fromUtf8("mGreaterEqualButton"));
        mGreaterEqualButton->setText(QString::fromUtf8(">="));

        gridLayout->addWidget(mGreaterEqualButton, 2, 8, 1, 1);

        mTanButton = new QPushButton(mOperatorsGroupBox);
        mTanButton->setObjectName(QString::fromUtf8("mTanButton"));
        mTanButton->setText(QString::fromUtf8("tan"));

        gridLayout->addWidget(mTanButton, 0, 8, 1, 1);

        mPlusPushButton = new QPushButton(mOperatorsGroupBox);
        mPlusPushButton->setObjectName(QString::fromUtf8("mPlusPushButton"));
        mPlusPushButton->setText(QString::fromUtf8("+"));

        gridLayout->addWidget(mPlusPushButton, 0, 0, 1, 1);

        mMultiplyPushButton = new QPushButton(mOperatorsGroupBox);
        mMultiplyPushButton->setObjectName(QString::fromUtf8("mMultiplyPushButton"));
        mMultiplyPushButton->setText(QString::fromUtf8("*"));

        gridLayout->addWidget(mMultiplyPushButton, 0, 1, 1, 1);

        mCosButton = new QPushButton(mOperatorsGroupBox);
        mCosButton->setObjectName(QString::fromUtf8("mCosButton"));
        mCosButton->setText(QString::fromUtf8("cos"));

        gridLayout->addWidget(mCosButton, 0, 4, 1, 1);

        mGreaterButton = new QPushButton(mOperatorsGroupBox);
        mGreaterButton->setObjectName(QString::fromUtf8("mGreaterButton"));
        mGreaterButton->setText(QString::fromUtf8(">"));

        gridLayout->addWidget(mGreaterButton, 2, 1, 1, 1);

        horizontalSpacer_3 = new QSpacerItem(5, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_3, 0, 14, 1, 1);

        mATanButton = new QPushButton(mOperatorsGroupBox);
        mATanButton->setObjectName(QString::fromUtf8("mATanButton"));
        mATanButton->setText(QString::fromUtf8("atan"));

        gridLayout->addWidget(mATanButton, 1, 8, 1, 1);

        mACosButton = new QPushButton(mOperatorsGroupBox);
        mACosButton->setObjectName(QString::fromUtf8("mACosButton"));
        mACosButton->setText(QString::fromUtf8("acos"));

        gridLayout->addWidget(mACosButton, 1, 4, 1, 1);

        mASinButton = new QPushButton(mOperatorsGroupBox);
        mASinButton->setObjectName(QString::fromUtf8("mASinButton"));
        mASinButton->setText(QString::fromUtf8("asin"));

        gridLayout->addWidget(mASinButton, 1, 6, 1, 1);

        mNotEqualButton = new QPushButton(mOperatorsGroupBox);
        mNotEqualButton->setObjectName(QString::fromUtf8("mNotEqualButton"));
        mNotEqualButton->setText(QString::fromUtf8("!="));

        gridLayout->addWidget(mNotEqualButton, 2, 4, 1, 1);

        mCloseBracketPushButton = new QPushButton(mOperatorsGroupBox);
        mCloseBracketPushButton->setObjectName(QString::fromUtf8("mCloseBracketPushButton"));
        mCloseBracketPushButton->setText(QString::fromUtf8(")"));

        gridLayout->addWidget(mCloseBracketPushButton, 1, 11, 1, 1);

        mEqualButton = new QPushButton(mOperatorsGroupBox);
        mEqualButton->setObjectName(QString::fromUtf8("mEqualButton"));
        mEqualButton->setText(QString::fromUtf8("="));

        gridLayout->addWidget(mEqualButton, 2, 2, 1, 1);

        mMinusPushButton = new QPushButton(mOperatorsGroupBox);
        mMinusPushButton->setObjectName(QString::fromUtf8("mMinusPushButton"));
        mMinusPushButton->setText(QString::fromUtf8("-"));

        gridLayout->addWidget(mMinusPushButton, 1, 0, 1, 1);

        mOpenBracketPushButton = new QPushButton(mOperatorsGroupBox);
        mOpenBracketPushButton->setObjectName(QString::fromUtf8("mOpenBracketPushButton"));
        mOpenBracketPushButton->setText(QString::fromUtf8("("));

        gridLayout->addWidget(mOpenBracketPushButton, 0, 11, 1, 1);

        mDividePushButton = new QPushButton(mOperatorsGroupBox);
        mDividePushButton->setObjectName(QString::fromUtf8("mDividePushButton"));
        mDividePushButton->setText(QString::fromUtf8("/"));

        gridLayout->addWidget(mDividePushButton, 1, 1, 1, 1);

        mExpButton = new QPushButton(mOperatorsGroupBox);
        mExpButton->setObjectName(QString::fromUtf8("mExpButton"));
        mExpButton->setText(QString::fromUtf8("^"));

        gridLayout->addWidget(mExpButton, 1, 2, 1, 1);

        mSinButton = new QPushButton(mOperatorsGroupBox);
        mSinButton->setObjectName(QString::fromUtf8("mSinButton"));
        mSinButton->setText(QString::fromUtf8("sin"));

        gridLayout->addWidget(mSinButton, 0, 6, 1, 1);

        mSqrtButton = new QPushButton(mOperatorsGroupBox);
        mSqrtButton->setObjectName(QString::fromUtf8("mSqrtButton"));
        mSqrtButton->setText(QString::fromUtf8("sqrt"));

        gridLayout->addWidget(mSqrtButton, 0, 2, 1, 1);

        mAbsButton = new QPushButton(mOperatorsGroupBox);
        mAbsButton->setObjectName(QString::fromUtf8("mAbsButton"));
        mAbsButton->setText(QString::fromUtf8("abs"));

        gridLayout->addWidget(mAbsButton, 3, 0, 1, 1);

        mMinButton = new QPushButton(mOperatorsGroupBox);
        mMinButton->setObjectName(QString::fromUtf8("mMinButton"));
        mMinButton->setText(QString::fromUtf8("min"));

        gridLayout->addWidget(mMinButton, 3, 1, 1, 1);

        mMaxButton = new QPushButton(mOperatorsGroupBox);
        mMaxButton->setObjectName(QString::fromUtf8("mMaxButton"));
        mMaxButton->setText(QString::fromUtf8("max"));

        gridLayout->addWidget(mMaxButton, 3, 2, 1, 1);


        verticalLayout->addWidget(mOperatorsGroupBox);

        groupBox = new QGroupBox(verticalLayoutWidget);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        verticalLayout_2 = new QVBoxLayout(groupBox);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        verticalLayout_2->setContentsMargins(0, -1, 0, 0);
        mExpressionTextEdit = new QTextEdit(groupBox);
        mExpressionTextEdit->setObjectName(QString::fromUtf8("mExpressionTextEdit"));

        verticalLayout_2->addWidget(mExpressionTextEdit);


        verticalLayout->addWidget(groupBox);

        splitter_2->addWidget(verticalLayoutWidget);

        verticalLayout_3->addWidget(splitter_2);

        mExpressionValidLabel = new QLabel(QgsRasterCalcDialogBase);
        mExpressionValidLabel->setObjectName(QString::fromUtf8("mExpressionValidLabel"));

        verticalLayout_3->addWidget(mExpressionValidLabel);

        mButtonBox = new QDialogButtonBox(QgsRasterCalcDialogBase);
        mButtonBox->setObjectName(QString::fromUtf8("mButtonBox"));
        mButtonBox->setOrientation(Qt::Horizontal);
        mButtonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Help|QDialogButtonBox::Ok);

        verticalLayout_3->addWidget(mButtonBox);

        splitter_2->raise();
        mButtonBox->raise();
        mExpressionValidLabel->raise();
        QWidget::setTabOrder(mRasterBandsListWidget, mOutputFormatComboBox);
        QWidget::setTabOrder(mOutputFormatComboBox, mCurrentLayerExtentButton);
        QWidget::setTabOrder(mCurrentLayerExtentButton, mXMinSpinBox);
        QWidget::setTabOrder(mXMinSpinBox, mXMaxSpinBox);
        QWidget::setTabOrder(mXMaxSpinBox, mYMinSpinBox);
        QWidget::setTabOrder(mYMinSpinBox, mYMaxSpinBox);
        QWidget::setTabOrder(mYMaxSpinBox, mNColumnsSpinBox);
        QWidget::setTabOrder(mNColumnsSpinBox, mNRowsSpinBox);
        QWidget::setTabOrder(mNRowsSpinBox, mCrsSelector);
        QWidget::setTabOrder(mCrsSelector, mAddResultToProjectCheckBox);
        QWidget::setTabOrder(mAddResultToProjectCheckBox, mPlusPushButton);
        QWidget::setTabOrder(mPlusPushButton, mMultiplyPushButton);
        QWidget::setTabOrder(mMultiplyPushButton, mSqrtButton);
        QWidget::setTabOrder(mSqrtButton, mCosButton);
        QWidget::setTabOrder(mCosButton, mSinButton);
        QWidget::setTabOrder(mSinButton, mTanButton);
        QWidget::setTabOrder(mTanButton, mLogButton);
        QWidget::setTabOrder(mLogButton, mOpenBracketPushButton);
        QWidget::setTabOrder(mOpenBracketPushButton, mMinusPushButton);
        QWidget::setTabOrder(mMinusPushButton, mDividePushButton);
        QWidget::setTabOrder(mDividePushButton, mExpButton);
        QWidget::setTabOrder(mExpButton, mACosButton);
        QWidget::setTabOrder(mACosButton, mASinButton);
        QWidget::setTabOrder(mASinButton, mATanButton);
        QWidget::setTabOrder(mATanButton, mLnButton);
        QWidget::setTabOrder(mLnButton, mCloseBracketPushButton);
        QWidget::setTabOrder(mCloseBracketPushButton, mLessButton);
        QWidget::setTabOrder(mLessButton, mGreaterButton);
        QWidget::setTabOrder(mGreaterButton, mEqualButton);
        QWidget::setTabOrder(mEqualButton, mNotEqualButton);
        QWidget::setTabOrder(mNotEqualButton, mLesserEqualButton);
        QWidget::setTabOrder(mLesserEqualButton, mGreaterEqualButton);
        QWidget::setTabOrder(mGreaterEqualButton, mAndButton);
        QWidget::setTabOrder(mAndButton, mOrButton);
        QWidget::setTabOrder(mOrButton, mAbsButton);
        QWidget::setTabOrder(mAbsButton, mMinButton);
        QWidget::setTabOrder(mMinButton, mMaxButton);
        QWidget::setTabOrder(mMaxButton, mExpressionTextEdit);

        retranslateUi(QgsRasterCalcDialogBase);
        QObject::connect(mButtonBox, SIGNAL(accepted()), QgsRasterCalcDialogBase, SLOT(accept()));
        QObject::connect(mButtonBox, SIGNAL(rejected()), QgsRasterCalcDialogBase, SLOT(reject()));

        QMetaObject::connectSlotsByName(QgsRasterCalcDialogBase);
    } // setupUi

    void retranslateUi(QDialog *QgsRasterCalcDialogBase)
    {
        QgsRasterCalcDialogBase->setWindowTitle(QCoreApplication::translate("QgsRasterCalcDialogBase", "Raster Calculator", nullptr));
        mRasterBandsGroupBox->setTitle(QCoreApplication::translate("QgsRasterCalcDialogBase", "Raster Bands", nullptr));
        mResultGroupBox->setTitle(QCoreApplication::translate("QgsRasterCalcDialogBase", "Result Layer", nullptr));
        mRowsLabel->setText(QCoreApplication::translate("QgsRasterCalcDialogBase", "Rows", nullptr));
        mYMinLabel->setText(QCoreApplication::translate("QgsRasterCalcDialogBase", "Y min", nullptr));
        mXMinLabel->setText(QCoreApplication::translate("QgsRasterCalcDialogBase", "X min", nullptr));
        mXMaxLabel->setText(QCoreApplication::translate("QgsRasterCalcDialogBase", "X max", nullptr));
        mColumnsLabel->setText(QCoreApplication::translate("QgsRasterCalcDialogBase", "Columns", nullptr));
        mYMaxLabel->setText(QCoreApplication::translate("QgsRasterCalcDialogBase", "Y max", nullptr));
        mOutputFormatLabel->setText(QCoreApplication::translate("QgsRasterCalcDialogBase", "Output format", nullptr));
        mCurrentLayerExtentButton->setText(QCoreApplication::translate("QgsRasterCalcDialogBase", "Selected Layer Extent", nullptr));
        mOutputLayerLabel->setText(QCoreApplication::translate("QgsRasterCalcDialogBase", "Output layer", nullptr));
        mAddResultToProjectCheckBox->setText(QCoreApplication::translate("QgsRasterCalcDialogBase", "Add result to project", nullptr));
        label->setText(QCoreApplication::translate("QgsRasterCalcDialogBase", "Output CRS", nullptr));
        mOperatorsGroupBox->setTitle(QCoreApplication::translate("QgsRasterCalcDialogBase", "Operators", nullptr));
        groupBox->setTitle(QCoreApplication::translate("QgsRasterCalcDialogBase", "Raster Calculator Expression", nullptr));
        mExpressionValidLabel->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class QgsRasterCalcDialogBase: public Ui_QgsRasterCalcDialogBase {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_QGSRASTERCALCDIALOGBASE_H
