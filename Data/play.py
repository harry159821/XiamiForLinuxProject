#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
TIME =  time.time()
import pymedia.audio.acodec as acodec
import pymedia.audio.sound as sound
import pymedia.muxer as muxer
import urllib2,thread,threading,sys
import socket

class Player():
    '''
    music player online
    '''
    def __init__(self,file_name):
        self.file_name = file_name
        self.i = 0
        #self.play()
        f0 = file('start.txt','a')
        f0.write('start\n')
        f0.close()
        self.TcpThread = tcpThread(self)
        self.TcpThread.start()

    def play(self):
        self.stopFlag = True
        self.mp3 = []
        self.i = 0
        #dm = muxer.Demuxer(str.split(self.file_name, '.')[-1].lower())
        dm = muxer.Demuxer('mp3')
        #f = open(self.file_name, 'rb')
        snd = dec = None
        header = {
                    #'Referer': 'http://www.xiami.com/',
                    'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36',
                 }
        request = urllib2.Request(self.file_name,headers=header)
        self.f = urllib2.urlopen(request)
        
        print 'Player Init Time:%s'%(time.time()-TIME)
        #s = self.f.read(32000)
        s = self.f.read(10000)
        #thread.start_new_thread(self.download,())

        self.tcpFlag = True

        #self.TcpThread = tcpThread(self)
        #self.TcpThread.start()

        #self.downloadthread = downloadThread(self.f, self.mp3)
        #self.downloadthread.start()

        while self.stopFlag:
            pass

        print 'first read long:%s'%(len(s))
        while len(s) and self.tcpFlag:
            frames = dm.parse(s)
            if frames:
                for fr in frames:
                    if dec == None:
                        dec = acodec.Decoder(dm.streams[fr[0]])
                        
                    r = dec.decode(fr[1])
                    if r and r.data:
                        if snd == None:
                            snd = sound.Output(
                                int(r.sample_rate),
                                r.channels,
                                sound.AFMT_S16_LE)
                        data = r.data
                        try:
                            snd.play(data)
                        except Exception, e:
                            print e
                            #sys.exit(0)
            '''
            if self.i<len(self.mp3):
                s = self.mp3[self.i]
            else:
                s = []
            self.i = self.i + 1
            '''         
            s = self.f.read(2000)
        print 'stop'
        f1 = file('stoped.txt','a')
        f1.write('stop\n')
        f1.close()
        #sys.exit(0)
        '''
        print 'DownLoad Complete'
        while snd.isPlaying():
            time.sleep(.05)
        '''

    def stop(self):
        print 'tcpFlag stop'
        self.tcpFlag =False
        #self.downloadthread.stop()

    def download(self):
        print 'download start'
        s = self.f.read(2000)
        i = 0
        while len(s) and self.tcpFlag:
            self.mp3.append(s)
            try:
                s = self.f.read(2000)
            except Exception, e:
                s = 0
            i = i+101
        print 'Download Complete,Long:%s,Use time:%s'%(i,time.time()-TIME)
        thread.exit_thread()

class downloadThread(threading.Thread):
    def __init__(self,f,mp3):
        threading.Thread.__init__(self)
        self.f = f
        self.mp3 = mp3
        self.thread_stop = False

    def run(self):
        s = self.f.read(2000)
        i = 0
        while len(s) and not self.thread_stop:
            self.mp3.append(s)
            try:
                s = self.f.read(2000)
            except Exception, e:
                s = 0
            i = i+1
        print 'Download Complete,Long:%s,Use time:%s'%(i,time.time()-TIME)

    def stop(self):
        self.thread_stop = True

class tcpThread(threading.Thread):
    def __init__(self,master):
        threading.Thread.__init__(self)
        self.master = master

    def run(self):
        print 'link server start'
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        for i in range(9000,9002):
            try:
                sock.connect(('localhost', i))
                sock.send('test')
                if sock.recv(1024) == 'welcome to server!':
                    print 'link server success',i
                    sock.send('stop')
                    print sock.recv(1024)
                    sock.close()
                break
            except Exception,e:
                print '1',i,e
                pass
        print 'no server exits,I brcome server'

        self.master.stopFlag = False
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        for p in range(9000,9002):
            try:
                sock.bind(('localhost', p))
                print 'server listen start',p
                break
            except Exception,e:
                #print p,e
                pass

        self.stop = False
        sock.listen(5)
        while not self.stop:
            #等待下一个客户端连结
            connection, address = sock.accept()
            #连结是一个新的socket
            print 'Server connected by', address
            while not self.stop:
                try:
                    connection.settimeout(5)
                    #读取客户端套接字的下一行
                    data = connection.recv(1024)
                    #如果没有数量的话，那么跳出循环
                    if not data: break
                    if data == 'test':  
                        connection.send('welcome to server!')  
                    else:  
                        connection.send('please go out!')
                        print 'ok i go out'                    
                        self.stop = True
                except socket.timeout:  
                    print 'time out'                
            #当socket关闭时eof
            connection.close()

        self.master.stop()
        print 'tcp over'

if __name__ == "__main__":
    print 'python Init Time:%s'%(time.time()-TIME)
    p = Player("http://m5.file.xiami.com/813/98813/471688/1770554727_4338192_l.mp3?auth_key=5de7c9a7be8dc675985385cf5db8b4ee-1406160000-0-null")
    p.play()
