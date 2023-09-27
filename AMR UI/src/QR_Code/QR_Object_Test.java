package QR_Code;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class QR_Object_Test {

	@Test
	void test() {
		
		// tests get methods
		String url = "QR_Code_0_1";
		String code = "d8g8hr8jf85ju9j34s2435";
		int x_pos = 0;
		int y_pos = 1;
		String status = QR_Object.ACTIVE_STATUS;
		
		QR_Object obj = new QR_Object(url, code, x_pos, y_pos, status);
		
		assertEquals(url, obj.getName());
		assertEquals(code, obj.getQRCode());
		assertEquals(x_pos, obj.getX_pos());
		assertEquals(y_pos, obj.getY_pos());
		assertEquals("Active", obj.getStatus());
		
		//tests status for using correct status string
		url = "QR_Code_5_10";
		code = "d8galkj8jf85ju9j34s2435";
		x_pos = 5;
		y_pos = 10;
		status = "active";

		obj = new QR_Object(url, code, x_pos, y_pos, status);

		assertEquals(url, obj.getName());
		assertEquals(code, obj.getQRCode());
		assertEquals(x_pos, obj.getX_pos());
		assertEquals(y_pos, obj.getY_pos());
		assertEquals(QR_Object.FLAWED_STATUS, obj.getStatus());

		//tests for negative numbers
		url = "QR_Code_-5_-10";
		code = "d8galkasdfjf85ju9j34s25";
		x_pos = -5;
		y_pos = -10;
		status = QR_Object.ACTIVE_STATUS;

		obj = new QR_Object(url, code, x_pos, y_pos, status);

		assertEquals(url, obj.getName());
		assertEquals(code, obj.getQRCode());
		assertEquals(x_pos, obj.getX_pos());
		assertEquals(y_pos, obj.getY_pos());
		assertEquals(QR_Object.ACTIVE_STATUS, obj.getStatus());
		
		//tests for null values
		url = null;
		code = "d8galkasdfjf85ju9j34s25";
		x_pos = -5;
		y_pos = -10;
		status = QR_Object.ACTIVE_STATUS;

		obj = new QR_Object(url, code, x_pos, y_pos, status);

		assertEquals("invalid", obj.getName());
		assertEquals("invalid", obj.getQRCode());
		assertEquals(0, obj.getX_pos());
		assertEquals(0, obj.getY_pos());
		assertEquals(QR_Object.FLAWED_STATUS, obj.getStatus());
		
		//tests for null values
		url = "QR_Code_5_0";
		code = null;
		x_pos = 5;
		y_pos = 0;
		status = QR_Object.ACTIVE_STATUS;

		obj = new QR_Object(url, code, x_pos, y_pos, status);

		assertEquals("invalid", obj.getName());
		assertEquals("invalid", obj.getQRCode());
		assertEquals(0, obj.getX_pos());
		assertEquals(0, obj.getY_pos());
		assertEquals(QR_Object.FLAWED_STATUS, obj.getStatus());

		//tests for null values
		url = "QR_Code_5_0";
		code = "kfa89uf43jkbfw9834vn";
		x_pos = 5;
		y_pos = 0;
		status = null;

		obj = new QR_Object(url, code, x_pos, y_pos, status);

		assertEquals("invalid", obj.getName());
		assertEquals("invalid", obj.getQRCode());
		assertEquals(0, obj.getX_pos());
		assertEquals(0, obj.getY_pos());
		assertEquals(QR_Object.FLAWED_STATUS, obj.getStatus());
		
			
	}
	
//	@Test
//	void test2() {
//		fail("Not yet implemented");
//	}

}
