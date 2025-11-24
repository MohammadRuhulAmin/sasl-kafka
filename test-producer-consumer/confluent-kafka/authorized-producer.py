from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
from datetime import datetime
import time

# Configuration for authenticated producer
config = {
    'bootstrap_servers': ['192.168.30.79:9092'], #['host.docker.internal:9092'],#['172.16.48.88:9092'],
    'security_protocol': 'SASL_PLAINTEXT',
    'sasl_mechanism': 'PLAIN',
    # 'sasl_plain_username': 'dashboardx',
    # 'sasl_plain_password': '$$xdsx12!!@@33Xsd',
    'value_serializer': lambda v: json.dumps(v).encode('utf-8'),
    'api_version': (0, 10, 1)
}

def send_message(producer, topic, message):
    try:
        # Add timestamp to message
        message['timestamp'] = datetime.now().isoformat()
        future = producer.send(topic, message)
        result = future.get() #timeout=60
        print(f"✅ Message sent successfully to {topic}")
        print(f"Partition: {result.partition}, Offset: {result.offset}")
        print(f"Message: {message}")
        print("-------------------")
        
    except KafkaError as e:
        print(f"❌ Failed to send message: {str(e)}")

def main():
    try:
        # Create producer instance
        producer = KafkaProducer(**config)
        producer.partitions_for('bbp-etl') 
        print("📡 Connected to Kafka successfully!")
        # Sample messages
        messages = [
        #     {
        # "jobId": "aac0c77f-5d0c-499a-ba41-1ce68961d351",
        # "scheduleId": "6f8972a9-5b14-4e72-b86d-6b61ba5c3728",
        # "scheduleName": "Create New Schedule",
        # "reportType": None,
        # "status": None,
        # "timestamp": None,
        # "createdBy": None,
        # "ipaRole": None,
        # "recipients": {
        #     "id": "9122adf1-7a4c-442d-8da8-bbbce17f6295",
        #     "email": "ruhulamin.cs.dev@gmail.com",
        #     "username": "ipa_management37012",
        #     "phonenumber": "+8801401401406",
        #     "ipaMapingCode": "IPA_BEZA"
        # },
        # "params": {
        #     "endDate": "31-10-2025",
        #     "startDate": "01-10-2025"
        # },
        # "period": "25-10-2025"
        # }
        {
        "CCINE": "SUBMITTED",
        "oss_recommendation": "no",
        "org_tin_no": "123456789012",
        "org_mail": "info@company.com",
        "organization_name_bn": "টেক ইন্ডাস্ট্রিজ লিমিটেড",
        "organization_name_en": "Tech Industries Limited",
        "org_address_bn": "প্লট ২৩, রোড ১৫, গুলশান ১, ঢাকা ১২১২",
        "org_address_en": "Plot 23, Road 15, Gulshan 1, Dhaka 1212",
        "org_factory_address_bn": "সেক্টর ১০, উত্তরা, ঢাকা ১২৩০",
        "org_factory_address_en": "Sector 10, Uttara, Dhaka 1230",
        "org_mobile": "+8801712345678",
        "division_id": "dhaka",
        "holding_no": "H-123/A",
        "district_id": "dhaka",
        "org_ps_id": "gulshan",
        "org_post_code": "1212",
        "ow_type": "private_limited",
        "nationality": "Bangladeshi",
        "ow_designation": "Managing Director",
        "ow_nid": "1234567890123",
        "ow_name": "John Doe",
        "ow_pre_ps_id": "House 123, Road 45, Gulshan 2, Dhaka 1212",
        "ow_per_ps_id": "Village: Rampur, Post: Rampur, Upazila: Savar, District: Dhaka",
        "ow_district_id": "dhaka",
        "ah_industrial_name": "textile",
        "ah_recomendation_no": "REC-2025-001234",
        "ah_recomendation_date": "2025-01-15",
        "ah_sponsor_reg_no": "ISR-2024-567890",
        "ah_sponsor_reg_date": "2024-12-10",
        "ah_sponsor_name": "Bangladesh Investment Development Authority (BIDA)",
        "ah_raw_price_perc": 75,
        "bank_id": "brac_bank",
        "branch_id": "gulshan",
        "tl_no": "TL-2024-DHK-123456",
        "tl_date": "2024-07-01",
        "chamber_id": "Dhaka Chamber of Commerce and Industry (DCCI)",
        "fees_id": "slab_b",
        "undertaking": "true",
        "company_title": "",
        "org_fax": "",
        "contact_person_name": "",
        "owner_section": [],
        "share_percent": "",
        "share_type": "",
        "ah_import_right": "",
        "ah_import_right_currency": "USD",
        "ah_fire_cer_no": "",
        "ah_env_cer_no": "",
        "incorporation_registration_number": "",
        "ah_bond_license": "",
        "adhoc_yearly_proc_capacity": "",
        "adhoc_yearly_proc_capacity_unit": "MT",
        "adhoc_prod_capacity_desc": "",
        "adhoc_prod_capacity_desc_unit": "MT",
        "ah_total_labour": "null",
        "ah_mach_import": "",
        "ah_prod_insp_name": "",
        "adhoc_apply_production": "",
        "adhoc_apply_production_unit": "MT",
        "ah_prod_price": "",
        "ah_prod_price_currency": "BDT",
        "adhoc_items": [],
        "nominated_branch_address": "",
        "tl_org": "",
        "tl_address": "",
        "chamber_type": "",
        "chamber_cert_sl_no": "",
        "chamber_address": "",
        "attachments": {
            "raw_material_list": "https://cdn.example.com/uploads/1762689104470-z4mcqmon5.jpg",
            "registration_certificate": "https://cdn.example.com/uploads/1762689104472-xz0efhqny.jpg"
        },
        "clpia": "CCINE",
        "clpiaId": "74a679c2-f447-4720-885c-269cde535058"
        }
]

        
        # Send each message
        for message in messages:
            send_message(producer, 'bbp-etl', message)
            time.sleep(1)  
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    finally:
        producer.close()
        print("🔒 Producer connection closed")

if __name__ == "__main__":
    main()