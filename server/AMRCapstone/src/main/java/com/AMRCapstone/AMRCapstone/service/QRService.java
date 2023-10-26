package com.AMRCapstone.AMRCapstone.service;

import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.web.server.ResponseStatusException;

import com.AMRCapstone.AMRCapstone.Codes;
import com.AMRCapstone.AMRCapstone.access.QRAccess;
import com.AMRCapstone.AMRCapstone.model.QR;

@Service
public class QRService {
    public void updateStatus(String name, String status) {
        QR qr = QRAccess.getQRs().get(name);
        if (qr == null)
            throw new ResponseStatusException(HttpStatus.NOT_FOUND);
        // check message
        if (status.equals(Codes.QRActive) || status.equals(Codes.QRLost))
            qr.setStatus(status);

    }

}
