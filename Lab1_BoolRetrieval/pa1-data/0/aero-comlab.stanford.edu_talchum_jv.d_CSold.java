import java io import java net import java util public class chatserver public static void main string args throws ioexception if args length 1 throw new illegalargumentexception syntax chat server port int port integer parseint args 0 serversocket server new serversocket port while true socket client server accept system out println accepted from client getinetaddress chathandler handler new chathandler client handler start