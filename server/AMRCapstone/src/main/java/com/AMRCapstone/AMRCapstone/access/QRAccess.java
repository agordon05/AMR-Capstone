package com.AMRCapstone.AMRCapstone.access;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import com.AMRCapstone.AMRCapstone.model.QR;

public class QRAccess {
    // private static ArrayList<QR> QR_Codes;

    private static Map<String, QR> QRList;

    private final static String fileName = "/QR_Data.txt";

    private static BufferedReader bufferedReader = null;

    public static void initialize() {
        // QR_Codes = new ArrayList<QR>();
        QRList = new HashMap<String, QR>();

        // QRList.put("QR_Code_2_5", new QR("QR_Code_2_5", "Active", "image",
        // "342wfer89", 2,
        // 5));
        // QRList.put("QR_Code_2_4", new QR("QR_Code_2_4", "Active", "image", "879g2f3",
        // 2,
        // 4));
        // QRList.put("QR_Code_1_5", new QR("QR_Code_1_5", "Missing", "image",
        // "f2g34798", 1,
        // 5));

        // loadQRCodes();
    }

    public static void loadQRCodes() {
        try {
            // directory to current file, /../../ returns two directories which is where
            // file is located
            String filePath = new File("").getAbsolutePath() + fileName;
            // Create a FileReader and bufferedReader to read the file
            FileReader fileReader = new FileReader(filePath);
            bufferedReader = new BufferedReader(fileReader);

            String line;
            int count = 0;

            // Reads each line in data file
            while ((line = bufferedReader.readLine()) != null) {
                // Prints line for testing
                System.out.println(line);

                // Splits data into tokens
                String[] qrData = line.split("#");

                // Ensures correct number of tokens
                if (qrData.length != 5)
                    throw new Exception("data is corrupted");

                // Initializes data to objects
                String fileName = qrData[0];
                String qrCode = qrData[1];
                int x_pos = Integer.parseInt(qrData[2]);
                int y_pos = Integer.parseInt(qrData[3]);
                String status = qrData[4];

                // ---PLACEHOLDER---
                String image = "image";

                // Creates and adds qr object to access list
                QR temp = new QR(fileName, status, image, qrCode, x_pos, y_pos);
                addQR(temp);
                count++;
                System.out.println(count);

            }

            // Close BufferedReader
            // bufferedReader.close();

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (bufferedReader != null)
                try {
                    bufferedReader.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }

        }

    }

    public static void addQR(QR qr) {
        if (qr == null)
            return;
        // QR_Codes.add(qr);
        QRList.put(qr.getName(), qr);
    }

    public static Map<String, QR> getQRs() {
        return QRList;
    }

    public static QR getQrByPosition(float x, float y) {

        // Search through all of QR list
        // for (int index = 0; index < QR_Codes.size(); index++) {

        // // If QR code has the same x and y position, return QR
        // if (QR_Codes.get(index).getX_pos() == x && QR_Codes.get(index).getY_pos() ==
        // y) {
        // return QR_Codes.get(index);
        // }
        // }

        for (QR qr : QRList.values()) {
            if (qr.getX_pos() == x && qr.getY_pos() == y) {
                return qr;
            }
        }

        return null;
    }

    public static QR getQrByQRCode(String QRCode) {

        // Search through all of QR list
        // for (int index = 0; index < QR_Codes.size(); index++) {

        // // If QR has the same QR code, return QR
        // if (QR_Codes.get(index).getCode().equals(QRCode)) {
        // return QR_Codes.get(index);
        // }
        // }

        for (QR qr : QRList.values()) {
            if (qr.getCode().equals(QRCode)) {
                return qr;
            }
        }

        return null;

    }

    public static ArrayList<QR> getNearbyQR(float x, float y) {

        ArrayList<QR> list = new ArrayList<QR>();

        for (QR qr : QRList.values()) {
            float x_pos = qr.getX_pos();
            float y_pos = qr.getY_pos();

            if (x_pos == x && y_pos == y)
                continue;

            // if(x_pos == x){
            // if(Math.abs(y_pos - y) <= 1){

            // }
            // }
            // else if (y_pos == y){

            // }
            // If x and y coordinates of QR are 1 away, add to list
            else if (Math.abs(x_pos - x) <= 1 && Math.abs(y_pos - y) <= 1) {
                list.add(qr);
            }
        }

        return list;
    }

}
