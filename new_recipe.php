<!DOCTYPE PHP>

//example from https://www.webmasterworld.com/new_web_development/3837972.htm

for ($i=1;$i<=$rownums;$i++) { 
 $partname = 'Part' . $i; 
 $descname = 'Desc' . $i; 
 $qname = 'Qty' . $i; 
 $pricename = 'Price' . $i; 
 $extname = 'ExtPrice' . $i; 
 // Maintain existing values in the form, or not. 
 $data[$partname] = (isset($data[$partname]))?$data[$partname]:''; 
 $data[$descname] = (isset($data[$descname]))?$data[$descname]:''; 
 $data[$qname] = (isset($data[$qname]))?$data[$qname]:'0'; 
 $data[$pricename] = (isset($data[$pricename]))?$data[$pricename]:'0.00'; 
 $data[$extname] = (isset($data[$extname]))?$data[$extname]:'0.00'; 
 // Which results in Part1, Desc1 . . . etc., and prepopulated or default values. 
 $rowcontent = ' 
  <td id="ServiceDetailColumn"><input type="text" name="' . $partname . '" id="' . $partname . '" size="15" value="' . $data[$partname] . '"></td> 
  <td id="ServiceDetailColumn"><input type="text" name="' . $descname . '" id="' . $descname . '" size="100" value="' . $data[$descname] . '"></td> 
  <td id="ServiceDetailColumn"><input type="text" name="' . $qname . '" id="' . $qname . '" size="4" value="' . $data[$qname] . '"></td> 
  <td id="ServiceDetailColumn"><input type="text" name="' . $pricename . '" id="' . $pricename . '" size="7" value="' . $data[$pricename] . '"></td> 
  <td id="ServiceDetailColumn"><input type="text" name="' . $extname . '" id="' . $extname . '" size="7" value="' . $data[$extname] . '"></td>'; 
} 
