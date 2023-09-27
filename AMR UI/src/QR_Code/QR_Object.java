package QR_Code;

public class QR_Object {
	
	private String name = ""; // QR_Code 0-1
	private String QRCode = ""; // the string representation of the qr code
	private int x_pos = 0; // the x position of the qr code
	private int y_pos = 0; // the y position of the qr code
	private String status = ""; // the status of the qr code -- active, missing, damaged
	
	public QR_Object(String name, String code, int x_pos, int y_pos, String status) {
		this.name = name;
		this.QRCode = code;
		this.x_pos = x_pos;
		this.y_pos = y_pos;
		this.status = status;
	}

	/**
	 * @return the uRL
	 */
	public String getName() {
		return name;
	}

	/**
	 * @return the code
	 */
	public String getQRCode() {
		return QRCode;
	}

	/**
	 * @return the x_pos
	 */
	public int getX_pos() {
		return x_pos;
	}

	/**
	 * @return the y_pos
	 */
	public int getY_pos() {
		return y_pos;
	}

	/**
	 * @return the status
	 */
	public String getStatus() {
		return status;
	}
	

	
	
	

}
