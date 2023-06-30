import os, sys

#clear the old ntuples:
os.system('mkdir -p ntuples/')
os.system('rm -rf ntuples/*')

filedict = {
    # TTToSemileptonic:
    "/store/mc/Run3Winter22MiniAOD/TTToSemiLeptonic_TuneCP5_13p6TeV-powheg-pythia8/MINIAODSIM/FlatPU0to70_122X_mcRun3_2021_realistic_v9-v2/2830000/f939bace-2c61-4450-a335-9249b43d47d1.root":
        "ntuples/ttbar_1.root",
    "/store/mc/Run3Winter22MiniAOD/TTToSemiLeptonic_TuneCP5_13p6TeV-powheg-pythia8/MINIAODSIM/FlatPU0to70_122X_mcRun3_2021_realistic_v9-v2/60000/043bce28-0eb0-4977-8279-6c1a86de4cda.root":
        "ntuples/ttbar_2.root",
    "/store/mc/Run3Winter22MiniAOD/TTToSemiLeptonic_TuneCP5_13p6TeV-powheg-pythia8/MINIAODSIM/FlatPU0to70_122X_mcRun3_2021_realistic_v9-v2/60000/0d7a2829-d0bc-462b-af26-4585cbc0defc.root":
        "ntuples/ttbar_3.root",
    
    # DYJetsToLL_M-50:
    "/store/mc/Run3Winter22MiniAOD/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/MINIAODSIM/122X_mcRun3_2021_realistic_v9-v2/60000/491ede9c-df69-46b9-94bf-675b09b330ca.root":
        "ntuples/dy_1.root",
    "/store/mc/Run3Winter22MiniAOD/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/MINIAODSIM/122X_mcRun3_2021_realistic_v9-v2/60000/768ebba4-99f3-43b4-bbde-4766d59716d6.root":
        "ntuples/dy_2.root",
    "/store/mc/Run3Winter22MiniAOD/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/MINIAODSIM/122X_mcRun3_2021_realistic_v9-v2/70000/013465fa-9e4d-47d0-b06f-82b40bdfb2a1.root":
        "ntuples/dy_3.root",
}

for INFILE, OUTFILE in filedict.items():
    #Generate a backup (because tha main code will turn into gibberish)
    os.system('cp -f testElectronMVARun3_cfg.py testBackup.py')    

    processline = f'cmsRun testElectronMVARun3_cfg.py {INFILE} {OUTFILE}'
    print(f'processline = {processline}')
    os.system(processline)

    #Restore the code from the backup:
    os.system('cp -f testBackup.py testElectronMVARun3_cfg.py')

#Cleaning up:
print('\n\nCLEANING UP ....')
os.system('hadd ntuples/ntuple_TTToSemileptonic.root ntuples/ttbar*')
os.system('hadd ntuples/ntuple_DYJetsToLL_M-50.root ntuples/dy*')
os.system('rm -rf ntuples/ttbar*')
os.system('rm -rf ntuples/dy*')

print('Done!')
