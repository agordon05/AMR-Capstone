package com.AMRCapstone.AMRCapstone.service;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import java.util.ArrayList;

import com.AMRCapstone.AMRCapstone.Codes;
import com.AMRCapstone.AMRCapstone.access.QRAccess;
import com.AMRCapstone.AMRCapstone.access.QR_Queue;
import com.AMRCapstone.AMRCapstone.access.RobotAccess;
import com.AMRCapstone.AMRCapstone.model.QR;
import com.AMRCapstone.AMRCapstone.model.Robot;

public class RobotServiceTest {
    private RobotService robotService;

    public void createRobotService(RobotService robotService) {
        this.robotService = robotService;
    }

    QR temp = new QR("QR_Code_1_1", Codes.QRActive, "image", "test", 1, 1);
    QR temp2 = new QR("QR_Code_1_2", Codes.QRActive, "image", "test2", 1, 2);
    QR temp3 = new QR("QR_Code_1_3", Codes.QRActive, "image", "test3", 1, 3);
    QR temp4 = new QR("QR_Code_2_1", Codes.QRActive, "image", "test4", 2, 1);
    QR temp5 = new QR("QR_Code_2_2", Codes.QRLost, "image", "test5", 2, 2);
    QR temp6 = new QR("QR_Code_2_3", Codes.QRLost, "image", "test6", 2, 3);
    QR temp7 = new QR("QR_Code_3_1", Codes.QRActive, "image", "test7", 3, 1);
    QR temp8 = new QR("QR_Code_3_2", Codes.QRActive, "image", "test8", 3, 2);
    QR temp9 = new QR("QR_Code_3_3", Codes.QRActive, "image", "test9", 3, 3);

    void initialize() {
        QR_Queue.initialize();
        QRAccess.initialize();
        RobotAccess.initialize();
        QRAccess.addQR(temp);
        QRAccess.addQR(temp2);
        QRAccess.addQR(temp3);
        QRAccess.addQR(temp4);
        QRAccess.addQR(temp5);
        QRAccess.addQR(temp6);
        QR_Queue.QueueUp();
    }

    @Test
    void testGet() {
        initialize();
        createRobotService(new RobotService());
        assertTrue(RobotAccess.getRobot().equals(robotService.get()), "");
    }

    @Test
    void testUpdate() {

        initialize();
        createRobotService(new RobotService());

        QR_Queue.resetQueue(temp);
        // QR actual = QR_Queue.getCurrentQR();
        // System.out.println(actual);

        assertTrue(temp.equals(QR_Queue.getCurrentQR()), temp.getCode() + "QR was not as expected");
        assertTrue(QR_Queue.getCurrentQR().getX_pos() == 1, "QR x pos was not as expected");
        assertTrue(QR_Queue.getCurrentQR().getY_pos() == 1, "QR y pos was not as expected");

        ArrayList<String> log = new ArrayList<>();
        log.add(Codes.HeadingMesssage);

        Robot tempRobot = new Robot(1, Codes.statusActive, Codes.HeadingMesssage, 2,
                3,
                35, 3, 5, null, log, null);
        ResponseEntity<float[]> response = robotService.update(tempRobot);

        // testing response
        // assertTrue(response.getStatusCode().equals(HttpStatus.OK));
        assertTrue(response.getBody()[0] == 1, "x_destination was actually " +
                response.getBody()[0]);
        assertTrue(response.getBody()[1] == 1, "y_destination was actually " +
                response.getBody()[1]);
        assertTrue(response.getBody().length == 2, "length was actually " +
                response.getBody().length);

        // testing update for robot in access
        assertTrue(RobotAccess.getRobot().getX_pos() == 2);
        assertTrue(RobotAccess.getRobot().getY_pos() == 3);
        assertTrue(RobotAccess.getRobot().getRotation() == 35);

        assertTrue(RobotAccess.getRobot().equals(robotService.get()),
                "Robot in Access is not the robot gotten");
    }

