import os

from fastapi.testclient import TestClient

from app.main import app

URL = "http://localhost:8000"

json_data_path = os.getcwd() + "/Pytest/"

client = TestClient(app)




# /Users/judhaha/AIOT_fasteyes-3/app/api/routes/user.py
# token_data = send_invite_mail(user_invite.email, user_invite.level, current_user.group_id,
#                               background_tasks=background_tasks)
# with open(os.getcwd() + "/app/api/" + 'invite_token.txt', 'w') as token:
#     token.write(token_data)


# /Users/judhaha/AIOT_fasteyes-3/app/api/routes/authentication.py
# @router.delete('/auth/clear_all_data_no_auth')
# def ClearAllData(db: Session = Depends(get_db)):
#     clear_all_data(db)
#     return "Clear Done"



# /Users/judhaha/AIOT_fasteyes-3/app/server/authentication/crud.py
# def clear_all_data(db: Session):
#     db.begin()
#     try:
#         db.query(bulletin_board).delete()
#         db.query(department).delete()
#         db.query(device).delete()
#         db.query(device_model).delete()
#         db.query(Error_handler).delete()
#         db.query(face).delete()
#         db.query(fasteyes_device).delete()
#         db.query(fasteyes_observation).delete()
#         db.query(fasteyes_output).delete()
#         db.query(fasteyes_uuid).delete()
#         db.query(group).delete()
#         db.query(observation).delete()
#         db.query(role).delete()
#         db.query(staff).delete()
#         db.query(user).delete()
#
#         if os.path.exists(FILE_PATH):
#             if os.path.exists(FILE_PATH + "observation"):
#                 shutil.rmtree(FILE_PATH + "observation")
#
#             if os.path.exists(FILE_PATH + "face"):
#                 shutil.rmtree(FILE_PATH + "face")
#
#         db.commit()
#     except Exception as e:
#         db.rollback()
#         print(str(e))
#         raise UnicornException(name=clear_all_data.__name__, description=str(e), status_code=500)
#     return "Done"



