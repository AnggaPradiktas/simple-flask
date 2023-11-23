from flask import Flask, jsonify, request, make_response
from model import Data

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/karyawan', methods=['GET','POST','PUT','DELETE'])
def karyawan():
  try:
    dt = Data()
    values = ()

    if request.method == 'GET':
      id_ = request.args.get("id")
      if id_:
        query = f"SELECT * FROM KARYAWAN WHERE id = ? "
        values = (id_,)
      else:
        query = "SELECT * FROM KARYAWAN;"
      data = dt.get_data(query, values)
    
    elif request.method == 'POST':
      datainput = request.json
      id = datainput['id']
      nama = datainput['nama']
      pekerjaan = datainput['pekerjaan']
      usia = datainput['usia']

      query = "INSERT INTO KARYAWAN (id, nama, pekerjaan, usia) VALUES (?, ?, ?, ?) "
      values = (id, nama, pekerjaan, usia)
      dt.insert_data(query, values)
      data = [{
        'pesan': 'berhasil menambah data'
      }]

    elif request.method == 'PUT':
      query = "UPDATE KARYAWAN SET id = ? "
      datainput = request.json
      id_ = datainput['id']
      values += (id_,)

      if 'nama' in datainput:
        nama = datainput['nama']
        values += (nama,)
        query += ", nama = ?"
      if 'pekerjaan' in datainput:
        pekerjaan = datainput['pekerjaan']
        values += (pekerjaan,)
        query += ", pekerjaan = ?"
      if 'usia' in datainput:
        usia = datainput['usia']
        values += (usia,)
        query += ", usia = ?"

      query += " where id = ? "
      values += (id_,)
      dt.insert_data(query, values)
      data = [{
        'pesan': 'berhasil mengubah data'
      }]

    else:
      query = "DELETE FROM KARYAWAN WHERE id = ? "
      id_ = request.args.get('id')
      values = (id_,)
      dt.insert_data(query, values)
      data = [{
        'pesan': 'berhasil menghapus data'
      }]
      
  except Exception as e:
    return make_response(jsonify({'error': str(e)}), 400)
  return make_response(jsonify({'data': data}), 200)

if __name__ == "__main__":
  app.run(port=8080)