    // testing correct QR scan and appropriate response
    @Test
    void testUpdate2() {

        initialize();
        createRobotService(new RobotService());

        QR_Queue.resetQueue(temp);
        // QR actual = QR_Queue.getCurrentQR();
        // System.out.println(actual);

        assertTrue(temp.equals(QR_Queue.getCurrentQR()), temp.getCode() + "QR was not as expected");
        assertTrue(QR_Queue.getCurrentQR().getX_pos() == 1, "QR x pos was not as expected");
        assertTrue(QR_Queue.getCurrentQR().getY_pos() == 1, "QR y pos was not as expected");

        ArrayList<String> log = new ArrayList<>();
        log.add(Codes.HeadingMesssage);

        Robot tempRobot = new Robot(1, Codes.statusActive, Codes.HeadingMesssage, 2,
                3,
                35, 3, 5, "test", log, null);
        ResponseEntity<float[]> response = robotService.update(tempRobot);

        // testing response
        // assertTrue(response.getStatusCode().equals(HttpStatus.CONTINUE),
        // "http status code was " + response.getStatusCode().toString());

        assertTrue(response.getBody().length == 4, "length was actually " +
                response.getBody().length);

        assertTrue(response.getBody()[0] != 1 || response.getBody()[1] != 1,
                "destination didnt change " + response.getBody()[0] + " - " +
                        response.getBody()[1]);
        assertTrue(response.getBody()[2] == 1 && response.getBody()[3] == 1,
                "position returned " + response.getBody()[0] + " - " +
                        response.getBody()[1]);

        // testing update for robot in access
        assertTrue(RobotAccess.getRobot().getX_pos() == 2);
        assertTrue(RobotAccess.getRobot().getY_pos() == 3);
        assertTrue(RobotAccess.getRobot().getX_destination() == QR_Queue.getCurrentQR().getX_pos()
                && RobotAccess.getRobot().getY_destination() == QR_Queue.getCurrentQR().getY_pos());
        assertTrue(RobotAccess.getRobot().getRotation() == 35);
        assertNull(RobotAccess.getRobot().getQrScan(), "QR Scan was not null");
        assertTrue(RobotAccess.getRobot().equals(robotService.get()),
                "Robot in Access is not the robot gotten");
    }

    // testing updating the robot to current position, correction of destination and
    // adjustment of QR queue from incorrect QR scan
    @Test
    void testUpdate3() {

        initialize();
        createRobotService(new RobotService());

        QR_Queue.resetQueue(temp);
        // QR actual = QR_Queue.getCurrentQR();
        // System.out.println(actual);

        assertTrue(temp.equals(QR_Queue.getCurrentQR()), temp.getCode() + "QR was not as expected");
        assertTrue(QR_Queue.getCurrentQR().getX_pos() == 1, "QR x pos was not as expected");
        assertTrue(QR_Queue.getCurrentQR().getY_pos() == 1, "QR y pos was not as expected");

        ArrayList<String> log = new ArrayList<>();
        log.add(Codes.HeadingMesssage);

        Robot tempRobot = new Robot(1, Codes.statusActive, Codes.HeadingMesssage, 2,
                3,
                35, 3, 5, "test2", log, null);
        ResponseEntity<float[]> response = robotService.update(tempRobot);
        assertTrue(response != null);
        assertTrue(response.getBody() != null);
        // testing response
        // assertTrue(response.getStatusCode().equals(HttpStatus.ACCEPTED),
        // "http status code was " + response.getStatusCode().toString());
        assertTrue(response.getBody().length == 4, "length was actually " +
                response.getBody().length);
        assertTrue(response.getBody()[2] == 1 && response.getBody()[3] == 2,
                "position returned " + response.getBody()[0] + " - " +
                        response.getBody()[1]);

        // ----- SOMETIMES FAILS -----
        assertTrue(response.getBody()[0] != 1 || response.getBody()[1] != 2,
                "destination didnt changed " + response.getBody()[0] + " - " +
                        response.getBody()[1]);

        // testing update for robot in access
        assertTrue(RobotAccess.getRobot().getX_pos() == 2);
        assertTrue(RobotAccess.getRobot().getY_pos() == 3);
        assertTrue(RobotAccess.getRobot().getX_destination() == QR_Queue.getCurrentQR().getX_pos()
                && RobotAccess.getRobot().getY_destination() == QR_Queue.getCurrentQR().getY_pos());
        assertTrue(RobotAccess.getRobot().getRotation() == 35);
        assertNull(RobotAccess.getRobot().getQrScan(), "QR Scan was not null");
        assertTrue(RobotAccess.getRobot().equals(robotService.get()), "Robot in Access is not the robot gotten");
    }
}
