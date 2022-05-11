# Alzheimer-disease-diagnosis-E3
This is the public repository for the Software Engineering course project assigned to group E3.

Technical Report:

Vlad:
Relevant folders:
AD_dem_distrubed_social-_after_relevant - 291 png files 24.8MB
AD_dem_distrubed_social-_after_relevant_Augmented - 20661 png files 1.3GB

AD_dem_wCVD_contribut - 616 png files 53.5MB
AD_dem_wCVD_contribut_Augmented - 43736 png files 2.86GB

DementiaPD-_primary_relevant - 337 png files 28.8MB
DementiaPD-_primary_relevant_Augmented - 23927 png files 1.53GB

Frontotemporal_demt._prim_relevant 408 png files 35.1MB
Frontotemporal_demt._prim_relevant_Augmented - 28968 png files 1.86GB

No_dementia - 293 png files 23.8MB
No_dementia_Augmented - 20803 png files 1.3GB

Non_AD_dem-_Other_primary - 363 png files 31.5MB
Non_AD_dem-_Other_primary_Augmented - 25773 png files 1.67GB

All of the png files in the original folders are slices that we received from Data Pre-Processing.
I received a total of 2370 slices in a .png format, there were 62 residual files that I deleted manually, so from 2308 original slices  (197MB) I obtained a total of 163868 augmented slices (10.5GB).
Using the processing power of my AMD Ryzen 7 4800h, I managed to augment between 1 and 3 original slices per second, obtaining between 50 and 200 augmented files, depending on the size and slice area of the original pictures in that specific processing interval.
This resulted in me obtaining 10.5GB of data in around 30 minutes.
All the data that I generated has been transferred to an External Hard Drive, that will be passed on to the CNN team.

Rares:
Pentru folderele: Vascular_Demt-_secondary, Vascular_Demt-_primary, Vascular_demt__primary, Cognitive normal, AD-dem_wdepress__not_contribut, AD_dem_distrubed_social-_with, cu dimensiunea totala de 898MB, cu 26.943 slice-uri primite de la pre-processing, cu procesorul Intel I5-10300, 2.50GHZ, 4 Core(s), am obtinut la o rate de augmentare de 4.7 slice-uri pe secundă, un total de 231.672 de poze augmentate într-un timp total de 51:15.02, cu dimensiunea totala de 9.09GB pe care le-am transmis la CNN printr-un disk extern.

Cristian:
For the following folders: Uncertain Dementia having 1285 Mb, with 18767 slices, received by the Pre-Processing team, with Intel i7-9750H processor, 2.60 GHz, 6 Core(s), the received augmentation rate was of 8-9 slices per second, a total of 131370 augmented images were generated in a total time of 17:13.03, having 8.84 GB that were sent to the CNN team via an external hard drive.

Ștefana:
Initially, I removed 54 irrelevant photos to get at the number of slices listed below.
For the folders AD_dem_cannot_be_primary_relevant (198 png), AD_dem_woth_list_B_contribut (139 png), AD_dem_woth_unusual_featsubs_demt (87 png), DAT (169 png), DLBD_primary (141 png) and Unc_impair_reversible (141 png) received from the Data Pre-processing API, containing 874 photos in PNG format and a size of 75,9 MB, I generated augmented images at a rate of 18 - 50 per second using the Intel(R) Core(TM) i7-1065G7 CPU @ 1.30GHz 1.50 GHz processor.
After 31:32.88 minutes, 48.010,058 photos with a total size of 4,06 GB were generated and uploaded to CNN through an external drive.
The folders after augmentation: AD_dem_cannot_be_primary_relevant_Augmented (14.058 png), AD_dem_woth_list_B_contribut (9869 png), AD_dem_woth_unusual_featsubs_demt (6177 png), DAT (11.999 png), DLBD_primary (10.011 png) and Unc_impair_reversible (9940 png).

Daria:
For the folders:
0.5_in_memory_only(206 files), AD_dem_visuspatial-_with(266 files), D_dem_wCVD_not_contrib(209 files), AD_dem_wdepresss-_contribut_relevant(260 files), AD_dem_woth_list_B_not_contrib(207 files), Incipient_demt_PTP_relevant(262 files)
with total of 123MB, 1410 slices processed with Intel i7-4720HQ CPU 2.60GHz. Rate of augmentation being 5-30 slices per second, a total of 98700 augmented images processed in 53:13:45 minutes, size of6.47GB, sent to CNN by an external drive 

Antonio:
For the folders AD_Dementia (3872 files ), AD_dem_Language_dysf_after(683 files ), AD_dem_Language_dysf_with(693 files ),  AD_dem_wdepresss-_not_contribut(1286  files ), ASTEA  NU AU LABEL(935 fisiere), DLBD-_primary(1926 files), Unc_ques._Impairment(898 files ) received from pre-processing , in total 9600 files, without the deleted files  ~50-100 . After augmentation i have 720510 images , 730803 with the originals , total size 42.7 GB and one image is between 8 KB and 178 KB. Aproximative time is 57 min 36 sec , the time was estimated with an example of  50 images and a duration of ~18 sec using the processor AMD Ryzen 9 5900HX with Radeon Graphics 3.30 GHz.
Real time can be higher then the estimated time when there are alot of files (ex. 100 000 images)

The Data Augmentation API seeks to produce appropriate augmented pictures in order to improve diagnostic accuracy.