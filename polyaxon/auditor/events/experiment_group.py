import auditor

from event_manager.events import experiment_group

auditor.subscribe(experiment_group.ExperimentGroupCreatedEvent)
auditor.subscribe(experiment_group.ExperimentGroupUpdatedEvent)
auditor.subscribe(experiment_group.ExperimentGroupDeletedEvent)
auditor.subscribe(experiment_group.ExperimentGroupViewedEvent)
auditor.subscribe(experiment_group.ExperimentGroupStoppedEvent)
auditor.subscribe(experiment_group.ExperimentGroupResumedEvent)
auditor.subscribe(experiment_group.ExperimentGroupFinishedEvent)
auditor.subscribe(experiment_group.ExperimentGroupExperimentsViewedEvent)
auditor.subscribe(experiment_group.ExperimentGroupIterationEvent)
auditor.subscribe(experiment_group.ExperimentGroupRandomEvent)
auditor.subscribe(experiment_group.ExperimentGroupGridEvent)
auditor.subscribe(experiment_group.ExperimentGroupHyperbandEvent)
auditor.subscribe(experiment_group.ExperimentGroupBOEvent)
