import pytest 
import requests 
import json 


BASE_URL = "https://postman-echo.com" 

    
def test_1_get_with_query_params(): 
    params = {"user": "Denis", "role": "tester", "page": "1"} 
    response = requests.get( 
        f"{BASE_URL}/get", 
        params=params, 
        headers={"Accept": "application/json"} 
    ) 
        
    assert response.status_code == 200 
    resp_json = response.json()         
    assert resp_json["args"] == params 
        
def test_2_get_with_body(): 
    response = requests.get( 
        f"{BASE_URL}/get", 
        data=json.dumps({"unexpected": "data"}), 
        headers={"Content-Type": "application/json"} 
    ) 
        
    assert response.status_code == 200 
    resp_json = response.json()       
    assert "unexpected" in resp_json.get("args", {}) 
        
def test_3_post_json_body(): 
    payload = {"taskId": 1, "title": "Automation tests", "completed": False} 
            
    response = requests.post( 
        f"{BASE_URL}/post", 
        json=payload, 
        headers={"Content-Type": "application/json"} 
    ) 
            
    assert response.status_code == 200 
    resp_json = response.json()         
    assert resp_json["json"] == payload 
                       
def test_4_invalid_method_for_get(): 
    response = requests.post( 
        f"{BASE_URL}/get", 
        json={"test": "bad_method"} 
    ) 
    
    assert response.status_code == 404 
        
def test_5_put_methods(): 
    put_response = requests.put(
        f"{BASE_URL}/post", 
        json={"change": "all"}
    ) 
    
    assert put_response.status_code == 404 

def test_6_delete_methods():   
    delete_response = requests.delete(f"{BASE_URL}/post") 
    
    assert delete_response.status_code == 404