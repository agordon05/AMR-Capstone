package QR_Code;

import static org.junit.jupiter.api.Assertions.*;

import java.util.ArrayList;

import org.junit.jupiter.api.Test;

class QR_Queue_Test {
	
	void initialize(){
		QR_Queue.initialize();
	}
	void fillQueue() {
		QR_Queue.addToQueue();
	}
	void load() {
		
		QR_Access.initialize();
		
		// tests get methods
		
		int x_size = 20;
		int y_size = 20;

		for(int xIndex = 0; xIndex < x_size; xIndex++) {
			for(int yIndex = 0; yIndex < y_size; yIndex++) {
				String url = "QR_Code_" + xIndex + "_" + yIndex;
				String code = "d8iaosd5" + xIndex + "asdkflj" + yIndex + "asdfg235";
				int x_pos = xIndex;
				int y_pos = yIndex;
				String status = QR_Object.ACTIVE_STATUS;
				QR_Object obj = new QR_Object(url, code, x_pos, y_pos, status);
				QR_Access.addQR(obj);
			}
		}
		
	}
	
	
	@Test
	void test() {
		
		// initialize
		initialize();
		load();
		
		// add qr to queue
		QR_Object obj = QR_Access.getQrByPosition(1, 1);
		QR_Queue.addQR(obj);
		
		// tests that object in queue is not null
		assertEquals(obj, QR_Queue.getCurrentQR());
		
		
		assertEquals(null, QR_Queue.getPrevQR());
		// tests pop method
		QR_Queue.pop();
		assertEquals(null, QR_Queue.getCurrentQR());
		assertEquals(obj, QR_Queue.getPrevQR());
		
		QR_Queue.addToQueue();
		ArrayList<QR_Object> queue = QR_Queue.getQueue();
		assertEquals(QR_Queue.sizeOfQueue, queue.size());
		for(int index = 0; index < queue.size(); index++) {
			
			System.out.println(queue.get(index).toString());
		}
		obj = QR_Queue.getCurrentQR();
		QR_Queue.pop();
		assertEquals(QR_Queue.sizeOfQueue - 1, QR_Queue.getQueue().size());
		
		
	}

}
