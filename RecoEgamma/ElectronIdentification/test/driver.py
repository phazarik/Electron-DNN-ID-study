import os, sys, argparse

parser=argparse.ArgumentParser()
parser.add_argument('--dryrun' ,type=bool,required=False,help='Check If everything is correct before submitting')
parser.add_argument('--test'   ,type=bool,required=False,help='Submit one file')
args=parser.parse_args()

dryrun = args.dryrun
test   = args.test
campaign = 'Run3Summer22'

#clear the old ntuples:
print('cleaning old stuff ...')
os.system('mkdir -p ntuples/')
os.system('rm -rf ntuples/*')
print('')

#samples that I want to run on:
samplenames = ['dy','taugun','gjet','qcd']

filedict = {
    # DYJetsToLL_M-50:
    "/store/mc/Run3Summer22MiniAODv3/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/MINIAODSIM/forPOG_124X_mcRun3_2022_realistic_v12-v4/70000/091cb0d6-d3c0-4400-915f-4cc2e0ceade2.root":
    "ntuples/dy_1.root",
    "/store/mc/Run3Summer22MiniAODv3/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/MINIAODSIM/forPOG_124X_mcRun3_2022_realistic_v12-v4/70000/0c4fd62e-6ebd-4ea4-b9d2-6a9d1fac97e1.root":
    "ntuples/dy_2.root",
    "/store/mc/Run3Summer22MiniAODv3/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8/MINIAODSIM/forPOG_124X_mcRun3_2022_realistic_v12-v4/70000/0f3a8d22-8a0a-4341-8329-910d40a7bad3.root":
    "ntuples/dy_1.root",
    #TauGun
    "/store/mc/Run3Summer22EEMiniAODv3/TauGun_E-10to100_13p6TeV_pythia8/MINIAODSIM/124X_mcRun3_2022_realistic_postEE_v1-v2/2810000/2529abe9-a4c2-42c3-8dc5-b3ec067efa2a.root":
    "ntuples/taugun_10to100.root",
    "/store/mc/Run3Summer22MiniAODv3/TauGun_E-100to3000_13p6TeV_pythia8/MINIAODSIM/124X_mcRun3_2022_realistic_v12-v2/2820000/0c7bd61f-d49f-499b-a87c-15232fb4f16b.root":
    "ntuples/taugun_100to3000.root",
    "/store/mc/Run3Summer22MiniAODv3/TauGun_E-100to3000_13p6TeV_pythia8/MINIAODSIM/124X_mcRun3_2022_realistic_v12-v2/2820000/4d41e80d-4f52-44f6-b452-83f0b4e3e34c.root":
    "ntuples/taugun_100to3000.root",
    #GJet
    "/store/mc/Run3Summer22MiniAODv3/GJet_PT-10to40_DoubleEMEnriched_TuneCP5_13p6TeV_pythia8/MINIAODSIM/124X_mcRun3_2022_realistic_v12-v2/2820000/01de4b51-1cfd-4050-98a4-da9148e444b4.root":
    "ntuples/gjet_10to40.root",
    "/store/mc/Run3Summer22MiniAODv3/GJet_PT-40_DoubleEMEnriched_TuneCP5_13p6TeV_pythia8/MINIAODSIM/124X_mcRun3_2022_realistic_v12-v2/2820000/13a07048-c90a-4d2d-bada-1379e6b7b301.root":
    "ntuples/gjet_2.root",
    "/store/mc/Run3Summer22MiniAODv3/GJet_PT-40_DoubleEMEnriched_TuneCP5_13p6TeV_pythia8/MINIAODSIM/124X_mcRun3_2022_realistic_v12-v2/2820000/208a9014-0e0f-490b-9e45-a3c13bcf3ff0.root":
    "ntuples/gjet_3.root",
    #QCD
    "/store/mc/Run3Summer22MiniAODv3/QCD_PT-10to30_EMEnriched_TuneCP5_13p6TeV_pythia8/MINIAODSIM/124X_mcRun3_2022_realistic_v12-v2/2810000/6e56d96b-f855-4767-b75e-d767a36c731d.root":
    "ntuples/qcd_10to30.root",
    "/store/mc/Run3Summer22MiniAODv3/QCD_PT-30to50_EMEnriched_TuneCP5_13p6TeV_pythia8/MINIAODSIM/124X_mcRun3_2022_realistic_v12-v2/2820000/58cd6ddc-f242-4004-95ac-208f419da5b9.root":
    "ntuples/qcd_30to50.root",
    "/store/mc/Run3Summer22MiniAODv3/QCD_PT-50to80_EMEnriched_TuneCP5_13p6TeV_pythia8/MINIAODSIM/124X_mcRun3_2022_realistic_v12-v2/2810000/1ec818d6-8a0a-4151-bedd-e9b2c49625fe.root":
    "ntuples/qcd_50to80.root",
    "/store/mc/Run3Summer22MiniAODv3/QCD_PT-80to120_EMEnriched_TuneCP5_13p6TeV_pythia8/MINIAODSIM/124X_mcRun3_2022_realistic_v12-v2/2810000/1688bdfb-6e1a-4699-b103-8ce62d70bf1a.root":
    "ntuples/qcd_80to120.root",
    "/store/mc/Run3Summer22MiniAODv3/QCD_PT-120to170_EMEnriched_TuneCP5_13p6TeV_pythia8/MINIAODSIM/124X_mcRun3_2022_realistic_v12-v2/2810000/1cc04019-6c3d-40bb-b0bd-d4b69c37119b.root":
    "ntuples/qcd_120to170.root",
    "/store/mc/Run3Summer22MiniAODv3/QCD_PT-170to300_EMEnriched_TuneCP5_13p6TeV_pythia8/MINIAODSIM/124X_mcRun3_2022_realistic_v12-v2/2820000/0c103a02-f1b9-425f-8cd9-64f4b88fc6e2.root":
    "ntuples/qcd_170to300.root",
    "/store/mc/Run3Summer22MiniAODv3/QCD_PT-300toInf_EMEnriched_TuneCP5_13p6TeV_pythia8/MINIAODSIM/124X_mcRun3_2022_realistic_v12-v2/2820000/6bf8db20-d8a8-42be-b33b-0b21f59dfad2.root":
    "ntuples/qcd_300.root",
}

count = 0
drycount = 0
for INFILE, OUTFILE in filedict.items():
    for name in samplenames:
        if OUTFILE.startswith(f'ntuples/{name}'):
            print(f'\033[93mproducing {OUTFILE} ...\033[0m')
            processline = f'cmsRun testElectronMVA_cfg.py {INFILE} {OUTFILE}'
            drycount = drycount+1
            if dryrun == True: print(f'processline = {processline}')
            else :
                print(f'processline = {processline}')
                os.system(processline)
                count = count+1
            
            if test == True: break

#Summary
print('')
print('-' * 50)
print('\033[93mSUMMARY\033[0m')
print(f'Samples = {samplenames}')
print(f'No of input files (attempted) = {drycount}')
print(f'No of input files (ran) = {count}')
print('-' * 50)

#Cleaning up:
print('\nCLEANING UP ....')
for name in samplenames:
    for filename in os.listdir('ntuples'):
        if filename.startswith(name):
            hadd_and_clean = f'hadd ntuples/ntuple_{campaign}_{name}.root ntuples/{name}* && rm -rf ntuples/{name}*' 
            if(dryrun==True): print(hadd_and_clean)
            else: os.system(hadd_and_clean)
            break

print('Done!')
