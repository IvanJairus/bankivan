import pymysql
from app import app
from config import mysql
from flask import jsonify, json
from flask import flash, request
from werkzeug.exceptions import HTTPException

# from werkzeug import generate_password_hash, check_password_hash

@app.route('/add', methods=['POST'])
def add_user():
    try:
        _json = request.json
        _nama = _json['nama']
        _alamat = _json['alamat']
        _tempat_lahir = _json['tempat_lahir']
        _tanggal_lahir = _json['tanggal_lahir']
        _no_KTP = _json['no_KTP']
        _no_HP = _json['no_HP']

        try:
            if _nama and _alamat and _tempat_lahir and _tanggal_lahir and _no_KTP and _no_HP and request.method == 'POST':
                sql = "INSERT INTO tbl_karyawan(nama, alamat, tempat_lahir, tanggal_lahir, no_KTP, no_HP) VALUES(%s, %s, %s, %s, %s, %s)"
                data = (_nama, _alamat, _tempat_lahir, _tanggal_lahir, _no_KTP, _no_HP,)
                conn = mysql.connect()
                cursor = mysql.get_db().cursor()
                cursor = conn.cursor()
                cursor.execute(sql, data)
                conn.commit()
                resp = jsonify('User added successfully!')
                resp.status_code = 200
                return resp
            else:
                return not_found()

        except Exception as e:
            handle_exception(e)

            # Don't stop the stream, just ignore the duplicate.

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/users')
def users():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_karyawan")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/user/<int:id>')
def user(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM tbl_karyawan WHERE no_KTP=%s", id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update', methods=['POST'])
def update_user():
    try:
        _json = request.json
        _id = _json['id']
        _nama = _json['nama']
        _alamat = _json['alamat']
        _tempat_lahir = _json['tempat_lahir']
        _tanggal_lahir = _json['tanggal_lahir']
        _no_KTP = _json['no_KTP']
        _no_HP = _json['no_HP']
        # validate the received values
        if _nama and _alamat and _tempat_lahir and _id and _tanggal_lahir and _no_KTP and _no_HP and request.method == 'POST':
            # do not save password as a plain text
            # save edits
            sql = "UPDATE tbl_karyawan SET nama=%s, alamat=%s, tempat_lahir=%s, tanggal_lahir=%s, no_KTP=%s, no_HP=%s WHERE user_id=%s"
            data = (_nama, _alamat, _tempat_lahir, _id, _tanggal_lahir, _no_KTP, _no_HP,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/delete/<int:id>')
def delete_user(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tbl_karyawan WHERE user_id=%s", (id,))
        conn.commit()
        resp = jsonify('User deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        # "name": e.name,
        "description": 'No. KTP sudah ada.',
    })
    response.content_type = "application/json"
    return response

if __name__ == "__main__":
    app.run()