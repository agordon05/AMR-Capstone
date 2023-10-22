package com.AMRCapstone.AMRCapstone.controller;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.fail;

import java.util.ArrayList;
import java.util.Arrays;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.http.MediaType;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.MvcResult;
import org.springframework.test.web.servlet.RequestBuilder;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;
import org.springframework.web.context.WebApplicationContext;

import com.AMRCapstone.AMRCapstone.Codes;
import com.AMRCapstone.AMRCapstone.access.QRAccess;
import com.AMRCapstone.AMRCapstone.access.QR_Queue;
import com.AMRCapstone.AMRCapstone.access.RobotAccess;
import com.AMRCapstone.AMRCapstone.model.QR;
import com.AMRCapstone.AMRCapstone.model.Robot;
import com.AMRCapstone.AMRCapstone.service.RobotService;
import com.fasterxml.jackson.databind.ObjectMapper;

@SpringBootTest
public class RobotControllerTest {

    // private RobotService robotService;

    // public void createRobotService(RobotService robotService) {
    // this.robotService = robotService;
    // }

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
        QR_Queue.resetQueue(temp9);
    }

    // @Test
    // void testGet() {
    // initialize();
    // createRobotService(new RobotService());
    // assertTrue(RobotAccess.getRobot().equals(robotService.get()), "");
    // }

    @Autowired
    private WebApplicationContext webApplicationContext;
    private MockMvc mockMvc;

    @BeforeEach
    void printApplicationContext() {
        mockMvc = MockMvcBuilders.webAppContextSetup(webApplicationContext).build();
        // This
        Arrays.stream(webApplicationContext.getBeanDefinitionNames())
                .map(name -> webApplicationContext.getBean(name).getClass().getName())
                .sorted()
                .forEach(System.out::println);
    }

    private String baseRobotToStringExpected() {
        Robot temp = new Robot(1, "Inactive", "Connecting", 0, 0, 0, 0, 0, null, new ArrayList<String>(), null);
        temp.addtoLoggerList("Waiting for robot to connect");
        // temp.setUserSignal("Forward");
        return temp.toString();
        // "{\"id\":1,\"status\":\"Inactive\",\"message\":\"Connecting\",\"x_pos\":0.0,\"y_pos\":0.0,\"rotation\":0.0,\"x_destination\":0.0,\"y_destination\":0.0,\"qrScan\":null,\"loggerList\":[\"Waiting
        // for robot to connect\"],\"userSignal\":null,\"image\":null}";
    }

    @Test
    void testGetRobot() throws Exception {
        initialize();
        // Creating a GET request
        RequestBuilder request = MockMvcRequestBuilders.get("/robot");
        MvcResult result = mockMvc.perform(request).andReturn();

        // Extract the content from the response
        String content = result.getResponse().getContentAsString();

        // Compare the content with the expected string
        assertEquals(baseRobotToStringExpected(), content, "Response was not as expected");
    }

    @Test
    void testGetUserControl() throws Exception {
        initialize();
        // Creating a GET request
        RequestBuilder request = MockMvcRequestBuilders.get("/robot/user");
        MvcResult result = mockMvc.perform(request).andReturn();

        // Extract the content from the response
        String content = result.getResponse().getContentAsString();

        // Compare the content with the expected string
        // null value will be sent back as ""
        assertEquals("", content, "Response was not as expected");
    }

    @Test
    void testUpdateRobot() throws Exception {
        initialize();
        // Prepare the Robot object and populate it with data
        Robot robot = new Robot(1, Codes.statusActive, "Connecting", 3, 2, 35, 1, 2, null, new ArrayList<String>(),
                null);

        // Create a PUT request with the serialized JSON request body
        RequestBuilder request = MockMvcRequestBuilders.put("/robot")
                .contentType(MediaType.APPLICATION_JSON)
                .content(new ObjectMapper().writeValueAsString(robot))
                .accept(MediaType.APPLICATION_JSON); // Send the PUT request and receive the response
        MvcResult result = mockMvc.perform(request)
                .andExpect(MockMvcResultMatchers.status().isOk())
                .andReturn();

        // Extract the content from the response
        String content = result.getResponse().getContentAsString();

        // Verify the response
        assertNotNull(content, "Response content should not be empty");
        if (content.isEmpty()) {
            fail("Response content is empty");
        }

        // Convert the content to a float[] using Jackson ObjectMapper
        float[] response = new ObjectMapper().readValue(content, float[].class);

        // Expected float[] response based on the input
        float[] expectedResponse = { 3, 3 };

        // (response.length == 2? (response[0] + " " + response[1]) : (response[0] + " "
        // + response[1] + " " + response[2] + " " + response[3]))

        // Compare the content with the expected float[] response
        assertArrayEquals(expectedResponse, response,
                "Response was not as expected: [" + (response.length == 2 ? (response[0] + " " + response[1])
                        : (response[0] + " " + response[1] + " " + response[2] + " " + response[3]) + "]"));

        robot.setQrScan("test9");

        // Create a PUT request with the serialized JSON request body
        request = MockMvcRequestBuilders.put("/robot")
                .contentType(MediaType.APPLICATION_JSON)
                .content(new ObjectMapper().writeValueAsString(robot))
                .accept(MediaType.APPLICATION_JSON); // Send the PUT request and receive the response
        result = mockMvc.perform(request)
                .andExpect(MockMvcResultMatchers.status().isOk())
                .andReturn();

        // Extract the content from the response
        content = result.getResponse().getContentAsString();

        // Verify the response
        assertNotNull(content, "Response content should not be empty");
        if (content.isEmpty()) {
            fail("Response content is empty");
        }

        // Convert the content to a float[] using Jackson ObjectMapper
        response = new ObjectMapper().readValue(content, float[].class);

        // Expected float[] response based on the input
        expectedResponse = new float[4];
        expectedResponse[0] = 2;
        expectedResponse[1] = 3;
        expectedResponse[2] = 3;
        expectedResponse[3] = 3;

        // (response.length == 2? (response[0] + " " + response[1]) : (response[0] + " "
        // + response[1] + " " + response[2] + " " + response[3]))

        // Compare the content with the expected float[] response
        assertArrayEquals(expectedResponse, response,
                "Response was not as expected: [" + (response.length == 2 ? (response[0] + " " + response[1])
                        : (response[0] + " " + response[1] + " " + response[2] + " " + response[3]) + "]"));

    }
}
