<html>
  <head>
      <title>Gestore database</title>
  </head>
  <body>
    <form method="post" action="/">
        <fieldset>
            <legend>Campi da compilare</legend>
            <ul>
                <li>azione:
                    <select name="azione" >
                        <option value="add">aggiungi</option>
                        <option value="delete">elimina</option>
                        <option value="show" selected="selected">mostra</option>
                    </select>
                </li>
                <li>Tipo: <input name='tipo'>
                </li>
                <li>Nome: <input name='nome'>
                </li>
            </ul><input type='submit' value='Invia'>
        </fieldset>
    </form>

    <p>{{message}}</p>

  </body>
</html>