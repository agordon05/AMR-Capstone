package QR_Code;

import static org.junit.jupiter.api.Assertions.*;

import java.util.ArrayList;

import org.junit.jupiter.api.Test;

class QR_Access_Test {

	void initialize() {
		QR_Access.initialize();
	}
	
	void load() {
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
		
		
		// initializes access list
		initialize();
		// loads qr codes
		load();
		
		// tests objects aren't null
		QR_Object obj = QR_Access.getQrByPosition(0, 0);
		assertNotEquals(null, obj);
		assertNotEquals(null, obj.getName());
		assertNotEquals(null, obj.getQRCode());
		assertNotEquals(null, obj.getStatus());

		// tests the get qr by position method
		obj = QR_Access.getQrByQRCode("d8iaosd51asdkflj1asdfg235"); // qr code with position (1,1)
		assertNotEquals(null, obj);
		assertEquals("QR_Code_1_1", obj.getName());
		assertEquals("d8iaosd51asdkflj1asdfg235",obj.getQRCode());
		assertEquals(1, obj.getX_pos());
		assertEquals(1, obj.getY_pos());
		assertEquals(QR_Object.ACTIVE_STATUS, obj.getStatus());

		// tests get nearby qr codes method
		ArrayList<QR_Object> list = QR_Access.getNearbyQR(10, 5);
		for(int index = 0; index < list.size(); index++) {
			
			System.out.println(list.get(index).toString());
		}
		// tests size is correct
		assertNotEquals(0, list.size());
		assertEquals(8, list.size());
//		// tests qr codes in list are actually 1 apart
//		for(int index = 0; index < list.size(); index++) {
//			assertEquals(1, Math.abs(list.get(index).getX_pos() - 1));
//			assertEquals(1, Math.abs(list.get(index).getY_pos() - 1));
//			
//		}

		
	}
	
	@Test
	void test2() {
		QR_Access.initialize();
		assertTrue(0 == QR_Access.getQRs().size());
		QR_Access.loadQRCodes();
		assertTrue(60 == QR_Access.getQRs().size(), "size of qr list was actually " + QR_Access.getQRs().size());
	}

}
