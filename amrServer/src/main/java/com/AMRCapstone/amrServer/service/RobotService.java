package com.AMRCapstone.amrServer.service;

import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import com.AMRCapstone.amrServer.Codes;
import com.AMRCapstone.amrServer.access.QRAccess;
import com.AMRCapstone.amrServer.access.QR_Queue;
import com.AMRCapstone.amrServer.access.RobotAccess;
import com.AMRCapstone.amrServer.model.Robot;

@Service
public class RobotService {

    public Robot get() {
        return RobotAccess.getRobot();
    }

    public ResponseEntity<float[]> update(Robot temp) {
        Robot robot = RobotAccess.getRobot();

        // validation
        // check status
        if (temp.getStatus().equals(Codes.statusActive) || temp.getStatus().equals(Codes.statusInactive)) {
            robot.setStatus(temp.getStatus());
        }
        // check message
        if (temp.getMessage().equals(Codes.FoundObjMessage) ||
                temp.getMessage().equals(Codes.FoundQRMessage) ||
                temp.getMessage().equals(Codes.HeadingMesssage) ||
                temp.getMessage().equals(Codes.NotConnectedMessage) ||
                temp.getMessage().equals(Codes.ScanningMessage) ||
                temp.getMessage().equals(Codes.UserControl)) {
            robot.setMessage(temp.getMessage());
        }

        // update robot
        robot.setX_pos(temp.getX_pos());
        robot.setY_pos(temp.getY_pos());
        robot.setRotation(temp.getRotation());

        robot.setQrScan(temp.getQrScan());
        robot.setLoggerList(temp.getLoggerList());
        robot.setImage(temp.getImage());

        HttpStatus status;

        if (robot.getQrScan() == null) {
            status = HttpStatus.OK;
        }
        // test QR Scan
        else {
            // check QRQueue
            if (QR_Queue.getCurrentQR().getCode().equals(robot.getQrScan())) {
                // pop queue
                QR_Queue.pop();
                status = HttpStatus.OK;
            } else if (QRAccess.getQrByQRCode(robot.getQrScan()) != null) {
                // reset Queue
                QR_Queue.initialize(robot.getQrScan());

                // send out destination, QR position, Http status I-am-a-tea-pot
                status = HttpStatus.I_AM_A_TEAPOT;
            } else {
                status = HttpStatus.NOT_FOUND;
            }

        }

        robot.setX_destination(QR_Queue.getCurrentQR().getX_pos());
        robot.setY_destination(QR_Queue.getCurrentQR().getY_pos());
        robot.setQrScan(null);

        float[] response;
        if (status == HttpStatus.I_AM_A_TEAPOT) {
            response = new float[4];

            // destination
            response[0] = robot.getX_destination();
            response[1] = robot.getY_destination();

            // QR position
            response[2] = QR_Queue.getPrevQR().getX_pos();
            response[3] = QR_Queue.getPrevQR().getY_pos();
        }

        else {
            response = new float[2];
            response[0] = robot.getX_destination();
            response[1] = robot.getY_destination();

        }

        // create response

        HttpHeaders headers = new HttpHeaders();

        return new ResponseEntity<>(response, headers, HttpStatus.OK);
    }

}
