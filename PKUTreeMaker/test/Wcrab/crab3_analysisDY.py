from WMCore.Configuration import Configuration
config = Configuration()
config.section_("General")
config.General.requestName   = 'DY-4'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.inputFiles = ['Spring16_25nsV1_MC_L1FastJet_AK4PFchs.txt','Spring16_25nsV1_MC_L2Relative_AK4PFchs.txt','Spring16_25nsV1_MC_L3Absolute_AK4PFchs.txt','Spring16_25nsV1_MC_L2L3Residual_AK4PFchs.txt'] #'Fall15_25nsV2_MC_L1FastJet_AK4PFchs.txt','Fall15_25nsV2_MC_L2Relative_AK4PFchs.txt','Fall15_25nsV2_MC_L3Absolute_AK4PFchs.txt','Fall15_25nsV2_MC_L2L3Residual_AK4PFchs.txt']
# Name of the CMSSW configuration file
config.JobType.psetName    = 'analysis.py'
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
config.Data.outputDatasetTag = 'DY-4'

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'



