void SaleDialog::initFindCustomerButton() {
    QString imagePath = QString("%1/find.png").arg(Configs::getInstance().getImagesFolderFilePath());
    QPixmap pixmap(imagePath);
    QIcon icon(imagePath);
    findCustomerButton = new QPushButton(icon, "");
    QSize size = QSize(pixmap.size().width() + 6, pixmap.size().height() + 4);
    findCustomerButton->setMinimumSize(size);
    findCustomerButton->setMaximumSize(size); // 设置按钮的大小为图片的大小
    findCustomerButton->setFocusPolicy(Qt::NoFocus); // 得到焦点时，不显示虚线框
    findCustomerButton->setFlat(true);
    findCustomerButton->setDefault(true);
    findCustomerButton->setToolTip(tr("查找客户"));

    QHBoxLayout *buttonLayout = new QHBoxLayout();
    buttonLayout->setContentsMargins(0, 0, 0, 0);
    buttonLayout->addStretch();
    buttonLayout->addWidget(findCustomerButton);
    ui->cardNumberLineEdit->setLayout(buttonLayout);
	// 设置输入框中文件输入区，不让输入的文字在被隐藏在按钮下
    ui->cardNumberLineEdit->setTextMargins(0, 1, pixmap.size().width(), 1); 

    connect(findCustomerButton, SIGNAL(clicked()), this, SLOT(findCustomer()));
}