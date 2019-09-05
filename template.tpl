%rebase("base.html")
  %import stiri_v_vrsto
<table >
<tbody>
    %for i in range(6):
        <tr>
            %for j in range(7):
			<td>
            %if Igra.matrika[5-i][j] == 1:
                <img src="plavi.gif" alt="O">
            %elif Igra.matrika[5-i][j] == 2 :
                <img src="orange.gif" alt="P">
            %else:
                <img src="prazni.gif" alt="">
			%end
			</td>
			%end
        </tr>
	%end
	<tr>
	%for i in range(7):
	%j = i+1
			<td> <form action="/{{i}}/" method= "post"><button type="submit">{{j}}</button></form> </td>
	%end
	</tr>
</tbody>
</table>
%if Igra.stanje == stiri_v_vrsto.ZMAGA_PLAVI:
  <h1>Bravo Plavi!</h1>
  <form action="/nova/" method= "post">
  <button type="submit">Nova Igra</button>
  </form>
%elif Igra.stanje == stiri_v_vrsto.ZMAGA_ORANZNI:
  <h1>Bravo Oranžni!</h1>
  <form action="/nova/" method= "post">
  <button type="submit">Nova Igra</button>
  </form>
%elif Igra.stanje == stiri_v_vrsto.IZENACENO:
  <h1>Izenačeno</h1>
    <form action="/nova/" method= "post">
    <button type="submit">Nova Igra</button>
    </form>
%else:
<form action="/nova/" method= "post">
    <button type="submit">Ponastavi</button>
</form>
</form>
%end
