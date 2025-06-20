from fastapi import HTTPException, status


class ResponseHandler:
    @staticmethod
    def success(message, data=None):
        return {"message": message, "data": data}
    
    @staticmethod
    def get_single_success(name, id, data):
        message = f"Details for name {name} with ID {id}"
        return ResponseHandler.success(message, data)
    
    @staticmethod
    def create_success(name, id, data):
        message = f"{name} with ID {id} created successfully"
        return ResponseHandler.success(message, data)
    
    @staticmethod
    def update_success(name, id, data):
        message = f"{name} with ID {id} updated successfully"
        return ResponseHandler.success(message, data)
    
    @staticmethod
    def delete_success(name, id, data):
        message = f"{name } with ID {id} deleted successfully"
        return ResponseHandler.success(message, data)
    
    @staticmethod
    def not_found_error(name="", id=None):
        message = f"{name} with ID {id} not found"
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=message)
    
    @staticmethod
    def invalid_token(name=""):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid {name} token",
            headers={"WWW-Authenticate": "bearer"}
        )