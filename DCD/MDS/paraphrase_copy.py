import csv
import numpy as np
from sklearn.manifold import MDS
from matplotlib import pyplot as plt

if __name__ == '__main__':
    np.set_printoptions(suppress=True)

    count = [[0 for i in range(169)] for j in range(169)]
    with open("/home/jiangdingyi/jdy/force/DCD/data/DD3.csv","r") as f:
        data = csv.reader(f)
        for row in data:
            count[int(row[0])-1][int(row[1])-1] += 1


    with open("/home/jiangdingyi/jdy/force/DCD/data/DD4.csv","r") as f:
        data = csv.reader(f)
        for row in data:
            count[int(row[0])-1][int(row[1])-1] += 1


    with open("/home/jiangdingyi/jdy/force/DCD/data/DD5.csv","r") as f:
        data = csv.reader(f)

        for row in data:
            count[int(row[0])-1][int(row[1])-1] += 1

    for i in range(169):
        for j in range(169):
            if count[i][j] == 0:
                count[i][j] = 99
            else:
                count[i][j] = (1/count[i][j]) * 90
    # print(count)
    d_name = ["Exposure to forces of nature","Environmental heat and cold exposure","Ebola","Conflict and terrorism","Typhoid and paratyphoid","Other malignant neoplasms","Other cardiovascular and circulatory diseases","Invasive Non-typhoidal Salmonella (iNTS)","Whooping cough","Tetanus","Measles","Varicella and herpes zoster","Malaria","Chagas disease","Leishmaniasis","Protein-energy malnutrition","Iodine deficiency","Vitamin A deficiency","Dietary iron deficiency","Other nutritional deficiencies","Sexually transmitted infections excluding HIV","Tuberculosis","HIV/AIDS","Diarrheal diseases","Other intestinal infectious diseases","Lower respiratory infections","Upper respiratory infections","Otitis media","Meningitis","Encephalitis","Appendicitis","Paralytic ileus and intestinal obstruction","Inguinal, femoral, and abdominal hernia","Inflammatory bowel disease","Endocrine, metabolic, blood and immune disorders","Rheumatoid arthritis","Osteoarthritis","Low back pain","Neck pain","African trypanosomiasis","Schistosomiasis","Cysticercosis","Cystic echinococcosis","Lymphatic filariasis","Onchocerciasis","Trachoma","Dengue","Yellow fever","Lip and oral cavity cancer","Nasopharynx cancer","Other pharynx cancer","Gallbladder and biliary tract cancer","Pancreatic cancer","Malignant skin melanoma","Other digestive diseases","Alzheimer's disease and other dementias","Parkinson's disease","Idiopathic epilepsy","Multiple sclerosis","Motor neuron disease","Other neurological disorders","Schizophrenia","Drug use disorders","Depressive disorders","Bipolar disorder","Anxiety disorders","Eating disorders","Viral skin diseases","Acne vulgaris","Pancreatitis","Other musculoskeletal disorders","Congenital birth defects","Other mental disorders","Diabetes mellitus","Acute glomerulonephritis","Chronic kidney disease","Urinary diseases and male infertility","Gynecological diseases","Other unintentional injuries","Self-harm","Interpersonal violence","Food-borne trematodiases","Other neglected tropical diseases","Road injuries","Other transport injuries","Falls","Drowning","Fire, heat, and hot substances","Poisonings","Gout","Diphtheria","Stomach cancer","Liver cancer","Larynx cancer","Tracheal, bronchus and lung cancer","Breast cancer","Cervical cancer","Uterine cancer","Prostate cancer","Non-melanoma skin cancer","Ovarian cancer","Testicular cancer","Kidney cancer","Bladder cancer","Brain and central nervous system cancer","Thyroid cancer","Mesothelioma","Hodgkin lymphoma","Non-Hodgkin lymphoma","Multiple myeloma","Leukemia","Dermatitis","Psoriasis","Scabies","Fungal skin diseases","Alopecia areata","Pruritus","Non-rheumatic valvular heart disease","Chronic obstructive pulmonary disease","Pneumoconiosis","Asthma","Interstitial lung disease and pulmonary sarcoidosis","Other chronic respiratory diseases","Cirrhosis and other chronic liver diseases","Urticaria","Decubitus ulcer","Other skin and subcutaneous diseases","Age-related and other hearing loss","Other sense organ diseases","Oral disorders","Colon and rectum cancer","Rabies","Intestinal nematode infections","Maternal disorders","Neonatal disorders","Autism spectrum disorders","Attention-deficit/hyperactivity disorder","Conduct disorder","Idiopathic developmental intellectual disability","Exposure to mechanical forces","Headache disorders","Acute hepatitis","Leprosy","Other unspecified infectious diseases","Esophageal cancer","Adverse effects of medical treatment","Animal contact","Other neoplasms","Rheumatic heart disease","Ischemic heart disease","Stroke","Hypertensive heart disease","Executions and police conflict","Zika virus","Guinea worm disease","Hemoglobinopathies and hemolytic anemias","Alcohol use disorders","Sudden infant death syndrome","Bacterial skin diseases","Blindness and vision loss","Upper digestive system diseases","Vascular intestinal disorders","Gallbladder and biliary diseases","Peripheral artery disease","Endocarditis","Cardiomyopathy and myocarditis","Atrial fibrillation and flutter","Aortic aneurysm","Foreign body"]
    d_labels = [2,2,1,2,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1,0,1,1,2,2,2,1,1,2,2,2,2,2,2,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,0,2,0,1,1,1,0,2,2,0,0,0,0,0,2,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,2]
    mds = MDS(random_state=0)
    X_norm = mds.fit_transform(count)
    color = ['r', 'g', 'b']
    # print(X_transform)
    # with open("/home/jiangdingyi/jdy/force/DCD/MDS/result.csv", 'w') as f:
    #     write = csv.writer(f)
    #     write.writerows(count)
    # plt.scatter(X_transform[:,0], X_transform[:,1])
    plt.title('Embedding in 2D')
        # plt.scatter(X_norm[i, 0], X_norm[i, 1], c = color[K_labels.labels_[i]])
    for i in range(X_norm.shape[0]):
        plt.scatter(X_norm[i, 0], X_norm[i, 1], c = color[d_labels[i]])
    #plt.annotate(d_name[i], xy = (X_norm[i, 0], X_norm[i, 1]), xytext = (X_norm[i, 0], X_norm[i, 1])) # 这里xy是需要标记的坐标，xytext是对应的标签坐标
    # plt.scatter(X_tsne[:,0], X_tsne[:,1])
    plt.tight_layout()
    # plt.subplots_adjust(wspace=.4, hspace=0.5)
    plt.savefig('/home/jiangdingyi/jdy/force/DCD/MDS/plot2.png', dpi=1000)


