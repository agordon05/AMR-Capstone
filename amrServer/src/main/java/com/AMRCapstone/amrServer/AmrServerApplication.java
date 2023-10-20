package com.AMRCapstone.amrServer;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import com.AMRCapstone.amrServer.access.QRAccess;
import com.AMRCapstone.amrServer.access.RobotAccess;

@SpringBootApplication
public class AmrServerApplication {

	public static void main(String[] args) {
		RobotAccess.initialize();
		QRAccess.initialize();
		SpringApplication.run(AmrServerApplication.class, args);
	}

}
