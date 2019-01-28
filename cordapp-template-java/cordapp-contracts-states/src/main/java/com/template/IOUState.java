package com.template;

import com.google.common.collect.ImmutableList;
import net.corda.core.contracts.ContractState;
import net.corda.core.identity.AbstractParty;
import net.corda.core.identity.Party;

import java.util.List;

/**
 * Define your state object here.
 */
public class IOUState implements ContractState {
    private final Party patient;
    private final int patientId;
    private final String diagnosis;
    private final String treatment;
    private final Party doctor;

    public IOUState(int patientId, Party doctor, Party patient, String diagnosis, String treatment) {
      this.patient = patient;
      this.patientId = patientId;
      this.diagnosis = diagnosis;
      this.treatment = treatment;
      this.doctor = doctor;
    }

    public int getPatientId() {
        return patientId;
    }

    public Party getPatient() {
        return patient;
    }

    public Party getDoctor() {
        return doctor;
    }

    @Override
    public List<AbstractParty> getParticipants() {
        return ImmutableList.of(patient, doctor);
    }
}
