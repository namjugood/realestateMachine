import re
from typing import Optional, Dict, Any
import requests
import xml.etree.ElementTree as ET
import json
import logging

def format_phone_number(phone_number: str) -> Optional[str]:
    """
    전화번호 형식을 통일합니다.
    예: 010-1234-5678
    """
    if not phone_number:
        return None
    
    # 숫자만 추출
    numbers = re.sub(r'[^0-9]', '', phone_number)
    
    # 길이가 11자리인 경우 (01012345678)
    if len(numbers) == 11:
        return f"{numbers[:3]}-{numbers[3:7]}-{numbers[7:]}"
    
    # 길이가 10자리인 경우 (0101234567)
    elif len(numbers) == 10:
        return f"{numbers[:3]}-{numbers[3:6]}-{numbers[6:]}"
    
    return phone_number

def format_price(price: float) -> str:
    """
    가격을 한국식 형식으로 변환합니다.W
    예: 1,000,000원
    """
    return f"{price:,.0f}원" 

def callGetApi(url: str, params: dict) -> dict:
    """
    GET 요청을 보내고 응답을 반환합니다.
    """
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        # 응답 형식을 확인하여 텍스트로 반환, json으로 변환
        return xmlToJson(response.text)
    except AttributeError as e:
        logging.error(f"AttributeError")
        logging.error(f"callGetApi 오류: {e}")
        raise e
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTPError")
        print(f"에러 응답: {e.response.text if hasattr(e, 'response') else '응답 없음'}")
        raise e
    except Exception as e:
        logging.error(f"Exception")
        logging.error(f"callGetApi 오류: {e}")
        raise e

def callPostApi(url: str, params: dict) -> dict:
    """
    POST 요청을 보내고 응답을 반환합니다.
    """
    try:
        response = requests.post(url, json=params)
        response.raise_for_status()
        # 응답 형식을 확인하여 텍스트로 반환, json으로 변환
        return xmlToJson(response.text)
    except AttributeError as e:
        logging.error(f"callPostApi 오류: {e}")
        raise e
    except requests.exceptions.HTTPError as e:
        logging.error(f"callPostApi 오류: {e}")
        raise e
    except Exception as e:
        logging.error(f"callPostApi 오류: {e}")
        raise e

def xmlToJson(xml_string: str) -> Dict[str, Any]:
    """
    XML 문자열을 JSON 형식의 딕셔너리로 변환합니다.
    Args: xml_string (str): XML 형식의 문자열
    Returns: Dict[str, Any]: 변환된 JSON 데이터
    Raises: ValueError: XML 파싱 오류 시 발생
    """
    try:
        # XML 파싱
        root = ET.fromstring(xml_string)
        
        def parse_element(element):
            result = {}
            
            # 요소의 속성 처리
            for key, value in element.attrib.items():
                result[f"@{key}"] = value
            
            # 하위 요소 처리
            for child in element:
                child_tag = child.tag.split('}')[-1]  # 네임스페이스 제거
                child_data = parse_element(child)
                
                # 이미 존재하는 태그인 경우 리스트로 변환
                if child_tag in result:
                    if not isinstance(result[child_tag], list):
                        result[child_tag] = [result[child_tag]]
                    result[child_tag].append(child_data)
                else:
                    result[child_tag] = child_data
            
            # 텍스트 내용이 있는 경우 처리
            if element.text and element.text.strip():
                if result:  # 속성이나 하위 요소가 있는 경우
                    result["#text"] = element.text.strip()
                else:  # 텍스트만 있는 경우
                    return element.text.strip()
            
            return result
        
        # 루트 요소 파싱
        result = parse_element(root)
        
        return result
        
    except ET.ParseError as e:
        raise ValueError(f"XML 파싱 오류: {str(e)}")
    except Exception as e:
        raise ValueError(f"데이터 변환 중 오류 발생: {str(e)}")