package com.template

import net.corda.core.contracts.CommandData
import net.corda.core.contracts.Contract
import net.corda.core.contracts.ContractState
import net.corda.core.identity.AbstractParty
import net.corda.core.identity.Party
import net.corda.core.transactions.LedgerTransaction
import net.corda.core.contracts.*
import net.corda.core.transactions.*
import net.corda.core.transactions.BaseTransaction.*
import net.corda.core.schemas.MappedSchema
import net.corda.core.schemas.PersistentState
import net.corda.core.schemas.QueryableState
import net.corda.core.serialization.CordaSerializable
import javax.persistence.Column
import javax.persistence.Entity
import javax.persistence.Table

// *********
// * State *
// *********
data class PatientState(val patientName: String,
                        val doctorName: Party,
                        val hospitalName: Party,
                        val insuranceName: Party,
                        val data: String) : ContractState {
    override val participants: List<Party>get() = listOf(doctorName, hospitalName)
}

// ************
// * Contract *
// ************
class DiagnosisContract : Contract {
    companion object {
        // Used to identify our contract when building a transaction.
        const val DIAGNOSIS_CONTRACT_ID = "com.template.DiagnosisContract"
    }

    // Used to indicate the transaction's intent.
    interface Commands : CommandData {
        class Diagnosis: Commands
        class Verification: Commands
        class Treatment: Commands
        class Progress: Commands
    }

    // A transaction is valid if the verify() function of the contract of all the transaction's input and output states
    // does not throw an exception.
    override fun verify(tx: LedgerTransaction) {
        // Verification logic goes here.
        val command = tx.commands.requireSingleCommand<Commands>()
        requireThat{
        "No diagnosis should be consumed when sending a message".using (tx.inputs.isEmpty())
        "Only one diagnosis should be created per patient".using (tx.outputs.size == 1)
        val out = tx.outputsOfType<PatientState>().single()
        }
    }
}
