# This file reads all the XML files extracted from the ZIP file and combines the results into a single csv file

import os
import pandas as pd
import xml.etree.ElementTree as ET

# Define the function to extract data from a single XML file
def xmlfile2results(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Get the nct_id, the clinical trial identifier
    try:
        nctid = root.find('id_info').find('nct_id').text
    except:
        return None

    # Get study type (interventional vs non-interventional)
    try:
        study_type = root.find('study_type').text
    except:
        return None

    # Get intervention type and name
    try:
        intervention_type = root.find('intervention').find('intervention_type').text
    except:
        intervention_type = ''

    if intervention_type == 'Drug':
        try:
            drug = root.find('intervention').find('intervention_name').text
        except:
            drug = ''
    else:
        drug = ''

    # Get brief title and summary, and detailed description
    try:
        brief_title = root.find('brief_title').text
    except:
        brief_title = ''
    try:
        brief_summary = root.find('brief_summary').find('textblock').text
    except:
        brief_summary = ''
    try:
        detailed_description = root.find('detailed_description').find('textblock').text
    except:
        detailed_description = ''

    # Get overall status of trial
    try:
        overall_status = root.find('overall_status').text
    except:
        overall_status = ''

    # Get sponsor name
    try:
        sponsor = root.find('sponsors').find('lead_sponsor').find('agency').text
    except:
        sponsor = ''

    # Get clinical phase of trial
    try:
        phase = root.find('phase').text
    except:
        phase = ''

    # Get name of condition
    try:
        condition = root.find('condition').text
    except:
        condition = '' 

    try:
        study_first_posted = root.find('study_first_posted').text
    except:
        study_first_posted = ''

    try:
        results_first_submitted = root.find('results_first_submitted').text
    except:
        results_first_submitted = ''

    try:
        results_first_posted = root.find('results_first_posted').text
    except:
        results_first_posted = ''

    try:
        primary_completion_date = root.find('primary_completion_date').text
    except:
        primary_completion_date = ''

    data = {
        'nctid': nctid,
        'study_type': study_type,
        'intervention_type': intervention_type,
        'drug': drug,
        'brief_title': brief_title,
        'brief_summary': brief_summary,
        'detailed_description': detailed_description,
        'overall_status': overall_status,
        'sponsor': sponsor,
        'phase': phase,
        'condition': condition,
        # Dates:
        'results_first_submitted': results_first_submitted,
        'study_first_posted': study_first_posted,
        'results_first_posted': results_first_posted,
    }
    return data

# Function to traverse the directory and process all XML files
def process_all_xml_files(root_folder):
    all_data = []
    for subdir, _, files in os.walk(root_folder):
        print('processing folder ' + subdir)
        for file in files:
            if file.endswith('.xml'):
                xml_file_path = os.path.join(subdir, file)
                
                # Check if the file is empty
                if os.path.getsize(xml_file_path) == 0:
                    print(f'Skipping empty file: {xml_file_path}')
                    continue
                
                try:
                    data = xmlfile2results(xml_file_path)
                    all_data.append(data)
                except Exception as e:
                    print(f'Error processing file {xml_file_path}: {e}')
                    continue
                
    return pd.DataFrame(all_data)


# Run the functions (takes about 40min-1h) 
def main():
    root_folder = 'data' # Replace with data folder path
    compiled_data = process_all_xml_files(root_folder)
    compiled_data.to_csv('compiled_clinical_trials_data.csv', index=False)

if __name__ == '__main__':
    main()