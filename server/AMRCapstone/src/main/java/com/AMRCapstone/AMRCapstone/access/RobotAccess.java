package com.AMRCapstone.AMRCapstone.access;

import java.util.ArrayList;

import com.AMRCapstone.AMRCapstone.model.Robot;

public class RobotAccess {
    private static Robot robot;

    public static void initialize() {
        // QR_Codes = new ArrayList<QR>();
        robot = loadRobot();
    }

    private static Robot loadRobot() {
        // TEMPORARY
        robot = new Robot(1, "Inactive", "Connecting", 0, 0, 0, 0, 0, null, new ArrayList<String>(), null);
        robot.addtoLoggerList("Waiting for robot to connect");
        // robot.setUserSignal("Forward");
        return robot;
    }

    public static Robot getRobot() {
        return robot;
    }
}
