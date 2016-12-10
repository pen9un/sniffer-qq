import socket
import struct

while(1):
	HOST = socket.gethostbyname(socket.gethostname())[2]

	s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
	s.bind((HOST, 0))
	s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
	s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)



	buf = s.recvfrom(65565)

	src_ip = "%d.%d.%d.%d"%struct.unpack('BBBB', buf[0][12:16])
	dest_ip ="%d.%d.%d.%d"%struct.unpack('BBBB', buf[0][16:20])


	data1 = int(str("%d"%struct.unpack('B', buf[0][20:21])))
	data2 = int(str("%d"%struct.unpack('B', buf[0][21:22])))
	data3 = int(str("%d"%struct.unpack('B', buf[0][22:23])))
	data4 = int(str("%d"%struct.unpack('B', buf[0][23:24])))

	port   = data1 * 16*16 + data2
	d_port = data3 * 16*16 + data4
	if ((port == 4009) and (d_port == 8000)):
		_qq1 = int(str("%d"%struct.unpack('B', buf[0][35:36])))
		_qq2 = int(str("%d"%struct.unpack('B', buf[0][36:37])))
		_qq3 = int(str("%d"%struct.unpack('B', buf[0][37:38])))
		_qq4 = int(str("%d"%struct.unpack('B', buf[0][38:39])))
		QQNUMBER = _qq1*16*16*16*16*16*16+_qq2*16*16*16*16+_qq3*16*16+_qq4
		print QQNUMBER

	s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
