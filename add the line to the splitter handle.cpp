// Now add the line to the splitter handle
// Note: index 0 handle is always hidden, index 1 is between the two widgets
QSplitterHandle *handle = pSplitter->handle(1);
QVBoxLayout *layout = new QVBoxLayout(handle);
layout->setSpacing(0);
layout->setMargin(0);

QFrame *line = new QFrame(handle);
line->setFrameShape(QFrame::HLine);
line->setFrameShadow(QFrame::Sunken);
layout->addWidget(line);