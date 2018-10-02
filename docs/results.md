<script>
$(document).ready(function () {
  $('.nav-link-results').addClass('link-active');
});

$(function () { $('[data-toggle="tooltip"]').tooltip() })
</script>

# Results

<div class="container container-wide">
  <table class="table table-striped">
    <thead>
      <tr>
        <th class="id right-sep">Identifier</th>
        <th class="ae" data-toggle="tooltip" data-placement="top" title="Average angular error">AE</th>
        <!-- interval-ranges for angular errors -->
        
        <th class="ae-details" data-toggle="tooltip" data-placement="top" title="Average angular error in regions with flow magnitude in range 0.0 - 10.0">
          AE<br><tiny>0-10</tiny></th>
        
        <th class="ae-details" data-toggle="tooltip" data-placement="top" title="Average angular error in regions with flow magnitude in range 10.0 - 40.0">
          AE<br><tiny>10-40</tiny></th>
        
        <th class="ae-details" data-toggle="tooltip" data-placement="top" title="Average angular error in regions with flow magnitude in range 40.0 - 1000000000.0">
          AE<br><tiny>40-1e+09</tiny></th>
        
        <!-- -->
        <th class="ee left-sep" data-toggle="tooltip" data-placement="top" title="Average endpoint error">EE</th>
        <!-- interval-ranges for endpoint errors -->
        
        <th class="ee-details" data-toggle="tooltip" data-placement="top" title="Average endpoint error in regions with flow magnitude in range 0.0 - 10.0">
          EE<br><tiny>0-10</tiny></th>
        
        <th class="ee-details" data-toggle="tooltip" data-placement="top" title="Average endpoint error in regions with flow magnitude in range 10.0 - 40.0">
          EE<br><tiny>10-40</tiny></th>
        
        <th class="ee-details" data-toggle="tooltip" data-placement="top" title="Average endpoint error in regions with flow magnitude in range 40.0 - 1000000000.0">
          EE<br><tiny>40-1e+09</tiny></th>
        
        <!-- -->
        <th class="elapsed left-sep" data-toggle="tooltip" data-placement="top" title="Elapsed time in seconds">Elapsed</th>
      </tr>
    </thead>
      <tr style="border-bottom: 1px solid white;">
        
   <td class="id right-sep"> average </td>
   
   <td class="ae">
  0.443
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.432
  </td>
   
   <td class="ae-details">
  0.310
  </td>
   
   <td class="ae-details">
  0.402
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  9.640
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.703
  </td>
   
   <td class="ee-details">
  7.315
  </td>
   
   <td class="ee-details">
  24.204
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr> 
      
        
      <tr>
      
      
   <td class="id right-sep"> 10-th percentile </td>
   
   <td class="ae">
  0.206
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.204
  </td>
   
   <td class="ae-details">
  0.165
  </td>
   
   <td class="ae-details">
  0.310
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.746
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.706
  </td>
   
   <td class="ee-details">
  3.882
  </td>
   
   <td class="ee-details">
  25.635
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      
        
      <tr>
      
      
   <td class="id right-sep"> 25-th percentile </td>
   
   <td class="ae">
  0.265
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.262
  </td>
   
   <td class="ae-details">
  0.222
  </td>
   
   <td class="ae-details">
  0.506
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.046
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.916
  </td>
   
   <td class="ee-details">
  4.779
  </td>
   
   <td class="ee-details">
  36.600
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      
        
      <tr>
      
      
   <td class="id right-sep"> 50-th percentile </td>
   
   <td class="ae">
  0.392
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.380
  </td>
   
   <td class="ae-details">
  0.317
  </td>
   
   <td class="ae-details">
  0.820
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.183
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.553
  </td>
   
   <td class="ee-details">
  7.368
  </td>
   
   <td class="ee-details">
  49.827
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      
        
      <tr>
      
      
   <td class="id right-sep"> 75-th percentile </td>
   
   <td class="ae">
  0.542
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.539
  </td>
   
   <td class="ae-details">
  0.469
  </td>
   
   <td class="ae-details">
  1.151
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  8.275
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.084
  </td>
   
   <td class="ee-details">
  11.353
  </td>
   
   <td class="ee-details">
  68.247
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      
      
      <tr style="border-bottom: 1px solid white;">
      
      
   <td class="id right-sep"> 90-th percentile </td>
   
   <td class="ae">
  0.740
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.730
  </td>
   
   <td class="ae-details">
  0.726
  </td>
   
   <td class="ae-details">
  1.624
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  30.604
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  5.915
  </td>
   
   <td class="ee-details">
  16.995
  </td>
   
   <td class="ee-details">
  87.254
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.098
  </td>
      

    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0001.jpg">alley_1_0001</a></td>
   
   <td class="ae">
  0.150
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.150
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.666
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.666
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  2.862
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0002.jpg">alley_1_0002</a></td>
   
   <td class="ae">
  0.158
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.159
  </td>
   
   <td class="ae-details">
  0.048
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.734
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.733
  </td>
   
   <td class="ee-details">
  0.977
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.061
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0003.jpg">alley_1_0003</a></td>
   
   <td class="ae">
  0.164
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.169
  </td>
   
   <td class="ae-details">
  0.071
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.801
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.742
  </td>
   
   <td class="ee-details">
  1.831
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.065
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0004.jpg">alley_1_0004</a></td>
   
   <td class="ae">
  0.175
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.181
  </td>
   
   <td class="ae-details">
  0.106
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.870
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.751
  </td>
   
   <td class="ee-details">
  2.235
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.064
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0005.jpg">alley_1_0005</a></td>
   
   <td class="ae">
  0.190
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.197
  </td>
   
   <td class="ae-details">
  0.114
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.910
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.763
  </td>
   
   <td class="ee-details">
  2.485
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.056
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0006.jpg">alley_1_0006</a></td>
   
   <td class="ae">
  0.198
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.205
  </td>
   
   <td class="ae-details">
  0.124
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.954
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.798
  </td>
   
   <td class="ee-details">
  2.606
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0007.jpg">alley_1_0007</a></td>
   
   <td class="ae">
  0.210
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.217
  </td>
   
   <td class="ae-details">
  0.138
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.994
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.844
  </td>
   
   <td class="ee-details">
  2.567
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.062
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0008.jpg">alley_1_0008</a></td>
   
   <td class="ae">
  0.206
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.213
  </td>
   
   <td class="ae-details">
  0.138
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.964
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.791
  </td>
   
   <td class="ee-details">
  2.477
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0009.jpg">alley_1_0009</a></td>
   
   <td class="ae">
  0.204
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.208
  </td>
   
   <td class="ae-details">
  0.173
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.966
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.733
  </td>
   
   <td class="ee-details">
  2.752
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0010.jpg">alley_1_0010</a></td>
   
   <td class="ae">
  0.204
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.203
  </td>
   
   <td class="ae-details">
  0.217
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.967
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.767
  </td>
   
   <td class="ee-details">
  3.201
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0011.jpg">alley_1_0011</a></td>
   
   <td class="ae">
  0.212
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.208
  </td>
   
   <td class="ae-details">
  0.283
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.994
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.817
  </td>
   
   <td class="ee-details">
  4.829
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.060
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0012.jpg">alley_1_0012</a></td>
   
   <td class="ae">
  0.225
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.221
  </td>
   
   <td class="ae-details">
  0.315
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.994
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.809
  </td>
   
   <td class="ee-details">
  5.011
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.062
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0013.jpg">alley_1_0013</a></td>
   
   <td class="ae">
  0.234
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.230
  </td>
   
   <td class="ae-details">
  0.316
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.982
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.778
  </td>
   
   <td class="ee-details">
  5.216
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.060
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0014.jpg">alley_1_0014</a></td>
   
   <td class="ae">
  0.239
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.235
  </td>
   
   <td class="ae-details">
  0.323
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.947
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.752
  </td>
   
   <td class="ee-details">
  4.929
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.054
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0015.jpg">alley_1_0015</a></td>
   
   <td class="ae">
  0.237
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.233
  </td>
   
   <td class="ae-details">
  0.331
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.889
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.724
  </td>
   
   <td class="ee-details">
  4.553
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.064
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0016.jpg">alley_1_0016</a></td>
   
   <td class="ae">
  0.234
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.230
  </td>
   
   <td class="ae-details">
  0.347
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.823
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.723
  </td>
   
   <td class="ee-details">
  3.963
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.134
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0017.jpg">alley_1_0017</a></td>
   
   <td class="ae">
  0.240
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.240
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.709
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.709
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.062
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0018.jpg">alley_1_0018</a></td>
   
   <td class="ae">
  0.278
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.278
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.677
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.677
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.062
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0019.jpg">alley_1_0019</a></td>
   
   <td class="ae">
  0.325
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.326
  </td>
   
   <td class="ae-details">
  0.074
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.923
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.923
  </td>
   
   <td class="ee-details">
  2.200
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0020.jpg">alley_1_0020</a></td>
   
   <td class="ae">
  0.335
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.336
  </td>
   
   <td class="ae-details">
  0.261
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.232
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.192
  </td>
   
   <td class="ee-details">
  3.860
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.065
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0021.jpg">alley_1_0021</a></td>
   
   <td class="ae">
  0.330
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.342
  </td>
   
   <td class="ae-details">
  0.245
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.546
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.087
  </td>
   
   <td class="ee-details">
  4.745
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0022.jpg">alley_1_0022</a></td>
   
   <td class="ae">
  0.328
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.346
  </td>
   
   <td class="ae-details">
  0.226
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.965
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.323
  </td>
   
   <td class="ee-details">
  5.632
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.067
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0023.jpg">alley_1_0023</a></td>
   
   <td class="ae">
  0.341
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.362
  </td>
   
   <td class="ae-details">
  0.228
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.522
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.766
  </td>
   
   <td class="ee-details">
  6.589
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.064
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0024.jpg">alley_1_0024</a></td>
   
   <td class="ae">
  0.336
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.353
  </td>
   
   <td class="ae-details">
  0.266
  </td>
   
   <td class="ae-details">
  0.100
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.350
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.353
  </td>
   
   <td class="ee-details">
  6.783
  </td>
   
   <td class="ee-details">
  15.598
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0025.jpg">alley_1_0025</a></td>
   
   <td class="ae">
  0.321
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.329
  </td>
   
   <td class="ae-details">
  0.278
  </td>
   
   <td class="ae-details">
  0.063
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.801
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.039
  </td>
   
   <td class="ee-details">
  7.128
  </td>
   
   <td class="ee-details">
  14.232
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0026.jpg">alley_1_0026</a></td>
   
   <td class="ae">
  0.302
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.305
  </td>
   
   <td class="ae-details">
  0.270
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.390
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.022
  </td>
   
   <td class="ee-details">
  6.896
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0027.jpg">alley_1_0027</a></td>
   
   <td class="ae">
  0.278
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.279
  </td>
   
   <td class="ae-details">
  0.255
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.052
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.916
  </td>
   
   <td class="ee-details">
  7.342
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0028.jpg">alley_1_0028</a></td>
   
   <td class="ae">
  0.260
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.259
  </td>
   
   <td class="ae-details">
  0.326
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.766
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.727
  </td>
   
   <td class="ee-details">
  9.370
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.099
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0029.jpg">alley_1_0029</a></td>
   
   <td class="ae">
  0.239
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.238
  </td>
   
   <td class="ae-details">
  0.387
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.604
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.598
  </td>
   
   <td class="ee-details">
  5.509
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.067
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0030.jpg">alley_1_0030</a></td>
   
   <td class="ae">
  0.225
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.225
  </td>
   
   <td class="ae-details">
  0.358
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.519
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.519
  </td>
   
   <td class="ee-details">
  4.349
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.062
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0031.jpg">alley_1_0031</a></td>
   
   <td class="ae">
  0.229
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.229
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.476
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.476
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0032.jpg">alley_1_0032</a></td>
   
   <td class="ae">
  0.228
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.228
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.434
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.434
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.061
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0033.jpg">alley_1_0033</a></td>
   
   <td class="ae">
  0.207
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.207
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.395
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.395
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0034.jpg">alley_1_0034</a></td>
   
   <td class="ae">
  0.192
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.192
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.378
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.378
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0035.jpg">alley_1_0035</a></td>
   
   <td class="ae">
  0.187
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.187
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.381
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.381
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0036.jpg">alley_1_0036</a></td>
   
   <td class="ae">
  0.181
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.181
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.379
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.379
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.064
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0037.jpg">alley_1_0037</a></td>
   
   <td class="ae">
  0.190
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.190
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.406
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.406
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.064
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0038.jpg">alley_1_0038</a></td>
   
   <td class="ae">
  0.188
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.188
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.412
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.412
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0039.jpg">alley_1_0039</a></td>
   
   <td class="ae">
  0.236
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.236
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.458
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.458
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0040.jpg">alley_1_0040</a></td>
   
   <td class="ae">
  0.278
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.278
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.636
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.636
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0041.jpg">alley_1_0041</a></td>
   
   <td class="ae">
  0.274
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.274
  </td>
   
   <td class="ae-details">
  0.239
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.814
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.769
  </td>
   
   <td class="ee-details">
  3.618
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0042.jpg">alley_1_0042</a></td>
   
   <td class="ae">
  0.252
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.257
  </td>
   
   <td class="ae-details">
  0.137
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.896
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.752
  </td>
   
   <td class="ee-details">
  4.227
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0043.jpg">alley_1_0043</a></td>
   
   <td class="ae">
  0.255
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.259
  </td>
   
   <td class="ae-details">
  0.188
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.056
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.766
  </td>
   
   <td class="ee-details">
  6.303
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0044.jpg">alley_1_0044</a></td>
   
   <td class="ae">
  0.253
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.250
  </td>
   
   <td class="ae-details">
  0.290
  </td>
   
   <td class="ae-details">
  0.808
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.250
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.761
  </td>
   
   <td class="ee-details">
  9.230
  </td>
   
   <td class="ee-details">
  33.007
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0045.jpg">alley_1_0045</a></td>
   
   <td class="ae">
  0.268
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.252
  </td>
   
   <td class="ae-details">
  0.567
  </td>
   
   <td class="ae-details">
  0.980
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.406
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.706
  </td>
   
   <td class="ee-details">
  13.601
  </td>
   
   <td class="ee-details">
  39.453
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.101
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0046.jpg">alley_1_0046</a></td>
   
   <td class="ae">
  0.258
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.260
  </td>
   
   <td class="ae-details">
  0.209
  </td>
   
   <td class="ae-details">
  0.281
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.105
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.737
  </td>
   
   <td class="ee-details">
  8.531
  </td>
   
   <td class="ee-details">
  19.082
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0047.jpg">alley_1_0047</a></td>
   
   <td class="ae">
  0.261
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.266
  </td>
   
   <td class="ae-details">
  0.150
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.927
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.725
  </td>
   
   <td class="ee-details">
  5.454
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.065
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0048.jpg">alley_1_0048</a></td>
   
   <td class="ae">
  0.275
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.278
  </td>
   
   <td class="ae-details">
  0.216
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.921
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.700
  </td>
   
   <td class="ee-details">
  5.489
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_1_0049.jpg">alley_1_0049</a></td>
   
   <td class="ae">
  0.273
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.266
  </td>
   
   <td class="ae-details">
  0.745
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.727
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.608
  </td>
   
   <td class="ee-details">
  8.136
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.061
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0001.jpg">alley_2_0001</a></td>
   
   <td class="ae">
  0.375
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.376
  </td>
   
   <td class="ae-details">
  0.113
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.712
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.700
  </td>
   
   <td class="ee-details">
  3.480
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0002.jpg">alley_2_0002</a></td>
   
   <td class="ae">
  0.349
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.349
  </td>
   
   <td class="ae-details">
  0.316
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.752
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.715
  </td>
   
   <td class="ee-details">
  5.177
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0003.jpg">alley_2_0003</a></td>
   
   <td class="ae">
  0.322
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.321
  </td>
   
   <td class="ae-details">
  0.457
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.780
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.713
  </td>
   
   <td class="ee-details">
  7.427
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0004.jpg">alley_2_0004</a></td>
   
   <td class="ae">
  0.314
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.311
  </td>
   
   <td class="ae-details">
  0.643
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.816
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.746
  </td>
   
   <td class="ee-details">
  8.967
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0005.jpg">alley_2_0005</a></td>
   
   <td class="ae">
  0.288
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.288
  </td>
   
   <td class="ae-details">
  0.228
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.777
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.742
  </td>
   
   <td class="ee-details">
  6.345
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0006.jpg">alley_2_0006</a></td>
   
   <td class="ae">
  0.276
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.273
  </td>
   
   <td class="ae-details">
  0.627
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.842
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.754
  </td>
   
   <td class="ee-details">
  11.140
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0007.jpg">alley_2_0007</a></td>
   
   <td class="ae">
  0.263
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.261
  </td>
   
   <td class="ae-details">
  0.370
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.862
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.763
  </td>
   
   <td class="ee-details">
  9.225
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.065
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0008.jpg">alley_2_0008</a></td>
   
   <td class="ae">
  0.254
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.249
  </td>
   
   <td class="ae-details">
  0.648
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.912
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.791
  </td>
   
   <td class="ee-details">
  11.088
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0009.jpg">alley_2_0009</a></td>
   
   <td class="ae">
  0.264
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.264
  </td>
   
   <td class="ae-details">
  0.224
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.959
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.889
  </td>
   
   <td class="ee-details">
  7.837
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0010.jpg">alley_2_0010</a></td>
   
   <td class="ae">
  0.261
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.261
  </td>
   
   <td class="ae-details">
  0.265
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.983
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.933
  </td>
   
   <td class="ee-details">
  4.841
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0011.jpg">alley_2_0011</a></td>
   
   <td class="ae">
  0.259
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.259
  </td>
   
   <td class="ae-details">
  0.260
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.020
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.930
  </td>
   
   <td class="ee-details">
  5.672
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.064
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0012.jpg">alley_2_0012</a></td>
   
   <td class="ae">
  0.253
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.237
  </td>
   
   <td class="ae-details">
  0.923
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.139
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.910
  </td>
   
   <td class="ee-details">
  10.583
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0013.jpg">alley_2_0013</a></td>
   
   <td class="ae">
  0.262
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.258
  </td>
   
   <td class="ae-details">
  0.374
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.179
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.990
  </td>
   
   <td class="ee-details">
  7.233
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0014.jpg">alley_2_0014</a></td>
   
   <td class="ae">
  0.260
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.260
  </td>
   
   <td class="ae-details">
  0.250
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.178
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.012
  </td>
   
   <td class="ee-details">
  5.700
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0015.jpg">alley_2_0015</a></td>
   
   <td class="ae">
  0.214
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.209
  </td>
   
   <td class="ae-details">
  0.340
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.169
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.932
  </td>
   
   <td class="ee-details">
  6.977
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0016.jpg">alley_2_0016</a></td>
   
   <td class="ae">
  0.175
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.166
  </td>
   
   <td class="ae-details">
  0.380
  </td>
   
   <td class="ae-details">
  1.577
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.088
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.883
  </td>
   
   <td class="ee-details">
  5.880
  </td>
   
   <td class="ee-details">
  40.852
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0017.jpg">alley_2_0017</a></td>
   
   <td class="ae">
  0.176
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.168
  </td>
   
   <td class="ae-details">
  0.343
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.109
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.918
  </td>
   
   <td class="ee-details">
  5.300
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.065
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0018.jpg">alley_2_0018</a></td>
   
   <td class="ae">
  0.182
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.180
  </td>
   
   <td class="ae-details">
  0.229
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.167
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.037
  </td>
   
   <td class="ee-details">
  3.585
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0019.jpg">alley_2_0019</a></td>
   
   <td class="ae">
  0.214
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.216
  </td>
   
   <td class="ae-details">
  0.187
  </td>
   
   <td class="ae-details">
  0.182
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.391
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.265
  </td>
   
   <td class="ee-details">
  3.493
  </td>
   
   <td class="ee-details">
  24.425
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0020.jpg">alley_2_0020</a></td>
   
   <td class="ae">
  0.223
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.223
  </td>
   
   <td class="ae-details">
  0.221
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.633
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.467
  </td>
   
   <td class="ee-details">
  3.901
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.064
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0021.jpg">alley_2_0021</a></td>
   
   <td class="ae">
  0.227
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.226
  </td>
   
   <td class="ae-details">
  0.233
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.702
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.561
  </td>
   
   <td class="ee-details">
  3.373
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.065
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0022.jpg">alley_2_0022</a></td>
   
   <td class="ae">
  0.221
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.221
  </td>
   
   <td class="ae-details">
  0.221
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.853
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.703
  </td>
   
   <td class="ee-details">
  3.387
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.058
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0023.jpg">alley_2_0023</a></td>
   
   <td class="ae">
  0.216
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.216
  </td>
   
   <td class="ae-details">
  0.216
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.019
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.852
  </td>
   
   <td class="ee-details">
  3.536
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0024.jpg">alley_2_0024</a></td>
   
   <td class="ae">
  0.214
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.210
  </td>
   
   <td class="ae-details">
  0.241
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.136
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.975
  </td>
   
   <td class="ee-details">
  3.367
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0025.jpg">alley_2_0025</a></td>
   
   <td class="ae">
  0.211
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.204
  </td>
   
   <td class="ae-details">
  0.258
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.299
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.107
  </td>
   
   <td class="ee-details">
  3.527
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0026.jpg">alley_2_0026</a></td>
   
   <td class="ae">
  0.215
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.199
  </td>
   
   <td class="ae-details">
  0.291
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.585
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.250
  </td>
   
   <td class="ee-details">
  4.158
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0027.jpg">alley_2_0027</a></td>
   
   <td class="ae">
  0.199
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.188
  </td>
   
   <td class="ae-details">
  0.237
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.531
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.280
  </td>
   
   <td class="ee-details">
  3.390
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0028.jpg">alley_2_0028</a></td>
   
   <td class="ae">
  0.204
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.194
  </td>
   
   <td class="ae-details">
  0.230
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.671
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.410
  </td>
   
   <td class="ee-details">
  3.308
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0029.jpg">alley_2_0029</a></td>
   
   <td class="ae">
  0.196
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.183
  </td>
   
   <td class="ae-details">
  0.218
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.792
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.480
  </td>
   
   <td class="ee-details">
  3.339
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0030.jpg">alley_2_0030</a></td>
   
   <td class="ae">
  0.183
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.170
  </td>
   
   <td class="ae-details">
  0.202
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.907
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.571
  </td>
   
   <td class="ee-details">
  3.343
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.058
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0031.jpg">alley_2_0031</a></td>
   
   <td class="ae">
  0.180
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.164
  </td>
   
   <td class="ae-details">
  0.192
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.001
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.633
  </td>
   
   <td class="ee-details">
  3.273
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.065
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0032.jpg">alley_2_0032</a></td>
   
   <td class="ae">
  0.182
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.152
  </td>
   
   <td class="ae-details">
  0.194
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.207
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.719
  </td>
   
   <td class="ee-details">
  3.410
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.061
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0033.jpg">alley_2_0033</a></td>
   
   <td class="ae">
  0.174
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.153
  </td>
   
   <td class="ae-details">
  0.181
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.180
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.718
  </td>
   
   <td class="ee-details">
  3.334
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0034.jpg">alley_2_0034</a></td>
   
   <td class="ae">
  0.176
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.181
  </td>
   
   <td class="ae-details">
  0.175
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.260
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.837
  </td>
   
   <td class="ee-details">
  3.364
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0035.jpg">alley_2_0035</a></td>
   
   <td class="ae">
  0.174
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.190
  </td>
   
   <td class="ae-details">
  0.171
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.222
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.807
  </td>
   
   <td class="ee-details">
  3.303
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0036.jpg">alley_2_0036</a></td>
   
   <td class="ae">
  0.175
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.211
  </td>
   
   <td class="ae-details">
  0.168
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.264
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.797
  </td>
   
   <td class="ee-details">
  3.350
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0037.jpg">alley_2_0037</a></td>
   
   <td class="ae">
  0.170
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.198
  </td>
   
   <td class="ae-details">
  0.164
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.170
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.801
  </td>
   
   <td class="ee-details">
  3.251
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0038.jpg">alley_2_0038</a></td>
   
   <td class="ae">
  0.169
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.181
  </td>
   
   <td class="ae-details">
  0.165
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.092
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.837
  </td>
   
   <td class="ee-details">
  3.169
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0039.jpg">alley_2_0039</a></td>
   
   <td class="ae">
  0.162
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.154
  </td>
   
   <td class="ae-details">
  0.165
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.029
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.680
  </td>
   
   <td class="ee-details">
  3.196
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0040.jpg">alley_2_0040</a></td>
   
   <td class="ae">
  0.163
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.151
  </td>
   
   <td class="ae-details">
  0.175
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.916
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.642
  </td>
   
   <td class="ee-details">
  3.194
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0041.jpg">alley_2_0041</a></td>
   
   <td class="ae">
  0.159
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.145
  </td>
   
   <td class="ae-details">
  0.184
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.782
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.573
  </td>
   
   <td class="ee-details">
  3.155
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0042.jpg">alley_2_0042</a></td>
   
   <td class="ae">
  0.160
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.146
  </td>
   
   <td class="ae-details">
  0.205
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.645
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.484
  </td>
   
   <td class="ee-details">
  3.127
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0043.jpg">alley_2_0043</a></td>
   
   <td class="ae">
  0.168
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.157
  </td>
   
   <td class="ae-details">
  0.226
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.563
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.464
  </td>
   
   <td class="ee-details">
  3.083
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0044.jpg">alley_2_0044</a></td>
   
   <td class="ae">
  0.180
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.165
  </td>
   
   <td class="ae-details">
  0.296
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.518
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.382
  </td>
   
   <td class="ee-details">
  3.561
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0045.jpg">alley_2_0045</a></td>
   
   <td class="ae">
  0.188
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.179
  </td>
   
   <td class="ae-details">
  0.297
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.312
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.224
  </td>
   
   <td class="ee-details">
  3.433
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0046.jpg">alley_2_0046</a></td>
   
   <td class="ae">
  0.199
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.197
  </td>
   
   <td class="ae-details">
  0.241
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.199
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.163
  </td>
   
   <td class="ee-details">
  2.969
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0047.jpg">alley_2_0047</a></td>
   
   <td class="ae">
  0.200
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.197
  </td>
   
   <td class="ae-details">
  0.332
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.015
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.940
  </td>
   
   <td class="ee-details">
  4.779
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0048.jpg">alley_2_0048</a></td>
   
   <td class="ae">
  0.213
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.207
  </td>
   
   <td class="ae-details">
  0.699
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.065
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.014
  </td>
   
   <td class="ee-details">
  6.123
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/alley_2_0049.jpg">alley_2_0049</a></td>
   
   <td class="ae">
  0.200
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.198
  </td>
   
   <td class="ae-details">
  0.893
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.609
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.595
  </td>
   
   <td class="ee-details">
  7.243
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_2_0001.jpg">ambush_2_0001</a></td>
   
   <td class="ae">
  0.613
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.692
  </td>
   
   <td class="ae-details">
  0.441
  </td>
   
   <td class="ae-details">
  0.626
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  47.903
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  16.095
  </td>
   
   <td class="ee-details">
  13.987
  </td>
   
   <td class="ee-details">
  51.205
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_2_0002.jpg">ambush_2_0002</a></td>
   
   <td class="ae">
  0.548
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.554
  </td>
   
   <td class="ae-details">
  0.548
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  67.818
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  19.401
  </td>
   
   <td class="ee-details">
  69.862
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_2_0003.jpg">ambush_2_0003</a></td>
   
   <td class="ae">
  0.924
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.455
  </td>
   
   <td class="ae-details">
  0.936
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  91.670
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  16.617
  </td>
   
   <td class="ee-details">
  93.643
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_2_0004.jpg">ambush_2_0004</a></td>
   
   <td class="ae">
  0.660
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.610
  </td>
   
   <td class="ae-details">
  0.662
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  92.510
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  19.514
  </td>
   
   <td class="ee-details">
  95.543
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_2_0005.jpg">ambush_2_0005</a></td>
   
   <td class="ae">
  0.714
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.323
  </td>
   
   <td class="ae-details">
  0.826
  </td>
   
   <td class="ae-details">
  0.696
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  78.471
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  26.918
  </td>
   
   <td class="ee-details">
  21.725
  </td>
   
   <td class="ee-details">
  85.992
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_2_0006.jpg">ambush_2_0006</a></td>
   
   <td class="ae">
  0.872
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.378
  </td>
   
   <td class="ae-details">
  0.888
  </td>
   
   <td class="ae-details">
  0.854
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  63.197
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  18.751
  </td>
   
   <td class="ee-details">
  19.896
  </td>
   
   <td class="ee-details">
  77.102
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_2_0007.jpg">ambush_2_0007</a></td>
   
   <td class="ae">
  0.991
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.048
  </td>
   
   <td class="ae-details">
  0.391
  </td>
   
   <td class="ae-details">
  1.060
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  48.657
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  14.191
  </td>
   
   <td class="ee-details">
  13.336
  </td>
   
   <td class="ee-details">
  52.713
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_2_0008.jpg">ambush_2_0008</a></td>
   
   <td class="ae">
  1.085
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.967
  </td>
   
   <td class="ae-details">
  1.466
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  30.661
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  23.260
  </td>
   
   <td class="ee-details">
  54.549
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.065
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_2_0009.jpg">ambush_2_0009</a></td>
   
   <td class="ae">
  0.867
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.377
  </td>
   
   <td class="ae-details">
  0.746
  </td>
   
   <td class="ae-details">
  1.122
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  25.763
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.047
  </td>
   
   <td class="ee-details">
  17.636
  </td>
   
   <td class="ee-details">
  42.746
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.062
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_2_0010.jpg">ambush_2_0010</a></td>
   
   <td class="ae">
  0.817
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.263
  </td>
   
   <td class="ae-details">
  0.728
  </td>
   
   <td class="ae-details">
  1.116
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  27.490
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.613
  </td>
   
   <td class="ee-details">
  17.701
  </td>
   
   <td class="ee-details">
  46.894
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.061
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_2_0011.jpg">ambush_2_0011</a></td>
   
   <td class="ae">
  0.824
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.259
  </td>
   
   <td class="ae-details">
  0.702
  </td>
   
   <td class="ae-details">
  1.179
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  28.683
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.814
  </td>
   
   <td class="ee-details">
  18.133
  </td>
   
   <td class="ee-details">
  51.521
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_2_0012.jpg">ambush_2_0012</a></td>
   
   <td class="ae">
  0.589
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.668
  </td>
   
   <td class="ae-details">
  0.508
  </td>
   
   <td class="ae-details">
  0.633
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  33.514
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  5.540
  </td>
   
   <td class="ee-details">
  12.848
  </td>
   
   <td class="ee-details">
  58.921
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_2_0013.jpg">ambush_2_0013</a></td>
   
   <td class="ae">
  0.658
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.748
  </td>
   
   <td class="ae-details">
  0.617
  </td>
   
   <td class="ae-details">
  0.611
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  54.724
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  7.058
  </td>
   
   <td class="ee-details">
  17.980
  </td>
   
   <td class="ee-details">
  87.254
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.065
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_2_0014.jpg">ambush_2_0014</a></td>
   
   <td class="ae">
  0.740
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.239
  </td>
   
   <td class="ae-details">
  0.740
  </td>
   
   <td class="ae-details">
  0.755
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  65.343
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  26.698
  </td>
   
   <td class="ee-details">
  14.140
  </td>
   
   <td class="ee-details">
  116.755
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.067
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_2_0015.jpg">ambush_2_0015</a></td>
   
   <td class="ae">
  1.027
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.268
  </td>
   
   <td class="ae-details">
  1.028
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  88.972
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  15.305
  </td>
   
   <td class="ee-details">
  88.982
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_2_0016.jpg">ambush_2_0016</a></td>
   
   <td class="ae">
  0.771
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.771
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  57.023
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  57.023
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_2_0017.jpg">ambush_2_0017</a></td>
   
   <td class="ae">
  1.675
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  1.573
  </td>
   
   <td class="ae-details">
  1.815
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  42.459
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  33.267
  </td>
   
   <td class="ee-details">
  55.038
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.063
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_2_0018.jpg">ambush_2_0018</a></td>
   
   <td class="ae">
  1.873
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  1.890
  </td>
   
   <td class="ae-details">
  1.866
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  49.855
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  39.375
  </td>
   
   <td class="ee-details">
  54.067
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_2_0019.jpg">ambush_2_0019</a></td>
   
   <td class="ae">
  1.096
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.875
  </td>
   
   <td class="ae-details">
  1.513
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  34.360
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  25.582
  </td>
   
   <td class="ee-details">
  50.891
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_2_0020.jpg">ambush_2_0020</a></td>
   
   <td class="ae">
  1.342
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  1.342
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  84.247
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  84.247
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.067
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0001.jpg">ambush_4_0001</a></td>
   
   <td class="ae">
  0.916
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.586
  </td>
   
   <td class="ae-details">
  1.683
  </td>
   
   <td class="ae-details">
  2.744
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  10.484
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  5.170
  </td>
   
   <td class="ee-details">
  22.648
  </td>
   
   <td class="ee-details">
  49.311
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0002.jpg">ambush_4_0002</a></td>
   
   <td class="ae">
  0.856
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.729
  </td>
   
   <td class="ae-details">
  1.064
  </td>
   
   <td class="ae-details">
  1.897
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  9.674
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  6.154
  </td>
   
   <td class="ee-details">
  15.209
  </td>
   
   <td class="ee-details">
  49.237
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0003.jpg">ambush_4_0003</a></td>
   
   <td class="ae">
  1.398
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.365
  </td>
   
   <td class="ae-details">
  1.473
  </td>
   
   <td class="ae-details">
  1.624
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  15.639
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  11.584
  </td>
   
   <td class="ee-details">
  24.794
  </td>
   
   <td class="ee-details">
  44.774
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0004.jpg">ambush_4_0004</a></td>
   
   <td class="ae">
  1.527
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.789
  </td>
   
   <td class="ae-details">
  1.686
  </td>
   
   <td class="ae-details">
  1.163
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  75.425
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  24.298
  </td>
   
   <td class="ee-details">
  38.181
  </td>
   
   <td class="ee-details">
  150.033
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0005.jpg">ambush_4_0005</a></td>
   
   <td class="ae">
  1.161
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.168
  </td>
   
   <td class="ae-details">
  1.219
  </td>
   
   <td class="ae-details">
  1.133
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  89.321
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  18.097
  </td>
   
   <td class="ee-details">
  25.443
  </td>
   
   <td class="ee-details">
  139.257
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0006.jpg">ambush_4_0006</a></td>
   
   <td class="ae">
  1.105
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.671
  </td>
   
   <td class="ae-details">
  1.032
  </td>
   
   <td class="ae-details">
  1.308
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  47.713
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  8.172
  </td>
   
   <td class="ee-details">
  22.128
  </td>
   
   <td class="ee-details">
  78.707
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0007.jpg">ambush_4_0007</a></td>
   
   <td class="ae">
  1.354
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.351
  </td>
   
   <td class="ae-details">
  1.060
  </td>
   
   <td class="ae-details">
  1.673
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  67.341
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  13.743
  </td>
   
   <td class="ee-details">
  21.615
  </td>
   
   <td class="ee-details">
  117.900
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0008.jpg">ambush_4_0008</a></td>
   
   <td class="ae">
  0.788
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.862
  </td>
   
   <td class="ae-details">
  0.645
  </td>
   
   <td class="ae-details">
  0.830
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  48.282
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  10.591
  </td>
   
   <td class="ee-details">
  24.420
  </td>
   
   <td class="ee-details">
  55.416
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0009.jpg">ambush_4_0009</a></td>
   
   <td class="ae">
  0.691
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.211
  </td>
   
   <td class="ae-details">
  0.476
  </td>
   
   <td class="ae-details">
  1.032
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  37.388
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  19.109
  </td>
   
   <td class="ee-details">
  11.491
  </td>
   
   <td class="ee-details">
  79.411
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.062
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0010.jpg">ambush_4_0010</a></td>
   
   <td class="ae">
  1.095
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.597
  </td>
   
   <td class="ae-details">
  1.150
  </td>
   
   <td class="ae-details">
  1.813
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  39.005
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.420
  </td>
   
   <td class="ee-details">
  21.563
  </td>
   
   <td class="ee-details">
  101.347
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0011.jpg">ambush_4_0011</a></td>
   
   <td class="ae">
  0.630
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.498
  </td>
   
   <td class="ae-details">
  0.593
  </td>
   
   <td class="ae-details">
  0.885
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  22.913
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  5.677
  </td>
   
   <td class="ee-details">
  12.647
  </td>
   
   <td class="ee-details">
  61.367
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0012.jpg">ambush_4_0012</a></td>
   
   <td class="ae">
  0.642
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.508
  </td>
   
   <td class="ae-details">
  0.426
  </td>
   
   <td class="ae-details">
  1.160
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  23.126
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  5.512
  </td>
   
   <td class="ee-details">
  9.782
  </td>
   
   <td class="ee-details">
  71.135
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0013.jpg">ambush_4_0013</a></td>
   
   <td class="ae">
  0.561
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.475
  </td>
   
   <td class="ae-details">
  0.440
  </td>
   
   <td class="ae-details">
  0.916
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  21.015
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  18.987
  </td>
   
   <td class="ee-details">
  12.486
  </td>
   
   <td class="ee-details">
  53.326
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.063
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0014.jpg">ambush_4_0014</a></td>
   
   <td class="ae">
  0.364
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.081
  </td>
   
   <td class="ae-details">
  0.325
  </td>
   
   <td class="ae-details">
  0.490
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  12.751
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  10.251
  </td>
   
   <td class="ee-details">
  10.690
  </td>
   
   <td class="ee-details">
  33.147
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0015.jpg">ambush_4_0015</a></td>
   
   <td class="ae">
  0.321
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.310
  </td>
   
   <td class="ae-details">
  0.291
  </td>
   
   <td class="ae-details">
  0.409
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  11.162
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.848
  </td>
   
   <td class="ee-details">
  8.494
  </td>
   
   <td class="ee-details">
  32.120
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.063
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0016.jpg">ambush_4_0016</a></td>
   
   <td class="ae">
  0.361
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.903
  </td>
   
   <td class="ae-details">
  0.336
  </td>
   
   <td class="ae-details">
  0.430
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  15.168
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  24.256
  </td>
   
   <td class="ee-details">
  7.556
  </td>
   
   <td class="ee-details">
  44.625
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0017.jpg">ambush_4_0017</a></td>
   
   <td class="ae">
  0.359
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.379
  </td>
   
   <td class="ae-details">
  0.314
  </td>
   
   <td class="ae-details">
  0.451
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  13.290
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  7.142
  </td>
   
   <td class="ee-details">
  8.314
  </td>
   
   <td class="ee-details">
  39.664
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0018.jpg">ambush_4_0018</a></td>
   
   <td class="ae">
  0.502
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.578
  </td>
   
   <td class="ae-details">
  0.427
  </td>
   
   <td class="ae-details">
  0.619
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  11.423
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  5.855
  </td>
   
   <td class="ee-details">
  8.367
  </td>
   
   <td class="ee-details">
  43.599
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0019.jpg">ambush_4_0019</a></td>
   
   <td class="ae">
  0.535
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.533
  </td>
   
   <td class="ae-details">
  0.464
  </td>
   
   <td class="ae-details">
  0.635
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  8.681
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.130
  </td>
   
   <td class="ee-details">
  15.564
  </td>
   
   <td class="ee-details">
  37.602
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0020.jpg">ambush_4_0020</a></td>
   
   <td class="ae">
  0.343
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.004
  </td>
   
   <td class="ae-details">
  0.326
  </td>
   
   <td class="ae-details">
  0.523
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  14.452
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  6.914
  </td>
   
   <td class="ee-details">
  12.890
  </td>
   
   <td class="ee-details">
  41.399
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0021.jpg">ambush_4_0021</a></td>
   
   <td class="ae">
  0.903
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.656
  </td>
   
   <td class="ae-details">
  0.661
  </td>
   
   <td class="ae-details">
  0.926
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  40.936
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  10.752
  </td>
   
   <td class="ee-details">
  20.576
  </td>
   
   <td class="ee-details">
  42.976
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0022.jpg">ambush_4_0022</a></td>
   
   <td class="ae">
  1.217
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.223
  </td>
   
   <td class="ae-details">
  1.238
  </td>
   
   <td class="ae-details">
  1.060
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  34.531
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  17.330
  </td>
   
   <td class="ee-details">
  33.168
  </td>
   
   <td class="ee-details">
  45.331
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0023.jpg">ambush_4_0023</a></td>
   
   <td class="ae">
  0.493
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.405
  </td>
   
   <td class="ae-details">
  0.718
  </td>
   
   <td class="ae-details">
  1.173
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  6.368
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.927
  </td>
   
   <td class="ee-details">
  18.545
  </td>
   
   <td class="ee-details">
  50.698
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0024.jpg">ambush_4_0024</a></td>
   
   <td class="ae">
  0.355
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.254
  </td>
   
   <td class="ae-details">
  0.818
  </td>
   
   <td class="ae-details">
  1.025
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  6.298
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.037
  </td>
   
   <td class="ee-details">
  18.527
  </td>
   
   <td class="ee-details">
  38.219
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0025.jpg">ambush_4_0025</a></td>
   
   <td class="ae">
  0.415
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.943
  </td>
   
   <td class="ae-details">
  0.358
  </td>
   
   <td class="ae-details">
  0.691
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  9.409
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  7.085
  </td>
   
   <td class="ee-details">
  9.565
  </td>
   
   <td class="ee-details">
  41.656
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.067
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0026.jpg">ambush_4_0026</a></td>
   
   <td class="ae">
  0.445
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.996
  </td>
   
   <td class="ae-details">
  0.412
  </td>
   
   <td class="ae-details">
  0.762
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  18.622
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  12.829
  </td>
   
   <td class="ee-details">
  14.410
  </td>
   
   <td class="ee-details">
  178.946
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0027.jpg">ambush_4_0027</a></td>
   
   <td class="ae">
  0.420
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.690
  </td>
   
   <td class="ae-details">
  0.397
  </td>
   
   <td class="ae-details">
  0.422
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  26.252
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  7.402
  </td>
   
   <td class="ee-details">
  8.980
  </td>
   
   <td class="ee-details">
  153.959
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0028.jpg">ambush_4_0028</a></td>
   
   <td class="ae">
  0.551
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.551
  </td>
   
   <td class="ae-details">
  0.747
  </td>
   
   <td class="ae-details">
  0.486
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  34.426
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.570
  </td>
   
   <td class="ee-details">
  14.421
  </td>
   
   <td class="ee-details">
  110.708
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0029.jpg">ambush_4_0029</a></td>
   
   <td class="ae">
  0.484
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.971
  </td>
   
   <td class="ae-details">
  0.472
  </td>
   
   <td class="ae-details">
  0.474
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  25.153
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  6.559
  </td>
   
   <td class="ee-details">
  8.463
  </td>
   
   <td class="ee-details">
  70.994
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.067
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0030.jpg">ambush_4_0030</a></td>
   
   <td class="ae">
  0.507
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.569
  </td>
   
   <td class="ae-details">
  0.476
  </td>
   
   <td class="ae-details">
  0.537
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  18.952
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  11.633
  </td>
   
   <td class="ee-details">
  9.501
  </td>
   
   <td class="ee-details">
  44.174
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0031.jpg">ambush_4_0031</a></td>
   
   <td class="ae">
  0.621
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.967
  </td>
   
   <td class="ae-details">
  0.612
  </td>
   
   <td class="ae-details">
  0.630
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  15.809
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  13.688
  </td>
   
   <td class="ee-details">
  10.658
  </td>
   
   <td class="ee-details">
  39.596
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_4_0032.jpg">ambush_4_0032</a></td>
   
   <td class="ae">
  0.791
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.863
  </td>
   
   <td class="ae-details">
  0.669
  </td>
   
   <td class="ae-details">
  0.305
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  8.437
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.369
  </td>
   
   <td class="ee-details">
  16.252
  </td>
   
   <td class="ee-details">
  33.151
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0001.jpg">ambush_5_0001</a></td>
   
   <td class="ae">
  0.634
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.668
  </td>
   
   <td class="ae-details">
  0.509
  </td>
   
   <td class="ae-details">
  0.339
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.554
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.304
  </td>
   
   <td class="ee-details">
  8.023
  </td>
   
   <td class="ee-details">
  17.567
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0002.jpg">ambush_5_0002</a></td>
   
   <td class="ae">
  0.648
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.694
  </td>
   
   <td class="ae-details">
  0.437
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.592
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.556
  </td>
   
   <td class="ee-details">
  8.364
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.064
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0003.jpg">ambush_5_0003</a></td>
   
   <td class="ae">
  0.689
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.719
  </td>
   
   <td class="ae-details">
  0.512
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.595
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.744
  </td>
   
   <td class="ee-details">
  8.676
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.065
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0004.jpg">ambush_5_0004</a></td>
   
   <td class="ae">
  0.651
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.704
  </td>
   
   <td class="ae-details">
  0.315
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.677
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.293
  </td>
   
   <td class="ee-details">
  5.149
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0005.jpg">ambush_5_0005</a></td>
   
   <td class="ae">
  0.564
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.599
  </td>
   
   <td class="ae-details">
  0.231
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.183
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.880
  </td>
   
   <td class="ee-details">
  5.046
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0006.jpg">ambush_5_0006</a></td>
   
   <td class="ae">
  0.660
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.701
  </td>
   
   <td class="ae-details">
  0.193
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.676
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.527
  </td>
   
   <td class="ee-details">
  4.350
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.065
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0007.jpg">ambush_5_0007</a></td>
   
   <td class="ae">
  0.772
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.803
  </td>
   
   <td class="ae-details">
  0.229
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.063
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.036
  </td>
   
   <td class="ee-details">
  3.540
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.061
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0008.jpg">ambush_5_0008</a></td>
   
   <td class="ae">
  0.825
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.895
  </td>
   
   <td class="ae-details">
  0.287
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.468
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.242
  </td>
   
   <td class="ee-details">
  5.213
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0009.jpg">ambush_5_0009</a></td>
   
   <td class="ae">
  0.839
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.929
  </td>
   
   <td class="ae-details">
  0.307
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.903
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.773
  </td>
   
   <td class="ee-details">
  4.681
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0010.jpg">ambush_5_0010</a></td>
   
   <td class="ae">
  0.768
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.888
  </td>
   
   <td class="ae-details">
  0.190
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.551
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.383
  </td>
   
   <td class="ee-details">
  4.359
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.088
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0011.jpg">ambush_5_0011</a></td>
   
   <td class="ae">
  0.735
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.844
  </td>
   
   <td class="ae-details">
  0.227
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.309
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.948
  </td>
   
   <td class="ee-details">
  4.996
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0012.jpg">ambush_5_0012</a></td>
   
   <td class="ae">
  0.731
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.854
  </td>
   
   <td class="ae-details">
  0.279
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.739
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.006
  </td>
   
   <td class="ee-details">
  6.452
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.062
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0013.jpg">ambush_5_0013</a></td>
   
   <td class="ae">
  0.754
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.918
  </td>
   
   <td class="ae-details">
  0.325
  </td>
   
   <td class="ae-details">
  0.090
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.760
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.909
  </td>
   
   <td class="ee-details">
  7.072
  </td>
   
   <td class="ee-details">
  6.492
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.065
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0014.jpg">ambush_5_0014</a></td>
   
   <td class="ae">
  0.718
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.796
  </td>
   
   <td class="ae-details">
  0.629
  </td>
   
   <td class="ae-details">
  0.365
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  8.989
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.198
  </td>
   
   <td class="ee-details">
  12.026
  </td>
   
   <td class="ee-details">
  43.181
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.063
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0015.jpg">ambush_5_0015</a></td>
   
   <td class="ae">
  0.627
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.743
  </td>
   
   <td class="ae-details">
  0.433
  </td>
   
   <td class="ae-details">
  0.326
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  7.138
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.912
  </td>
   
   <td class="ee-details">
  8.933
  </td>
   
   <td class="ee-details">
  35.052
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0016.jpg">ambush_5_0016</a></td>
   
   <td class="ae">
  0.625
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.772
  </td>
   
   <td class="ae-details">
  0.256
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.928
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.204
  </td>
   
   <td class="ee-details">
  5.750
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.062
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0017.jpg">ambush_5_0017</a></td>
   
   <td class="ae">
  0.453
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.550
  </td>
   
   <td class="ae-details">
  0.193
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.115
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.735
  </td>
   
   <td class="ee-details">
  5.132
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0018.jpg">ambush_5_0018</a></td>
   
   <td class="ae">
  0.385
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.459
  </td>
   
   <td class="ae-details">
  0.196
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.946
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.745
  </td>
   
   <td class="ee-details">
  5.453
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0019.jpg">ambush_5_0019</a></td>
   
   <td class="ae">
  0.372
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.436
  </td>
   
   <td class="ae-details">
  0.215
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.747
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.256
  </td>
   
   <td class="ee-details">
  5.949
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0020.jpg">ambush_5_0020</a></td>
   
   <td class="ae">
  0.330
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.367
  </td>
   
   <td class="ae-details">
  0.241
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.419
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.292
  </td>
   
   <td class="ee-details">
  7.067
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0021.jpg">ambush_5_0021</a></td>
   
   <td class="ae">
  0.322
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.401
  </td>
   
   <td class="ae-details">
  0.157
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.974
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.928
  </td>
   
   <td class="ee-details">
  6.165
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0022.jpg">ambush_5_0022</a></td>
   
   <td class="ae">
  0.423
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.500
  </td>
   
   <td class="ae-details">
  0.299
  </td>
   
   <td class="ae-details">
  0.521
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  6.151
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.482
  </td>
   
   <td class="ee-details">
  8.905
  </td>
   
   <td class="ee-details">
  39.294
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0023.jpg">ambush_5_0023</a></td>
   
   <td class="ae">
  0.449
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.427
  </td>
   
   <td class="ae-details">
  0.256
  </td>
   
   <td class="ae-details">
  0.799
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  10.487
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.105
  </td>
   
   <td class="ee-details">
  10.930
  </td>
   
   <td class="ee-details">
  35.817
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0024.jpg">ambush_5_0024</a></td>
   
   <td class="ae">
  0.435
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.509
  </td>
   
   <td class="ae-details">
  0.324
  </td>
   
   <td class="ae-details">
  1.651
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.817
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.418
  </td>
   
   <td class="ee-details">
  10.313
  </td>
   
   <td class="ee-details">
  44.896
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0025.jpg">ambush_5_0025</a></td>
   
   <td class="ae">
  0.394
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.332
  </td>
   
   <td class="ae-details">
  0.550
  </td>
   
   <td class="ae-details">
  0.601
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.549
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.132
  </td>
   
   <td class="ee-details">
  10.625
  </td>
   
   <td class="ee-details">
  34.808
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0026.jpg">ambush_5_0026</a></td>
   
   <td class="ae">
  0.319
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.304
  </td>
   
   <td class="ae-details">
  0.259
  </td>
   
   <td class="ae-details">
  1.144
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.820
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.744
  </td>
   
   <td class="ee-details">
  6.668
  </td>
   
   <td class="ee-details">
  41.068
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0027.jpg">ambush_5_0027</a></td>
   
   <td class="ae">
  0.340
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.392
  </td>
   
   <td class="ae-details">
  0.284
  </td>
   
   <td class="ae-details">
  0.660
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.322
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.708
  </td>
   
   <td class="ee-details">
  8.083
  </td>
   
   <td class="ee-details">
  39.725
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0028.jpg">ambush_5_0028</a></td>
   
   <td class="ae">
  0.402
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.380
  </td>
   
   <td class="ae-details">
  0.371
  </td>
   
   <td class="ae-details">
  0.508
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  9.960
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.198
  </td>
   
   <td class="ee-details">
  10.606
  </td>
   
   <td class="ee-details">
  26.490
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0029.jpg">ambush_5_0029</a></td>
   
   <td class="ae">
  0.380
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.318
  </td>
   
   <td class="ae-details">
  0.560
  </td>
   
   <td class="ae-details">
  0.413
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  13.637
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.086
  </td>
   
   <td class="ee-details">
  14.302
  </td>
   
   <td class="ee-details">
  30.853
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0030.jpg">ambush_5_0030</a></td>
   
   <td class="ae">
  0.284
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.300
  </td>
   
   <td class="ae-details">
  0.224
  </td>
   
   <td class="ae-details">
  0.295
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  13.963
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.825
  </td>
   
   <td class="ee-details">
  6.881
  </td>
   
   <td class="ee-details">
  39.653
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0031.jpg">ambush_5_0031</a></td>
   
   <td class="ae">
  0.374
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.382
  </td>
   
   <td class="ae-details">
  0.207
  </td>
   
   <td class="ae-details">
  0.599
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  20.595
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.663
  </td>
   
   <td class="ee-details">
  7.230
  </td>
   
   <td class="ee-details">
  86.731
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0032.jpg">ambush_5_0032</a></td>
   
   <td class="ae">
  0.590
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.658
  </td>
   
   <td class="ae-details">
  0.392
  </td>
   
   <td class="ae-details">
  0.574
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  21.196
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.756
  </td>
   
   <td class="ee-details">
  13.689
  </td>
   
   <td class="ee-details">
  59.553
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0033.jpg">ambush_5_0033</a></td>
   
   <td class="ae">
  0.598
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.637
  </td>
   
   <td class="ae-details">
  0.334
  </td>
   
   <td class="ae-details">
  0.658
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  18.435
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.818
  </td>
   
   <td class="ee-details">
  15.109
  </td>
   
   <td class="ee-details">
  52.676
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.067
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0034.jpg">ambush_5_0034</a></td>
   
   <td class="ae">
  0.724
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.334
  </td>
   
   <td class="ae-details">
  0.701
  </td>
   
   <td class="ae-details">
  0.856
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  22.255
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.226
  </td>
   
   <td class="ee-details">
  10.111
  </td>
   
   <td class="ee-details">
  63.794
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0035.jpg">ambush_5_0035</a></td>
   
   <td class="ae">
  0.648
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.457
  </td>
   
   <td class="ae-details">
  0.565
  </td>
   
   <td class="ae-details">
  1.124
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  25.393
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.043
  </td>
   
   <td class="ee-details">
  10.461
  </td>
   
   <td class="ee-details">
  107.793
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0036.jpg">ambush_5_0036</a></td>
   
   <td class="ae">
  0.559
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.441
  </td>
   
   <td class="ae-details">
  0.919
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  28.410
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  12.879
  </td>
   
   <td class="ee-details">
  75.708
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0037.jpg">ambush_5_0037</a></td>
   
   <td class="ae">
  0.457
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.292
  </td>
   
   <td class="ae-details">
  0.706
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  29.465
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  9.835
  </td>
   
   <td class="ee-details">
  59.276
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0038.jpg">ambush_5_0038</a></td>
   
   <td class="ae">
  0.587
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.479
  </td>
   
   <td class="ae-details">
  0.714
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  36.878
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  11.809
  </td>
   
   <td class="ee-details">
  66.594
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0039.jpg">ambush_5_0039</a></td>
   
   <td class="ae">
  0.937
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.636
  </td>
   
   <td class="ae-details">
  1.229
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  42.942
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  10.893
  </td>
   
   <td class="ee-details">
  74.030
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0040.jpg">ambush_5_0040</a></td>
   
   <td class="ae">
  1.119
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.603
  </td>
   
   <td class="ae-details">
  0.740
  </td>
   
   <td class="ae-details">
  1.588
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  39.736
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  7.663
  </td>
   
   <td class="ee-details">
  10.261
  </td>
   
   <td class="ee-details">
  69.516
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0041.jpg">ambush_5_0041</a></td>
   
   <td class="ae">
  1.010
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.638
  </td>
   
   <td class="ae-details">
  0.977
  </td>
   
   <td class="ae-details">
  1.538
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  28.776
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  7.293
  </td>
   
   <td class="ee-details">
  26.803
  </td>
   
   <td class="ee-details">
  59.182
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0042.jpg">ambush_5_0042</a></td>
   
   <td class="ae">
  0.791
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.772
  </td>
   
   <td class="ae-details">
  0.371
  </td>
   
   <td class="ae-details">
  0.991
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  20.043
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  7.342
  </td>
   
   <td class="ee-details">
  12.466
  </td>
   
   <td class="ee-details">
  49.861
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0043.jpg">ambush_5_0043</a></td>
   
   <td class="ae">
  0.692
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.438
  </td>
   
   <td class="ae-details">
  0.425
  </td>
   
   <td class="ae-details">
  1.365
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  25.147
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  12.917
  </td>
   
   <td class="ee-details">
  9.383
  </td>
   
   <td class="ee-details">
  66.305
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0044.jpg">ambush_5_0044</a></td>
   
   <td class="ae">
  0.334
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.297
  </td>
   
   <td class="ae-details">
  0.405
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  26.544
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  11.497
  </td>
   
   <td class="ee-details">
  55.994
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.064
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0045.jpg">ambush_5_0045</a></td>
   
   <td class="ae">
  0.297
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.222
  </td>
   
   <td class="ae-details">
  0.414
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  31.234
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  7.180
  </td>
   
   <td class="ee-details">
  68.335
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0046.jpg">ambush_5_0046</a></td>
   
   <td class="ae">
  0.773
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.732
  </td>
   
   <td class="ae-details">
  1.666
  </td>
   
   <td class="ae-details">
  0.832
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  41.036
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  6.147
  </td>
   
   <td class="ee-details">
  54.379
  </td>
   
   <td class="ee-details">
  102.205
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0047.jpg">ambush_5_0047</a></td>
   
   <td class="ae">
  1.005
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  1.253
  </td>
   
   <td class="ae-details">
  0.589
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  69.185
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  27.144
  </td>
   
   <td class="ee-details">
  139.545
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0048.jpg">ambush_5_0048</a></td>
   
   <td class="ae">
  1.253
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.595
  </td>
   
   <td class="ae-details">
  0.588
  </td>
   
   <td class="ae-details">
  1.436
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  68.511
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  9.289
  </td>
   
   <td class="ee-details">
  12.874
  </td>
   
   <td class="ee-details">
  85.353
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_5_0049.jpg">ambush_5_0049</a></td>
   
   <td class="ae">
  1.387
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  2.141
  </td>
   
   <td class="ae-details">
  1.109
  </td>
   
   <td class="ae-details">
  1.394
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  62.863
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  19.412
  </td>
   
   <td class="ee-details">
  27.492
  </td>
   
   <td class="ee-details">
  63.806
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_6_0001.jpg">ambush_6_0001</a></td>
   
   <td class="ae">
  0.667
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.851
  </td>
   
   <td class="ae-details">
  0.514
  </td>
   
   <td class="ae-details">
  1.145
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  21.006
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  10.054
  </td>
   
   <td class="ee-details">
  14.373
  </td>
   
   <td class="ee-details">
  42.095
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_6_0002.jpg">ambush_6_0002</a></td>
   
   <td class="ae">
  0.838
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.730
  </td>
   
   <td class="ae-details">
  0.506
  </td>
   
   <td class="ae-details">
  1.672
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  27.006
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  9.389
  </td>
   
   <td class="ee-details">
  14.570
  </td>
   
   <td class="ee-details">
  58.649
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_6_0003.jpg">ambush_6_0003</a></td>
   
   <td class="ae">
  0.741
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.497
  </td>
   
   <td class="ae-details">
  0.463
  </td>
   
   <td class="ae-details">
  1.472
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  27.443
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  10.460
  </td>
   
   <td class="ee-details">
  14.737
  </td>
   
   <td class="ee-details">
  60.859
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_6_0004.jpg">ambush_6_0004</a></td>
   
   <td class="ae">
  0.620
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.468
  </td>
   
   <td class="ae-details">
  0.484
  </td>
   
   <td class="ae-details">
  1.259
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  21.617
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  14.888
  </td>
   
   <td class="ee-details">
  16.995
  </td>
   
   <td class="ee-details">
  44.036
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.083
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_6_0005.jpg">ambush_6_0005</a></td>
   
   <td class="ae">
  0.581
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.428
  </td>
   
   <td class="ae-details">
  0.515
  </td>
   
   <td class="ae-details">
  1.043
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  19.946
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.109
  </td>
   
   <td class="ee-details">
  16.759
  </td>
   
   <td class="ee-details">
  42.809
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_6_0006.jpg">ambush_6_0006</a></td>
   
   <td class="ae">
  0.800
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.894
  </td>
   
   <td class="ae-details">
  0.811
  </td>
   
   <td class="ae-details">
  0.436
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  14.130
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  9.966
  </td>
   
   <td class="ee-details">
  13.484
  </td>
   
   <td class="ee-details">
  32.447
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_6_0007.jpg">ambush_6_0007</a></td>
   
   <td class="ae">
  0.631
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.755
  </td>
   
   <td class="ae-details">
  0.522
  </td>
   
   <td class="ae-details">
  0.725
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  13.424
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  13.529
  </td>
   
   <td class="ee-details">
  11.120
  </td>
   
   <td class="ee-details">
  35.923
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_6_0008.jpg">ambush_6_0008</a></td>
   
   <td class="ae">
  0.419
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.598
  </td>
   
   <td class="ae-details">
  0.327
  </td>
   
   <td class="ae-details">
  0.304
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  11.357
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  10.875
  </td>
   
   <td class="ee-details">
  7.103
  </td>
   
   <td class="ee-details">
  25.635
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.119
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_6_0009.jpg">ambush_6_0009</a></td>
   
   <td class="ae">
  0.276
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.537
  </td>
   
   <td class="ae-details">
  0.218
  </td>
   
   <td class="ae-details">
  0.371
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  12.274
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  9.777
  </td>
   
   <td class="ee-details">
  5.890
  </td>
   
   <td class="ee-details">
  33.859
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_6_0010.jpg">ambush_6_0010</a></td>
   
   <td class="ae">
  0.386
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.621
  </td>
   
   <td class="ae-details">
  0.340
  </td>
   
   <td class="ae-details">
  0.480
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  19.216
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  9.924
  </td>
   
   <td class="ee-details">
  10.710
  </td>
   
   <td class="ee-details">
  39.401
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_6_0011.jpg">ambush_6_0011</a></td>
   
   <td class="ae">
  0.793
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.598
  </td>
   
   <td class="ae-details">
  0.501
  </td>
   
   <td class="ae-details">
  1.208
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  31.379
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  16.368
  </td>
   
   <td class="ee-details">
  18.625
  </td>
   
   <td class="ee-details">
  49.827
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_6_0012.jpg">ambush_6_0012</a></td>
   
   <td class="ae">
  0.695
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.223
  </td>
   
   <td class="ae-details">
  0.590
  </td>
   
   <td class="ae-details">
  0.729
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  28.700
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  12.195
  </td>
   
   <td class="ee-details">
  19.792
  </td>
   
   <td class="ee-details">
  36.502
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_6_0013.jpg">ambush_6_0013</a></td>
   
   <td class="ae">
  0.482
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.566
  </td>
   
   <td class="ae-details">
  0.360
  </td>
   
   <td class="ae-details">
  0.668
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  23.129
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  12.196
  </td>
   
   <td class="ee-details">
  14.016
  </td>
   
   <td class="ee-details">
  37.026
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_6_0014.jpg">ambush_6_0014</a></td>
   
   <td class="ae">
  0.906
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.601
  </td>
   
   <td class="ae-details">
  1.068
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  47.793
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  22.619
  </td>
   
   <td class="ee-details">
  61.155
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_6_0015.jpg">ambush_6_0015</a></td>
   
   <td class="ae">
  0.762
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.710
  </td>
   
   <td class="ae-details">
  0.784
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  76.707
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  25.723
  </td>
   
   <td class="ee-details">
  99.184
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_6_0016.jpg">ambush_6_0016</a></td>
   
   <td class="ae">
  0.755
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.594
  </td>
   
   <td class="ae-details">
  1.006
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  43.773
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  15.666
  </td>
   
   <td class="ee-details">
  87.767
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_6_0017.jpg">ambush_6_0017</a></td>
   
   <td class="ae">
  0.652
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.491
  </td>
   
   <td class="ae-details">
  0.249
  </td>
   
   <td class="ae-details">
  1.770
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  32.296
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  9.712
  </td>
   
   <td class="ee-details">
  8.810
  </td>
   
   <td class="ee-details">
  98.168
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_6_0018.jpg">ambush_6_0018</a></td>
   
   <td class="ae">
  0.603
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.890
  </td>
   
   <td class="ae-details">
  0.173
  </td>
   
   <td class="ae-details">
  0.805
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  33.106
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  20.341
  </td>
   
   <td class="ee-details">
  11.957
  </td>
   
   <td class="ee-details">
  43.048
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_6_0019.jpg">ambush_6_0019</a></td>
   
   <td class="ae">
  0.326
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.715
  </td>
   
   <td class="ae-details">
  0.546
  </td>
   
   <td class="ae-details">
  0.287
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  21.510
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  5.996
  </td>
   
   <td class="ee-details">
  15.104
  </td>
   
   <td class="ee-details">
  22.677
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.061
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0001.jpg">ambush_7_0001</a></td>
   
   <td class="ae">
  0.431
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.431
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.505
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.505
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0002.jpg">ambush_7_0002</a></td>
   
   <td class="ae">
  0.435
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.435
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.508
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.508
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0003.jpg">ambush_7_0003</a></td>
   
   <td class="ae">
  0.441
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.441
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.533
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.533
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0004.jpg">ambush_7_0004</a></td>
   
   <td class="ae">
  0.449
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.449
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.598
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.598
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0005.jpg">ambush_7_0005</a></td>
   
   <td class="ae">
  0.459
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.458
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.492
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.042
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.686
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  47.563
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0006.jpg">ambush_7_0006</a></td>
   
   <td class="ae">
  0.459
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.444
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  1.161
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.104
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.662
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  69.264
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0007.jpg">ambush_7_0007</a></td>
   
   <td class="ae">
  0.471
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.468
  </td>
   
   <td class="ae-details">
  0.635
  </td>
   
   <td class="ae-details">
  0.562
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.515
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.826
  </td>
   
   <td class="ee-details">
  23.356
  </td>
   
   <td class="ee-details">
  46.671
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.065
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0008.jpg">ambush_7_0008</a></td>
   
   <td class="ae">
  0.474
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.486
  </td>
   
   <td class="ae-details">
  0.744
  </td>
   
   <td class="ae-details">
  0.272
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.329
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.802
  </td>
   
   <td class="ee-details">
  26.015
  </td>
   
   <td class="ee-details">
  28.893
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0009.jpg">ambush_7_0009</a></td>
   
   <td class="ae">
  0.487
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.481
  </td>
   
   <td class="ae-details">
  1.712
  </td>
   
   <td class="ae-details">
  0.439
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.518
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.739
  </td>
   
   <td class="ee-details">
  37.231
  </td>
   
   <td class="ee-details">
  24.810
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0010.jpg">ambush_7_0010</a></td>
   
   <td class="ae">
  0.492
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.505
  </td>
   
   <td class="ae-details">
  0.694
  </td>
   
   <td class="ae-details">
  0.317
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.537
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.319
  </td>
   
   <td class="ee-details">
  27.700
  </td>
   
   <td class="ee-details">
  26.885
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0011.jpg">ambush_7_0011</a></td>
   
   <td class="ae">
  0.510
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.513
  </td>
   
   <td class="ae-details">
  0.476
  </td>
   
   <td class="ae-details">
  0.486
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.728
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.600
  </td>
   
   <td class="ee-details">
  22.199
  </td>
   
   <td class="ee-details">
  30.748
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0012.jpg">ambush_7_0012</a></td>
   
   <td class="ae">
  0.658
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.550
  </td>
   
   <td class="ae-details">
  0.377
  </td>
   
   <td class="ae-details">
  1.720
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  6.615
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.094
  </td>
   
   <td class="ee-details">
  16.651
  </td>
   
   <td class="ee-details">
  53.547
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0013.jpg">ambush_7_0013</a></td>
   
   <td class="ae">
  0.696
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.603
  </td>
   
   <td class="ae-details">
  0.735
  </td>
   
   <td class="ae-details">
  2.207
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  6.495
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.288
  </td>
   
   <td class="ee-details">
  18.409
  </td>
   
   <td class="ee-details">
  51.636
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0014.jpg">ambush_7_0014</a></td>
   
   <td class="ae">
  0.598
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.675
  </td>
   
   <td class="ae-details">
  0.233
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.613
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.825
  </td>
   
   <td class="ee-details">
  7.368
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0015.jpg">ambush_7_0015</a></td>
   
   <td class="ae">
  0.448
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.446
  </td>
   
   <td class="ae-details">
  1.050
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.047
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.023
  </td>
   
   <td class="ee-details">
  10.834
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0016.jpg">ambush_7_0016</a></td>
   
   <td class="ae">
  0.412
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.412
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.756
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.756
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0017.jpg">ambush_7_0017</a></td>
   
   <td class="ae">
  0.422
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.422
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.765
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.765
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0018.jpg">ambush_7_0018</a></td>
   
   <td class="ae">
  0.406
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.406
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.741
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.741
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0019.jpg">ambush_7_0019</a></td>
   
   <td class="ae">
  0.412
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.412
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.725
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.725
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0020.jpg">ambush_7_0020</a></td>
   
   <td class="ae">
  0.439
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.439
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.734
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.734
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0021.jpg">ambush_7_0021</a></td>
   
   <td class="ae">
  0.444
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.444
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.728
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.728
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0022.jpg">ambush_7_0022</a></td>
   
   <td class="ae">
  0.450
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.450
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.739
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.739
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0023.jpg">ambush_7_0023</a></td>
   
   <td class="ae">
  0.445
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.445
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.721
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.721
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.067
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0024.jpg">ambush_7_0024</a></td>
   
   <td class="ae">
  0.481
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.479
  </td>
   
   <td class="ae-details">
  0.653
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.889
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.844
  </td>
   
   <td class="ee-details">
  6.648
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0025.jpg">ambush_7_0025</a></td>
   
   <td class="ae">
  0.496
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.497
  </td>
   
   <td class="ae-details">
  0.469
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.963
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.900
  </td>
   
   <td class="ee-details">
  5.187
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0026.jpg">ambush_7_0026</a></td>
   
   <td class="ae">
  0.491
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.493
  </td>
   
   <td class="ae-details">
  0.394
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.981
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.923
  </td>
   
   <td class="ee-details">
  4.441
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0027.jpg">ambush_7_0027</a></td>
   
   <td class="ae">
  0.492
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.492
  </td>
   
   <td class="ae-details">
  0.492
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.014
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.964
  </td>
   
   <td class="ee-details">
  5.176
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0028.jpg">ambush_7_0028</a></td>
   
   <td class="ae">
  0.501
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.503
  </td>
   
   <td class="ae-details">
  0.304
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.330
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.300
  </td>
   
   <td class="ee-details">
  3.700
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0029.jpg">ambush_7_0029</a></td>
   
   <td class="ae">
  0.503
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.509
  </td>
   
   <td class="ae-details">
  0.173
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.064
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.041
  </td>
   
   <td class="ee-details">
  3.474
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0030.jpg">ambush_7_0030</a></td>
   
   <td class="ae">
  0.541
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.633
  </td>
   
   <td class="ae-details">
  0.283
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.926
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.389
  </td>
   
   <td class="ee-details">
  4.438
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0031.jpg">ambush_7_0031</a></td>
   
   <td class="ae">
  0.562
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.734
  </td>
   
   <td class="ae-details">
  0.261
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.588
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.754
  </td>
   
   <td class="ee-details">
  5.052
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0032.jpg">ambush_7_0032</a></td>
   
   <td class="ae">
  0.568
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.768
  </td>
   
   <td class="ae-details">
  0.234
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.899
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.047
  </td>
   
   <td class="ee-details">
  5.316
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0033.jpg">ambush_7_0033</a></td>
   
   <td class="ae">
  0.535
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.740
  </td>
   
   <td class="ae-details">
  0.180
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.606
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.813
  </td>
   
   <td class="ee-details">
  4.976
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0034.jpg">ambush_7_0034</a></td>
   
   <td class="ae">
  0.490
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.661
  </td>
   
   <td class="ae-details">
  0.079
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.004
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.423
  </td>
   
   <td class="ee-details">
  4.404
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0035.jpg">ambush_7_0035</a></td>
   
   <td class="ae">
  0.472
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.506
  </td>
   
   <td class="ae-details">
  0.125
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.451
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.285
  </td>
   
   <td class="ee-details">
  4.141
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0036.jpg">ambush_7_0036</a></td>
   
   <td class="ae">
  0.479
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.585
  </td>
   
   <td class="ae-details">
  0.043
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.751
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.299
  </td>
   
   <td class="ee-details">
  4.616
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0037.jpg">ambush_7_0037</a></td>
   
   <td class="ae">
  0.640
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.889
  </td>
   
   <td class="ae-details">
  0.252
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.470
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.191
  </td>
   
   <td class="ee-details">
  6.463
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0038.jpg">ambush_7_0038</a></td>
   
   <td class="ae">
  0.731
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.025
  </td>
   
   <td class="ae-details">
  0.279
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  6.291
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.877
  </td>
   
   <td class="ee-details">
  8.468
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.082
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0039.jpg">ambush_7_0039</a></td>
   
   <td class="ae">
  0.833
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.134
  </td>
   
   <td class="ae-details">
  0.301
  </td>
   
   <td class="ae-details">
  0.429
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  9.926
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  6.131
  </td>
   
   <td class="ee-details">
  11.606
  </td>
   
   <td class="ee-details">
  23.716
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.081
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0040.jpg">ambush_7_0040</a></td>
   
   <td class="ae">
  0.957
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.069
  </td>
   
   <td class="ae-details">
  0.613
  </td>
   
   <td class="ae-details">
  0.780
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  17.184
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  6.084
  </td>
   
   <td class="ee-details">
  17.622
  </td>
   
   <td class="ee-details">
  39.319
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0041.jpg">ambush_7_0041</a></td>
   
   <td class="ae">
  1.068
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.112
  </td>
   
   <td class="ae-details">
  0.460
  </td>
   
   <td class="ae-details">
  1.005
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  20.464
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  7.495
  </td>
   
   <td class="ee-details">
  19.049
  </td>
   
   <td class="ee-details">
  49.135
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0042.jpg">ambush_7_0042</a></td>
   
   <td class="ae">
  1.078
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.032
  </td>
   
   <td class="ae-details">
  1.063
  </td>
   
   <td class="ae-details">
  1.205
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  20.917
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  6.490
  </td>
   
   <td class="ee-details">
  34.069
  </td>
   
   <td class="ee-details">
  60.469
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0043.jpg">ambush_7_0043</a></td>
   
   <td class="ae">
  0.978
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.940
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  1.135
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  15.996
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.204
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  65.247
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0044.jpg">ambush_7_0044</a></td>
   
   <td class="ae">
  0.932
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.937
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.886
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  10.345
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.956
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  67.052
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.081
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0045.jpg">ambush_7_0045</a></td>
   
   <td class="ae">
  0.817
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.815
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.906
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.893
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.237
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  66.121
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0046.jpg">ambush_7_0046</a></td>
   
   <td class="ae">
  0.687
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.687
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.007
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.007
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0047.jpg">ambush_7_0047</a></td>
   
   <td class="ae">
  0.601
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.601
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.808
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.808
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0048.jpg">ambush_7_0048</a></td>
   
   <td class="ae">
  0.523
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.523
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.656
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.656
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/ambush_7_0049.jpg">ambush_7_0049</a></td>
   
   <td class="ae">
  0.513
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.513
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.623
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.623
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0001.jpg">bamboo_1_0001</a></td>
   
   <td class="ae">
  0.270
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.270
  </td>
   
   <td class="ae-details">
  0.329
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.619
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.606
  </td>
   
   <td class="ee-details">
  5.984
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0002.jpg">bamboo_1_0002</a></td>
   
   <td class="ae">
  0.271
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.271
  </td>
   
   <td class="ae-details">
  0.222
  </td>
   
   <td class="ae-details">
  0.101
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.662
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.634
  </td>
   
   <td class="ee-details">
  7.525
  </td>
   
   <td class="ee-details">
  20.421
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0003.jpg">bamboo_1_0003</a></td>
   
   <td class="ae">
  0.262
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.262
  </td>
   
   <td class="ae-details">
  0.258
  </td>
   
   <td class="ae-details">
  0.094
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.672
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.631
  </td>
   
   <td class="ee-details">
  10.736
  </td>
   
   <td class="ee-details">
  31.272
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0004.jpg">bamboo_1_0004</a></td>
   
   <td class="ae">
  0.256
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.256
  </td>
   
   <td class="ae-details">
  0.306
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.647
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.627
  </td>
   
   <td class="ee-details">
  9.961
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0005.jpg">bamboo_1_0005</a></td>
   
   <td class="ae">
  0.241
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.241
  </td>
   
   <td class="ae-details">
  0.420
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.625
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.614
  </td>
   
   <td class="ee-details">
  7.205
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0006.jpg">bamboo_1_0006</a></td>
   
   <td class="ae">
  0.244
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.244
  </td>
   
   <td class="ae-details">
  0.893
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.644
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.642
  </td>
   
   <td class="ee-details">
  10.482
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0007.jpg">bamboo_1_0007</a></td>
   
   <td class="ae">
  0.234
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.234
  </td>
   
   <td class="ae-details">
  0.742
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.664
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.659
  </td>
   
   <td class="ee-details">
  15.921
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0008.jpg">bamboo_1_0008</a></td>
   
   <td class="ae">
  0.228
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.228
  </td>
   
   <td class="ae-details">
  0.366
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.672
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.656
  </td>
   
   <td class="ee-details">
  8.867
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0009.jpg">bamboo_1_0009</a></td>
   
   <td class="ae">
  0.231
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.230
  </td>
   
   <td class="ae-details">
  0.727
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.688
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.675
  </td>
   
   <td class="ee-details">
  10.431
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0010.jpg">bamboo_1_0010</a></td>
   
   <td class="ae">
  0.231
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.230
  </td>
   
   <td class="ae-details">
  0.803
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.714
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.703
  </td>
   
   <td class="ee-details">
  8.488
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.065
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0011.jpg">bamboo_1_0011</a></td>
   
   <td class="ae">
  0.222
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.222
  </td>
   
   <td class="ae-details">
  0.138
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.704
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.702
  </td>
   
   <td class="ee-details">
  6.030
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.063
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0012.jpg">bamboo_1_0012</a></td>
   
   <td class="ae">
  0.217
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.217
  </td>
   
   <td class="ae-details">
  0.195
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.701
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.697
  </td>
   
   <td class="ee-details">
  6.544
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0013.jpg">bamboo_1_0013</a></td>
   
   <td class="ae">
  0.209
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.208
  </td>
   
   <td class="ae-details">
  0.351
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.703
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.682
  </td>
   
   <td class="ee-details">
  5.420
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.067
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0014.jpg">bamboo_1_0014</a></td>
   
   <td class="ae">
  0.203
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.202
  </td>
   
   <td class="ae-details">
  0.305
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.711
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.668
  </td>
   
   <td class="ee-details">
  5.022
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.062
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0015.jpg">bamboo_1_0015</a></td>
   
   <td class="ae">
  0.206
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.206
  </td>
   
   <td class="ae-details">
  0.211
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.746
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.704
  </td>
   
   <td class="ee-details">
  4.275
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.081
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0016.jpg">bamboo_1_0016</a></td>
   
   <td class="ae">
  0.204
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.200
  </td>
   
   <td class="ae-details">
  0.451
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.788
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.693
  </td>
   
   <td class="ee-details">
  7.342
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0017.jpg">bamboo_1_0017</a></td>
   
   <td class="ae">
  0.207
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.207
  </td>
   
   <td class="ae-details">
  0.233
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.794
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.736
  </td>
   
   <td class="ee-details">
  5.562
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0018.jpg">bamboo_1_0018</a></td>
   
   <td class="ae">
  0.192
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.191
  </td>
   
   <td class="ae-details">
  0.224
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.762
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.698
  </td>
   
   <td class="ee-details">
  6.825
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0019.jpg">bamboo_1_0019</a></td>
   
   <td class="ae">
  0.190
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.189
  </td>
   
   <td class="ae-details">
  0.209
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.795
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.733
  </td>
   
   <td class="ee-details">
  7.745
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0020.jpg">bamboo_1_0020</a></td>
   
   <td class="ae">
  0.181
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.176
  </td>
   
   <td class="ae-details">
  0.916
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.771
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.691
  </td>
   
   <td class="ee-details">
  11.453
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0021.jpg">bamboo_1_0021</a></td>
   
   <td class="ae">
  0.176
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.175
  </td>
   
   <td class="ae-details">
  0.251
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.774
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.694
  </td>
   
   <td class="ee-details">
  9.450
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0022.jpg">bamboo_1_0022</a></td>
   
   <td class="ae">
  0.173
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.166
  </td>
   
   <td class="ae-details">
  0.744
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.760
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.672
  </td>
   
   <td class="ee-details">
  7.932
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.083
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0023.jpg">bamboo_1_0023</a></td>
   
   <td class="ae">
  0.172
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.171
  </td>
   
   <td class="ae-details">
  0.263
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.756
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.685
  </td>
   
   <td class="ee-details">
  6.273
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0024.jpg">bamboo_1_0024</a></td>
   
   <td class="ae">
  0.176
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.176
  </td>
   
   <td class="ae-details">
  0.168
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.794
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.741
  </td>
   
   <td class="ee-details">
  5.607
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0025.jpg">bamboo_1_0025</a></td>
   
   <td class="ae">
  0.176
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.176
  </td>
   
   <td class="ae-details">
  0.168
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.760
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.701
  </td>
   
   <td class="ee-details">
  5.459
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0026.jpg">bamboo_1_0026</a></td>
   
   <td class="ae">
  0.172
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.170
  </td>
   
   <td class="ae-details">
  0.310
  </td>
   
   <td class="ae-details">
  1.242
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.778
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.699
  </td>
   
   <td class="ee-details">
  6.590
  </td>
   
   <td class="ee-details">
  41.049
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0027.jpg">bamboo_1_0027</a></td>
   
   <td class="ae">
  0.165
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.162
  </td>
   
   <td class="ae-details">
  0.390
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.756
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.665
  </td>
   
   <td class="ee-details">
  8.312
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0028.jpg">bamboo_1_0028</a></td>
   
   <td class="ae">
  0.175
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.173
  </td>
   
   <td class="ae-details">
  0.377
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.794
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.720
  </td>
   
   <td class="ee-details">
  7.693
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0029.jpg">bamboo_1_0029</a></td>
   
   <td class="ae">
  0.187
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.183
  </td>
   
   <td class="ae-details">
  0.532
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.863
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.750
  </td>
   
   <td class="ee-details">
  9.367
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.065
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0030.jpg">bamboo_1_0030</a></td>
   
   <td class="ae">
  0.168
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.167
  </td>
   
   <td class="ae-details">
  0.361
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.766
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.708
  </td>
   
   <td class="ee-details">
  6.880
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0031.jpg">bamboo_1_0031</a></td>
   
   <td class="ae">
  0.158
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.156
  </td>
   
   <td class="ae-details">
  0.404
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.775
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.704
  </td>
   
   <td class="ee-details">
  10.207
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0032.jpg">bamboo_1_0032</a></td>
   
   <td class="ae">
  0.168
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.163
  </td>
   
   <td class="ae-details">
  0.783
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.836
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.734
  </td>
   
   <td class="ee-details">
  11.891
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0033.jpg">bamboo_1_0033</a></td>
   
   <td class="ae">
  0.170
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.168
  </td>
   
   <td class="ae-details">
  0.620
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.808
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.757
  </td>
   
   <td class="ee-details">
  8.989
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0034.jpg">bamboo_1_0034</a></td>
   
   <td class="ae">
  0.172
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.170
  </td>
   
   <td class="ae-details">
  0.701
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.798
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.760
  </td>
   
   <td class="ee-details">
  12.397
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0035.jpg">bamboo_1_0035</a></td>
   
   <td class="ae">
  0.175
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.174
  </td>
   
   <td class="ae-details">
  0.479
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.788
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.758
  </td>
   
   <td class="ee-details">
  9.927
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.065
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0036.jpg">bamboo_1_0036</a></td>
   
   <td class="ae">
  0.175
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.174
  </td>
   
   <td class="ae-details">
  0.391
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.782
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.751
  </td>
   
   <td class="ee-details">
  9.664
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0037.jpg">bamboo_1_0037</a></td>
   
   <td class="ae">
  0.172
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.171
  </td>
   
   <td class="ae-details">
  0.361
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.793
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.752
  </td>
   
   <td class="ee-details">
  8.682
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0038.jpg">bamboo_1_0038</a></td>
   
   <td class="ae">
  0.167
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.165
  </td>
   
   <td class="ae-details">
  0.564
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.804
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.761
  </td>
   
   <td class="ee-details">
  8.087
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0039.jpg">bamboo_1_0039</a></td>
   
   <td class="ae">
  0.169
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.167
  </td>
   
   <td class="ae-details">
  0.421
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.831
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.769
  </td>
   
   <td class="ee-details">
  8.598
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0040.jpg">bamboo_1_0040</a></td>
   
   <td class="ae">
  0.162
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.158
  </td>
   
   <td class="ae-details">
  0.547
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.810
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.736
  </td>
   
   <td class="ee-details">
  8.809
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0041.jpg">bamboo_1_0041</a></td>
   
   <td class="ae">
  0.167
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.164
  </td>
   
   <td class="ae-details">
  0.385
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.841
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.754
  </td>
   
   <td class="ee-details">
  9.484
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0042.jpg">bamboo_1_0042</a></td>
   
   <td class="ae">
  0.164
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.157
  </td>
   
   <td class="ae-details">
  0.955
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.874
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.758
  </td>
   
   <td class="ee-details">
  12.695
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0043.jpg">bamboo_1_0043</a></td>
   
   <td class="ae">
  0.164
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.160
  </td>
   
   <td class="ae-details">
  0.588
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.871
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.779
  </td>
   
   <td class="ee-details">
  9.830
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0044.jpg">bamboo_1_0044</a></td>
   
   <td class="ae">
  0.171
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.164
  </td>
   
   <td class="ae-details">
  0.763
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.898
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.793
  </td>
   
   <td class="ee-details">
  9.780
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0045.jpg">bamboo_1_0045</a></td>
   
   <td class="ae">
  0.195
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.173
  </td>
   
   <td class="ae-details">
  1.155
  </td>
   
   <td class="ae-details">
  1.078
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.330
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.824
  </td>
   
   <td class="ee-details">
  14.880
  </td>
   
   <td class="ee-details">
  50.545
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0046.jpg">bamboo_1_0046</a></td>
   
   <td class="ae">
  0.196
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.180
  </td>
   
   <td class="ae-details">
  0.735
  </td>
   
   <td class="ae-details">
  1.483
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.550
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.857
  </td>
   
   <td class="ee-details">
  15.009
  </td>
   
   <td class="ee-details">
  68.457
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0047.jpg">bamboo_1_0047</a></td>
   
   <td class="ae">
  0.180
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.172
  </td>
   
   <td class="ae-details">
  0.730
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.036
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.832
  </td>
   
   <td class="ee-details">
  15.834
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0048.jpg">bamboo_1_0048</a></td>
   
   <td class="ae">
  0.181
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.177
  </td>
   
   <td class="ae-details">
  0.492
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.010
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.868
  </td>
   
   <td class="ee-details">
  11.848
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_1_0049.jpg">bamboo_1_0049</a></td>
   
   <td class="ae">
  0.168
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.164
  </td>
   
   <td class="ae-details">
  0.524
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.926
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.812
  </td>
   
   <td class="ee-details">
  10.888
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0001.jpg">bamboo_2_0001</a></td>
   
   <td class="ae">
  0.468
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.467
  </td>
   
   <td class="ae-details">
  0.690
  </td>
   
   <td class="ae-details">
  1.127
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.652
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.557
  </td>
   
   <td class="ee-details">
  21.571
  </td>
   
   <td class="ee-details">
  43.998
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0002.jpg">bamboo_2_0002</a></td>
   
   <td class="ae">
  0.480
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.475
  </td>
   
   <td class="ae-details">
  1.153
  </td>
   
   <td class="ae-details">
  0.595
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.740
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.612
  </td>
   
   <td class="ee-details">
  19.147
  </td>
   
   <td class="ee-details">
  36.239
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0003.jpg">bamboo_2_0003</a></td>
   
   <td class="ae">
  0.487
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.488
  </td>
   
   <td class="ae-details">
  0.403
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.758
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.649
  </td>
   
   <td class="ee-details">
  9.426
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0004.jpg">bamboo_2_0004</a></td>
   
   <td class="ae">
  0.471
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.470
  </td>
   
   <td class="ae-details">
  0.559
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.816
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.688
  </td>
   
   <td class="ee-details">
  11.771
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0005.jpg">bamboo_2_0005</a></td>
   
   <td class="ae">
  0.467
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.468
  </td>
   
   <td class="ae-details">
  0.206
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.718
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.666
  </td>
   
   <td class="ee-details">
  11.503
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0006.jpg">bamboo_2_0006</a></td>
   
   <td class="ae">
  0.463
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.463
  </td>
   
   <td class="ae-details">
  0.861
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.631
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.619
  </td>
   
   <td class="ee-details">
  15.004
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0007.jpg">bamboo_2_0007</a></td>
   
   <td class="ae">
  0.478
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.477
  </td>
   
   <td class="ae-details">
  0.389
  </td>
   
   <td class="ae-details">
  1.992
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.711
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.651
  </td>
   
   <td class="ee-details">
  13.607
  </td>
   
   <td class="ee-details">
  50.551
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0008.jpg">bamboo_2_0008</a></td>
   
   <td class="ae">
  0.474
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.474
  </td>
   
   <td class="ae-details">
  0.452
  </td>
   
   <td class="ae-details">
  0.148
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.857
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.686
  </td>
   
   <td class="ee-details">
  17.520
  </td>
   
   <td class="ee-details">
  27.590
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0009.jpg">bamboo_2_0009</a></td>
   
   <td class="ae">
  0.479
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.483
  </td>
   
   <td class="ae-details">
  0.162
  </td>
   
   <td class="ae-details">
  0.408
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.866
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.783
  </td>
   
   <td class="ee-details">
  6.521
  </td>
   
   <td class="ee-details">
  32.691
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0010.jpg">bamboo_2_0010</a></td>
   
   <td class="ae">
  0.482
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.486
  </td>
   
   <td class="ae-details">
  0.144
  </td>
   
   <td class="ae-details">
  0.223
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.948
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.825
  </td>
   
   <td class="ee-details">
  8.611
  </td>
   
   <td class="ee-details">
  13.467
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.061
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0011.jpg">bamboo_2_0011</a></td>
   
   <td class="ae">
  0.465
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.469
  </td>
   
   <td class="ae-details">
  0.208
  </td>
   
   <td class="ae-details">
  0.191
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.973
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.816
  </td>
   
   <td class="ee-details">
  11.913
  </td>
   
   <td class="ee-details">
  38.815
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0012.jpg">bamboo_2_0012</a></td>
   
   <td class="ae">
  0.470
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.473
  </td>
   
   <td class="ae-details">
  0.346
  </td>
   
   <td class="ae-details">
  0.173
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.076
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.898
  </td>
   
   <td class="ee-details">
  16.199
  </td>
   
   <td class="ee-details">
  11.139
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0013.jpg">bamboo_2_0013</a></td>
   
   <td class="ae">
  0.458
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.461
  </td>
   
   <td class="ae-details">
  0.781
  </td>
   
   <td class="ae-details">
  0.115
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.069
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.836
  </td>
   
   <td class="ee-details">
  14.590
  </td>
   
   <td class="ee-details">
  14.631
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0014.jpg">bamboo_2_0014</a></td>
   
   <td class="ae">
  0.466
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.470
  </td>
   
   <td class="ae-details">
  0.571
  </td>
   
   <td class="ae-details">
  0.258
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.425
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.941
  </td>
   
   <td class="ee-details">
  10.418
  </td>
   
   <td class="ee-details">
  27.212
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.067
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0015.jpg">bamboo_2_0015</a></td>
   
   <td class="ae">
  0.460
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.462
  </td>
   
   <td class="ae-details">
  0.389
  </td>
   
   <td class="ae-details">
  0.356
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.298
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.948
  </td>
   
   <td class="ee-details">
  8.557
  </td>
   
   <td class="ee-details">
  21.218
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.062
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0016.jpg">bamboo_2_0016</a></td>
   
   <td class="ae">
  0.451
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.454
  </td>
   
   <td class="ae-details">
  0.447
  </td>
   
   <td class="ae-details">
  0.275
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.441
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.872
  </td>
   
   <td class="ee-details">
  9.849
  </td>
   
   <td class="ee-details">
  29.563
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0017.jpg">bamboo_2_0017</a></td>
   
   <td class="ae">
  0.442
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.438
  </td>
   
   <td class="ae-details">
  0.321
  </td>
   
   <td class="ae-details">
  0.983
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.519
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.795
  </td>
   
   <td class="ee-details">
  8.266
  </td>
   
   <td class="ee-details">
  87.941
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0018.jpg">bamboo_2_0018</a></td>
   
   <td class="ae">
  0.427
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.427
  </td>
   
   <td class="ae-details">
  0.540
  </td>
   
   <td class="ae-details">
  0.678
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.817
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.758
  </td>
   
   <td class="ee-details">
  12.700
  </td>
   
   <td class="ee-details">
  32.216
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0019.jpg">bamboo_2_0019</a></td>
   
   <td class="ae">
  0.424
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.424
  </td>
   
   <td class="ae-details">
  0.382
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.798
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.773
  </td>
   
   <td class="ee-details">
  9.070
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0020.jpg">bamboo_2_0020</a></td>
   
   <td class="ae">
  0.424
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.423
  </td>
   
   <td class="ae-details">
  0.575
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.836
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.781
  </td>
   
   <td class="ee-details">
  11.117
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0021.jpg">bamboo_2_0021</a></td>
   
   <td class="ae">
  0.424
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.422
  </td>
   
   <td class="ae-details">
  0.520
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.929
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.797
  </td>
   
   <td class="ee-details">
  8.360
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0022.jpg">bamboo_2_0022</a></td>
   
   <td class="ae">
  0.440
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.434
  </td>
   
   <td class="ae-details">
  0.713
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.072
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.836
  </td>
   
   <td class="ee-details">
  11.115
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0023.jpg">bamboo_2_0023</a></td>
   
   <td class="ae">
  0.429
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.430
  </td>
   
   <td class="ae-details">
  0.407
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.034
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.843
  </td>
   
   <td class="ee-details">
  9.347
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.065
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0024.jpg">bamboo_2_0024</a></td>
   
   <td class="ae">
  0.428
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.424
  </td>
   
   <td class="ae-details">
  0.581
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.028
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.873
  </td>
   
   <td class="ee-details">
  7.552
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0025.jpg">bamboo_2_0025</a></td>
   
   <td class="ae">
  0.421
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.418
  </td>
   
   <td class="ae-details">
  0.525
  </td>
   
   <td class="ae-details">
  1.202
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.043
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.893
  </td>
   
   <td class="ee-details">
  9.234
  </td>
   
   <td class="ee-details">
  42.525
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0026.jpg">bamboo_2_0026</a></td>
   
   <td class="ae">
  0.423
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.422
  </td>
   
   <td class="ae-details">
  0.494
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.994
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.899
  </td>
   
   <td class="ee-details">
  7.131
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0027.jpg">bamboo_2_0027</a></td>
   
   <td class="ae">
  0.416
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.413
  </td>
   
   <td class="ae-details">
  0.614
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.966
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.868
  </td>
   
   <td class="ee-details">
  7.989
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0028.jpg">bamboo_2_0028</a></td>
   
   <td class="ae">
  0.413
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.409
  </td>
   
   <td class="ae-details">
  0.667
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.005
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.894
  </td>
   
   <td class="ee-details">
  8.603
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0029.jpg">bamboo_2_0029</a></td>
   
   <td class="ae">
  0.411
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.411
  </td>
   
   <td class="ae-details">
  0.428
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.042
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.936
  </td>
   
   <td class="ee-details">
  8.625
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0030.jpg">bamboo_2_0030</a></td>
   
   <td class="ae">
  0.391
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.391
  </td>
   
   <td class="ae-details">
  0.326
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.942
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.879
  </td>
   
   <td class="ee-details">
  7.780
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0031.jpg">bamboo_2_0031</a></td>
   
   <td class="ae">
  0.390
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.389
  </td>
   
   <td class="ae-details">
  0.460
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.945
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.871
  </td>
   
   <td class="ee-details">
  8.080
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0032.jpg">bamboo_2_0032</a></td>
   
   <td class="ae">
  0.392
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.391
  </td>
   
   <td class="ae-details">
  0.481
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.003
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.892
  </td>
   
   <td class="ee-details">
  9.367
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0033.jpg">bamboo_2_0033</a></td>
   
   <td class="ae">
  0.393
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.393
  </td>
   
   <td class="ae-details">
  0.404
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.053
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.909
  </td>
   
   <td class="ee-details">
  7.012
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0034.jpg">bamboo_2_0034</a></td>
   
   <td class="ae">
  0.400
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.396
  </td>
   
   <td class="ae-details">
  0.543
  </td>
   
   <td class="ae-details">
  0.820
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.259
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.937
  </td>
   
   <td class="ee-details">
  10.917
  </td>
   
   <td class="ee-details">
  35.931
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.062
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0035.jpg">bamboo_2_0035</a></td>
   
   <td class="ae">
  0.400
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.401
  </td>
   
   <td class="ae-details">
  0.370
  </td>
   
   <td class="ae-details">
  0.310
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.316
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.016
  </td>
   
   <td class="ee-details">
  8.388
  </td>
   
   <td class="ee-details">
  33.451
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0036.jpg">bamboo_2_0036</a></td>
   
   <td class="ae">
  0.405
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.398
  </td>
   
   <td class="ae-details">
  0.604
  </td>
   
   <td class="ae-details">
  0.141
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.442
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.012
  </td>
   
   <td class="ee-details">
  10.177
  </td>
   
   <td class="ee-details">
  24.727
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0037.jpg">bamboo_2_0037</a></td>
   
   <td class="ae">
  0.445
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.438
  </td>
   
   <td class="ae-details">
  0.590
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.433
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.074
  </td>
   
   <td class="ee-details">
  8.782
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0038.jpg">bamboo_2_0038</a></td>
   
   <td class="ae">
  0.430
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.432
  </td>
   
   <td class="ae-details">
  0.385
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.371
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.055
  </td>
   
   <td class="ee-details">
  8.109
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0039.jpg">bamboo_2_0039</a></td>
   
   <td class="ae">
  0.411
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.412
  </td>
   
   <td class="ae-details">
  0.378
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.430
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.010
  </td>
   
   <td class="ee-details">
  8.949
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.130
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0040.jpg">bamboo_2_0040</a></td>
   
   <td class="ae">
  0.453
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.453
  </td>
   
   <td class="ae-details">
  0.423
  </td>
   
   <td class="ae-details">
  1.621
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.804
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.168
  </td>
   
   <td class="ee-details">
  9.826
  </td>
   
   <td class="ee-details">
  42.948
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0041.jpg">bamboo_2_0041</a></td>
   
   <td class="ae">
  0.495
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.456
  </td>
   
   <td class="ae-details">
  0.782
  </td>
   
   <td class="ae-details">
  1.395
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.018
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.200
  </td>
   
   <td class="ee-details">
  14.891
  </td>
   
   <td class="ee-details">
  52.300
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0042.jpg">bamboo_2_0042</a></td>
   
   <td class="ae">
  0.479
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.444
  </td>
   
   <td class="ae-details">
  0.523
  </td>
   
   <td class="ae-details">
  1.407
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.988
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.152
  </td>
   
   <td class="ee-details">
  13.204
  </td>
   
   <td class="ee-details">
  69.095
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0043.jpg">bamboo_2_0043</a></td>
   
   <td class="ae">
  0.456
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.467
  </td>
   
   <td class="ae-details">
  0.314
  </td>
   
   <td class="ae-details">
  0.398
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.990
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.371
  </td>
   
   <td class="ee-details">
  12.026
  </td>
   
   <td class="ee-details">
  59.837
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0044.jpg">bamboo_2_0044</a></td>
   
   <td class="ae">
  0.501
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.492
  </td>
   
   <td class="ae-details">
  0.748
  </td>
   
   <td class="ae-details">
  0.462
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.028
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.343
  </td>
   
   <td class="ee-details">
  21.472
  </td>
   
   <td class="ee-details">
  48.755
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.090
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0045.jpg">bamboo_2_0045</a></td>
   
   <td class="ae">
  0.604
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.508
  </td>
   
   <td class="ae-details">
  0.948
  </td>
   
   <td class="ae-details">
  1.961
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.565
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.335
  </td>
   
   <td class="ee-details">
  25.016
  </td>
   
   <td class="ee-details">
  60.889
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0046.jpg">bamboo_2_0046</a></td>
   
   <td class="ae">
  0.627
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.541
  </td>
   
   <td class="ae-details">
  0.558
  </td>
   
   <td class="ae-details">
  1.581
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  6.191
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.470
  </td>
   
   <td class="ee-details">
  17.189
  </td>
   
   <td class="ee-details">
  56.037
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0047.jpg">bamboo_2_0047</a></td>
   
   <td class="ae">
  0.633
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.533
  </td>
   
   <td class="ae-details">
  0.785
  </td>
   
   <td class="ae-details">
  1.680
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  7.258
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.684
  </td>
   
   <td class="ee-details">
  23.077
  </td>
   
   <td class="ee-details">
  64.730
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0048.jpg">bamboo_2_0048</a></td>
   
   <td class="ae">
  0.595
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.549
  </td>
   
   <td class="ae-details">
  0.641
  </td>
   
   <td class="ae-details">
  1.140
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.381
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.752
  </td>
   
   <td class="ee-details">
  23.891
  </td>
   
   <td class="ee-details">
  43.804
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bamboo_2_0049.jpg">bamboo_2_0049</a></td>
   
   <td class="ae">
  0.534
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.501
  </td>
   
   <td class="ae-details">
  0.562
  </td>
   
   <td class="ae-details">
  1.100
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.354
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.972
  </td>
   
   <td class="ee-details">
  21.176
  </td>
   
   <td class="ee-details">
  49.907
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0001.jpg">bandage_1_0001</a></td>
   
   <td class="ae">
  0.531
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.568
  </td>
   
   <td class="ae-details">
  0.274
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.625
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.296
  </td>
   
   <td class="ee-details">
  4.951
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0002.jpg">bandage_1_0002</a></td>
   
   <td class="ae">
  0.539
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.622
  </td>
   
   <td class="ae-details">
  0.282
  </td>
   
   <td class="ae-details">
  1.580
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.429
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.504
  </td>
   
   <td class="ee-details">
  6.214
  </td>
   
   <td class="ee-details">
  41.438
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0003.jpg">bandage_1_0003</a></td>
   
   <td class="ae">
  0.560
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.620
  </td>
   
   <td class="ae-details">
  0.388
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.502
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.665
  </td>
   
   <td class="ee-details">
  9.776
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0004.jpg">bandage_1_0004</a></td>
   
   <td class="ae">
  0.536
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.602
  </td>
   
   <td class="ae-details">
  0.344
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.363
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.487
  </td>
   
   <td class="ee-details">
  5.924
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0005.jpg">bandage_1_0005</a></td>
   
   <td class="ae">
  0.520
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.543
  </td>
   
   <td class="ae-details">
  0.331
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.679
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.402
  </td>
   
   <td class="ee-details">
  4.968
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0006.jpg">bandage_1_0006</a></td>
   
   <td class="ae">
  0.503
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.505
  </td>
   
   <td class="ae-details">
  0.428
  </td>
   
   <td class="ae-details">
  1.537
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.516
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.270
  </td>
   
   <td class="ee-details">
  6.958
  </td>
   
   <td class="ee-details">
  53.156
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0007.jpg">bandage_1_0007</a></td>
   
   <td class="ae">
  0.525
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.506
  </td>
   
   <td class="ae-details">
  0.864
  </td>
   
   <td class="ae-details">
  2.799
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.689
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.242
  </td>
   
   <td class="ee-details">
  10.622
  </td>
   
   <td class="ee-details">
  51.313
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0008.jpg">bandage_1_0008</a></td>
   
   <td class="ae">
  0.540
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.554
  </td>
   
   <td class="ae-details">
  0.336
  </td>
   
   <td class="ae-details">
  2.897
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.768
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.247
  </td>
   
   <td class="ee-details">
  6.631
  </td>
   
   <td class="ee-details">
  58.016
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0009.jpg">bandage_1_0009</a></td>
   
   <td class="ae">
  0.523
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.540
  </td>
   
   <td class="ae-details">
  0.297
  </td>
   
   <td class="ae-details">
  2.486
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.035
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.373
  </td>
   
   <td class="ee-details">
  6.381
  </td>
   
   <td class="ee-details">
  92.741
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0010.jpg">bandage_1_0010</a></td>
   
   <td class="ae">
  0.500
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.529
  </td>
   
   <td class="ae-details">
  0.310
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.182
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.695
  </td>
   
   <td class="ee-details">
  6.467
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0011.jpg">bandage_1_0011</a></td>
   
   <td class="ae">
  0.523
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.601
  </td>
   
   <td class="ae-details">
  0.279
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.585
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.963
  </td>
   
   <td class="ee-details">
  5.539
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0012.jpg">bandage_1_0012</a></td>
   
   <td class="ae">
  0.518
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.668
  </td>
   
   <td class="ae-details">
  0.267
  </td>
   
   <td class="ae-details">
  1.962
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.874
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.977
  </td>
   
   <td class="ee-details">
  5.363
  </td>
   
   <td class="ee-details">
  71.923
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0013.jpg">bandage_1_0013</a></td>
   
   <td class="ae">
  0.510
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.677
  </td>
   
   <td class="ae-details">
  0.234
  </td>
   
   <td class="ae-details">
  1.707
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.927
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.950
  </td>
   
   <td class="ee-details">
  5.510
  </td>
   
   <td class="ee-details">
  53.528
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0014.jpg">bandage_1_0014</a></td>
   
   <td class="ae">
  0.514
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.662
  </td>
   
   <td class="ae-details">
  0.233
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.762
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.570
  </td>
   
   <td class="ee-details">
  6.004
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0015.jpg">bandage_1_0015</a></td>
   
   <td class="ae">
  0.524
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.651
  </td>
   
   <td class="ae-details">
  0.216
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.584
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.494
  </td>
   
   <td class="ee-details">
  6.235
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.067
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0016.jpg">bandage_1_0016</a></td>
   
   <td class="ae">
  0.527
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.644
  </td>
   
   <td class="ae-details">
  0.223
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.717
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.447
  </td>
   
   <td class="ee-details">
  7.019
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0017.jpg">bandage_1_0017</a></td>
   
   <td class="ae">
  0.520
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.616
  </td>
   
   <td class="ae-details">
  0.248
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.607
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.150
  </td>
   
   <td class="ee-details">
  7.753
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0018.jpg">bandage_1_0018</a></td>
   
   <td class="ae">
  0.511
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.593
  </td>
   
   <td class="ae-details">
  0.254
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.905
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.795
  </td>
   
   <td class="ee-details">
  6.346
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0019.jpg">bandage_1_0019</a></td>
   
   <td class="ae">
  0.505
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.579
  </td>
   
   <td class="ae-details">
  0.227
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.391
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.778
  </td>
   
   <td class="ee-details">
  4.708
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0020.jpg">bandage_1_0020</a></td>
   
   <td class="ae">
  0.504
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.556
  </td>
   
   <td class="ae-details">
  0.257
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.608
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.751
  </td>
   
   <td class="ee-details">
  6.627
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0021.jpg">bandage_1_0021</a></td>
   
   <td class="ae">
  0.523
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.559
  </td>
   
   <td class="ae-details">
  0.235
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.301
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.960
  </td>
   
   <td class="ee-details">
  5.029
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.081
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0022.jpg">bandage_1_0022</a></td>
   
   <td class="ae">
  0.526
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.543
  </td>
   
   <td class="ae-details">
  0.215
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.053
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.919
  </td>
   
   <td class="ee-details">
  4.556
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0023.jpg">bandage_1_0023</a></td>
   
   <td class="ae">
  0.523
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.536
  </td>
   
   <td class="ae-details">
  0.208
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.982
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.872
  </td>
   
   <td class="ee-details">
  4.607
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0024.jpg">bandage_1_0024</a></td>
   
   <td class="ae">
  0.489
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.498
  </td>
   
   <td class="ae-details">
  0.270
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.971
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.846
  </td>
   
   <td class="ee-details">
  5.067
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0025.jpg">bandage_1_0025</a></td>
   
   <td class="ae">
  0.503
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.510
  </td>
   
   <td class="ae-details">
  0.297
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.010
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.899
  </td>
   
   <td class="ee-details">
  5.577
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0026.jpg">bandage_1_0026</a></td>
   
   <td class="ae">
  0.520
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.525
  </td>
   
   <td class="ae-details">
  0.251
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.891
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.824
  </td>
   
   <td class="ee-details">
  5.669
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0027.jpg">bandage_1_0027</a></td>
   
   <td class="ae">
  0.542
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.546
  </td>
   
   <td class="ae-details">
  0.289
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.770
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.705
  </td>
   
   <td class="ee-details">
  5.494
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0028.jpg">bandage_1_0028</a></td>
   
   <td class="ae">
  0.560
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.564
  </td>
   
   <td class="ae-details">
  0.309
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.644
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.599
  </td>
   
   <td class="ee-details">
  4.604
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0029.jpg">bandage_1_0029</a></td>
   
   <td class="ae">
  0.575
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.577
  </td>
   
   <td class="ae-details">
  0.343
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.588
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.558
  </td>
   
   <td class="ee-details">
  4.225
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0030.jpg">bandage_1_0030</a></td>
   
   <td class="ae">
  0.580
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.582
  </td>
   
   <td class="ae-details">
  0.336
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.530
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.512
  </td>
   
   <td class="ee-details">
  4.024
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0031.jpg">bandage_1_0031</a></td>
   
   <td class="ae">
  0.569
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.570
  </td>
   
   <td class="ae-details">
  0.336
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.458
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.441
  </td>
   
   <td class="ee-details">
  4.110
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0032.jpg">bandage_1_0032</a></td>
   
   <td class="ae">
  0.580
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.581
  </td>
   
   <td class="ae-details">
  0.351
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.478
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.466
  </td>
   
   <td class="ee-details">
  3.985
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0033.jpg">bandage_1_0033</a></td>
   
   <td class="ae">
  0.576
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.577
  </td>
   
   <td class="ae-details">
  0.357
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.482
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.473
  </td>
   
   <td class="ee-details">
  3.911
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0034.jpg">bandage_1_0034</a></td>
   
   <td class="ae">
  0.563
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.564
  </td>
   
   <td class="ae-details">
  0.381
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.486
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.479
  </td>
   
   <td class="ee-details">
  3.993
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0035.jpg">bandage_1_0035</a></td>
   
   <td class="ae">
  0.578
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.579
  </td>
   
   <td class="ae-details">
  0.378
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.532
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.525
  </td>
   
   <td class="ee-details">
  3.881
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0036.jpg">bandage_1_0036</a></td>
   
   <td class="ae">
  0.613
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.614
  </td>
   
   <td class="ae-details">
  0.373
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.615
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.607
  </td>
   
   <td class="ee-details">
  3.833
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0037.jpg">bandage_1_0037</a></td>
   
   <td class="ae">
  0.636
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.636
  </td>
   
   <td class="ae-details">
  0.379
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.771
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.759
  </td>
   
   <td class="ee-details">
  5.433
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.067
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0038.jpg">bandage_1_0038</a></td>
   
   <td class="ae">
  0.631
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.631
  </td>
   
   <td class="ae-details">
  0.358
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.843
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.827
  </td>
   
   <td class="ee-details">
  7.991
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0039.jpg">bandage_1_0039</a></td>
   
   <td class="ae">
  0.618
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.618
  </td>
   
   <td class="ae-details">
  0.465
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.817
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.794
  </td>
   
   <td class="ee-details">
  11.436
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0040.jpg">bandage_1_0040</a></td>
   
   <td class="ae">
  0.604
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.604
  </td>
   
   <td class="ae-details">
  0.409
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.776
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.751
  </td>
   
   <td class="ee-details">
  9.878
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.139
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0041.jpg">bandage_1_0041</a></td>
   
   <td class="ae">
  0.598
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.600
  </td>
   
   <td class="ae-details">
  0.319
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.795
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.779
  </td>
   
   <td class="ee-details">
  5.844
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.099
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0042.jpg">bandage_1_0042</a></td>
   
   <td class="ae">
  0.590
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.592
  </td>
   
   <td class="ae-details">
  0.431
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.836
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.795
  </td>
   
   <td class="ee-details">
  5.873
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0043.jpg">bandage_1_0043</a></td>
   
   <td class="ae">
  0.588
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.593
  </td>
   
   <td class="ae-details">
  0.323
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.865
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.821
  </td>
   
   <td class="ee-details">
  4.290
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0044.jpg">bandage_1_0044</a></td>
   
   <td class="ae">
  0.600
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.609
  </td>
   
   <td class="ae-details">
  0.292
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.927
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.853
  </td>
   
   <td class="ee-details">
  4.398
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0045.jpg">bandage_1_0045</a></td>
   
   <td class="ae">
  0.615
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.630
  </td>
   
   <td class="ae-details">
  0.269
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.102
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.993
  </td>
   
   <td class="ee-details">
  4.619
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.062
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0046.jpg">bandage_1_0046</a></td>
   
   <td class="ae">
  0.623
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.643
  </td>
   
   <td class="ae-details">
  0.279
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.252
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.095
  </td>
   
   <td class="ee-details">
  5.012
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0047.jpg">bandage_1_0047</a></td>
   
   <td class="ae">
  0.622
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.645
  </td>
   
   <td class="ae-details">
  0.295
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.284
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.052
  </td>
   
   <td class="ee-details">
  5.611
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0048.jpg">bandage_1_0048</a></td>
   
   <td class="ae">
  0.620
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.649
  </td>
   
   <td class="ae-details">
  0.223
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.990
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.744
  </td>
   
   <td class="ee-details">
  5.373
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_1_0049.jpg">bandage_1_0049</a></td>
   
   <td class="ae">
  0.604
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.631
  </td>
   
   <td class="ae-details">
  0.219
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.818
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.574
  </td>
   
   <td class="ee-details">
  5.254
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0001.jpg">bandage_2_0001</a></td>
   
   <td class="ae">
  0.508
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.513
  </td>
   
   <td class="ae-details">
  0.330
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.401
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.021
  </td>
   
   <td class="ee-details">
  15.998
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0002.jpg">bandage_2_0002</a></td>
   
   <td class="ae">
  0.499
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.496
  </td>
   
   <td class="ae-details">
  0.590
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.444
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.918
  </td>
   
   <td class="ee-details">
  19.226
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0003.jpg">bandage_2_0003</a></td>
   
   <td class="ae">
  0.499
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.504
  </td>
   
   <td class="ae-details">
  0.368
  </td>
   
   <td class="ae-details">
  0.356
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.566
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.959
  </td>
   
   <td class="ee-details">
  18.505
  </td>
   
   <td class="ee-details">
  23.265
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0004.jpg">bandage_2_0004</a></td>
   
   <td class="ae">
  0.525
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.534
  </td>
   
   <td class="ae-details">
  0.323
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.810
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.083
  </td>
   
   <td class="ee-details">
  16.674
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0005.jpg">bandage_2_0005</a></td>
   
   <td class="ae">
  0.570
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.555
  </td>
   
   <td class="ae-details">
  0.805
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.378
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.983
  </td>
   
   <td class="ee-details">
  24.191
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0006.jpg">bandage_2_0006</a></td>
   
   <td class="ae">
  0.560
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.587
  </td>
   
   <td class="ae-details">
  0.212
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.898
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.198
  </td>
   
   <td class="ee-details">
  10.853
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0007.jpg">bandage_2_0007</a></td>
   
   <td class="ae">
  0.568
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.598
  </td>
   
   <td class="ae-details">
  0.239
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.976
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.434
  </td>
   
   <td class="ee-details">
  7.908
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0008.jpg">bandage_2_0008</a></td>
   
   <td class="ae">
  0.564
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.595
  </td>
   
   <td class="ae-details">
  0.304
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.167
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.504
  </td>
   
   <td class="ee-details">
  7.758
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.106
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0009.jpg">bandage_2_0009</a></td>
   
   <td class="ae">
  0.552
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.593
  </td>
   
   <td class="ae-details">
  0.305
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.308
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.557
  </td>
   
   <td class="ee-details">
  6.803
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0010.jpg">bandage_2_0010</a></td>
   
   <td class="ae">
  0.532
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.591
  </td>
   
   <td class="ae-details">
  0.249
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.263
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.536
  </td>
   
   <td class="ee-details">
  5.803
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0011.jpg">bandage_2_0011</a></td>
   
   <td class="ae">
  0.512
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.585
  </td>
   
   <td class="ae-details">
  0.195
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.235
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.537
  </td>
   
   <td class="ee-details">
  5.250
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0012.jpg">bandage_2_0012</a></td>
   
   <td class="ae">
  0.500
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.573
  </td>
   
   <td class="ae-details">
  0.170
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.123
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.555
  </td>
   
   <td class="ee-details">
  4.719
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0013.jpg">bandage_2_0013</a></td>
   
   <td class="ae">
  0.487
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.549
  </td>
   
   <td class="ae-details">
  0.178
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.872
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.458
  </td>
   
   <td class="ee-details">
  3.917
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0014.jpg">bandage_2_0014</a></td>
   
   <td class="ae">
  0.476
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.518
  </td>
   
   <td class="ae-details">
  0.201
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.729
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.466
  </td>
   
   <td class="ee-details">
  3.454
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.067
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0015.jpg">bandage_2_0015</a></td>
   
   <td class="ae">
  0.465
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.499
  </td>
   
   <td class="ae-details">
  0.220
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.705
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.472
  </td>
   
   <td class="ee-details">
  3.373
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.117
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0016.jpg">bandage_2_0016</a></td>
   
   <td class="ae">
  0.451
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.493
  </td>
   
   <td class="ae-details">
  0.184
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.649
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.398
  </td>
   
   <td class="ee-details">
  3.259
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.092
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0017.jpg">bandage_2_0017</a></td>
   
   <td class="ae">
  0.452
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.476
  </td>
   
   <td class="ae-details">
  0.232
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.620
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.351
  </td>
   
   <td class="ee-details">
  4.079
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0018.jpg">bandage_2_0018</a></td>
   
   <td class="ae">
  0.457
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.475
  </td>
   
   <td class="ae-details">
  0.248
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.548
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.266
  </td>
   
   <td class="ee-details">
  4.811
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0019.jpg">bandage_2_0019</a></td>
   
   <td class="ae">
  0.444
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.454
  </td>
   
   <td class="ae-details">
  0.261
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.400
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.192
  </td>
   
   <td class="ee-details">
  5.634
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0020.jpg">bandage_2_0020</a></td>
   
   <td class="ae">
  0.471
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.473
  </td>
   
   <td class="ae-details">
  0.380
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.338
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.207
  </td>
   
   <td class="ee-details">
  6.342
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0021.jpg">bandage_2_0021</a></td>
   
   <td class="ae">
  0.475
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.475
  </td>
   
   <td class="ae-details">
  0.651
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.237
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.190
  </td>
   
   <td class="ee-details">
  12.049
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0022.jpg">bandage_2_0022</a></td>
   
   <td class="ae">
  0.460
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.458
  </td>
   
   <td class="ae-details">
  0.697
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.185
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.128
  </td>
   
   <td class="ee-details">
  9.096
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0023.jpg">bandage_2_0023</a></td>
   
   <td class="ae">
  0.440
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.442
  </td>
   
   <td class="ae-details">
  0.232
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.188
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.147
  </td>
   
   <td class="ee-details">
  6.035
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0024.jpg">bandage_2_0024</a></td>
   
   <td class="ae">
  0.449
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.454
  </td>
   
   <td class="ae-details">
  0.182
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.290
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.238
  </td>
   
   <td class="ee-details">
  4.192
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0025.jpg">bandage_2_0025</a></td>
   
   <td class="ae">
  0.446
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.457
  </td>
   
   <td class="ae-details">
  0.203
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.358
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.260
  </td>
   
   <td class="ee-details">
  3.590
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.063
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0026.jpg">bandage_2_0026</a></td>
   
   <td class="ae">
  0.462
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.486
  </td>
   
   <td class="ae-details">
  0.197
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.434
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.297
  </td>
   
   <td class="ee-details">
  2.960
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0027.jpg">bandage_2_0027</a></td>
   
   <td class="ae">
  0.455
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.485
  </td>
   
   <td class="ae-details">
  0.177
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.441
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.238
  </td>
   
   <td class="ee-details">
  3.310
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0028.jpg">bandage_2_0028</a></td>
   
   <td class="ae">
  0.450
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.481
  </td>
   
   <td class="ae-details">
  0.144
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.434
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.183
  </td>
   
   <td class="ee-details">
  3.925
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0029.jpg">bandage_2_0029</a></td>
   
   <td class="ae">
  0.451
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.478
  </td>
   
   <td class="ae-details">
  0.104
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.398
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.177
  </td>
   
   <td class="ee-details">
  4.169
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0030.jpg">bandage_2_0030</a></td>
   
   <td class="ae">
  0.460
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.478
  </td>
   
   <td class="ae-details">
  0.201
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.365
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.144
  </td>
   
   <td class="ee-details">
  4.606
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0031.jpg">bandage_2_0031</a></td>
   
   <td class="ae">
  0.469
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.480
  </td>
   
   <td class="ae-details">
  0.271
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.292
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.085
  </td>
   
   <td class="ee-details">
  4.827
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0032.jpg">bandage_2_0032</a></td>
   
   <td class="ae">
  0.477
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.486
  </td>
   
   <td class="ae-details">
  0.293
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.276
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.112
  </td>
   
   <td class="ee-details">
  4.663
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0033.jpg">bandage_2_0033</a></td>
   
   <td class="ae">
  0.476
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.481
  </td>
   
   <td class="ae-details">
  0.304
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.207
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.119
  </td>
   
   <td class="ee-details">
  4.405
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.115
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0034.jpg">bandage_2_0034</a></td>
   
   <td class="ae">
  0.490
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.491
  </td>
   
   <td class="ae-details">
  0.328
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.140
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.120
  </td>
   
   <td class="ee-details">
  4.070
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.097
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0035.jpg">bandage_2_0035</a></td>
   
   <td class="ae">
  0.508
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.508
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.068
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.068
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0036.jpg">bandage_2_0036</a></td>
   
   <td class="ae">
  0.502
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.502
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.012
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.012
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0037.jpg">bandage_2_0037</a></td>
   
   <td class="ae">
  0.511
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.511
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.034
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.034
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0038.jpg">bandage_2_0038</a></td>
   
   <td class="ae">
  0.513
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.513
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.003
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.003
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0039.jpg">bandage_2_0039</a></td>
   
   <td class="ae">
  0.519
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.519
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.940
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.940
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0040.jpg">bandage_2_0040</a></td>
   
   <td class="ae">
  0.529
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.529
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.902
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.902
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0041.jpg">bandage_2_0041</a></td>
   
   <td class="ae">
  0.526
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.526
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.902
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.902
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0042.jpg">bandage_2_0042</a></td>
   
   <td class="ae">
  0.518
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.518
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.918
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.918
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0043.jpg">bandage_2_0043</a></td>
   
   <td class="ae">
  0.518
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.518
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.958
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.958
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0044.jpg">bandage_2_0044</a></td>
   
   <td class="ae">
  0.527
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.527
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.978
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.978
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.064
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0045.jpg">bandage_2_0045</a></td>
   
   <td class="ae">
  0.536
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.536
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.943
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.943
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.096
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0046.jpg">bandage_2_0046</a></td>
   
   <td class="ae">
  0.544
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.544
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.885
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.885
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.085
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0047.jpg">bandage_2_0047</a></td>
   
   <td class="ae">
  0.539
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.539
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.828
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.828
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0048.jpg">bandage_2_0048</a></td>
   
   <td class="ae">
  0.561
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.561
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.829
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.829
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/bandage_2_0049.jpg">bandage_2_0049</a></td>
   
   <td class="ae">
  0.564
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.564
  </td>
   
   <td class="ae-details">
  0.883
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.836
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.835
  </td>
   
   <td class="ee-details">
  9.083
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0001.jpg">cave_2_0001</a></td>
   
   <td class="ae">
  0.248
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.392
  </td>
   
   <td class="ae-details">
  0.228
  </td>
   
   <td class="ae-details">
  0.401
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.055
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.474
  </td>
   
   <td class="ee-details">
  5.060
  </td>
   
   <td class="ee-details">
  20.745
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0002.jpg">cave_2_0002</a></td>
   
   <td class="ae">
  0.232
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.355
  </td>
   
   <td class="ae-details">
  0.215
  </td>
   
   <td class="ae-details">
  0.029
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.770
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.217
  </td>
   
   <td class="ee-details">
  4.832
  </td>
   
   <td class="ee-details">
  15.494
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0003.jpg">cave_2_0003</a></td>
   
   <td class="ae">
  0.216
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.318
  </td>
   
   <td class="ae-details">
  0.194
  </td>
   
   <td class="ae-details">
  0.051
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.556
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.201
  </td>
   
   <td class="ee-details">
  4.839
  </td>
   
   <td class="ee-details">
  14.520
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.061
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0004.jpg">cave_2_0004</a></td>
   
   <td class="ae">
  0.227
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.349
  </td>
   
   <td class="ae-details">
  0.186
  </td>
   
   <td class="ae-details">
  2.533
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.819
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.424
  </td>
   
   <td class="ee-details">
  4.944
  </td>
   
   <td class="ee-details">
  53.207
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0005.jpg">cave_2_0005</a></td>
   
   <td class="ae">
  0.249
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.453
  </td>
   
   <td class="ae-details">
  0.219
  </td>
   
   <td class="ae-details">
  1.537
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.776
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.862
  </td>
   
   <td class="ee-details">
  5.601
  </td>
   
   <td class="ee-details">
  40.911
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.063
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0006.jpg">cave_2_0006</a></td>
   
   <td class="ae">
  0.300
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.588
  </td>
   
   <td class="ae-details">
  0.286
  </td>
   
   <td class="ae-details">
  0.549
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  7.105
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  5.584
  </td>
   
   <td class="ee-details">
  6.980
  </td>
   
   <td class="ee-details">
  28.068
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.067
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0007.jpg">cave_2_0007</a></td>
   
   <td class="ae">
  0.361
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.749
  </td>
   
   <td class="ae-details">
  0.323
  </td>
   
   <td class="ae-details">
  1.024
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  8.457
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.837
  </td>
   
   <td class="ee-details">
  8.672
  </td>
   
   <td class="ee-details">
  37.656
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0008.jpg">cave_2_0008</a></td>
   
   <td class="ae">
  0.726
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.338
  </td>
   
   <td class="ae-details">
  0.726
  </td>
   
   <td class="ae-details">
  2.529
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  15.935
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.453
  </td>
   
   <td class="ee-details">
  16.115
  </td>
   
   <td class="ee-details">
  53.090
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0009.jpg">cave_2_0009</a></td>
   
   <td class="ae">
  0.674
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.686
  </td>
   
   <td class="ae-details">
  0.605
  </td>
   
   <td class="ae-details">
  1.388
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  17.337
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  6.049
  </td>
   
   <td class="ee-details">
  15.393
  </td>
   
   <td class="ee-details">
  42.411
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0010.jpg">cave_2_0010</a></td>
   
   <td class="ae">
  0.549
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.384
  </td>
   
   <td class="ae-details">
  0.483
  </td>
   
   <td class="ae-details">
  0.960
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  17.005
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  5.029
  </td>
   
   <td class="ee-details">
  13.936
  </td>
   
   <td class="ee-details">
  38.357
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0011.jpg">cave_2_0011</a></td>
   
   <td class="ae">
  0.733
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.494
  </td>
   
   <td class="ae-details">
  0.727
  </td>
   
   <td class="ae-details">
  0.982
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  19.594
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.615
  </td>
   
   <td class="ee-details">
  18.100
  </td>
   
   <td class="ee-details">
  39.140
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.081
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0012.jpg">cave_2_0012</a></td>
   
   <td class="ae">
  0.815
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.832
  </td>
   
   <td class="ae-details">
  0.798
  </td>
   
   <td class="ae-details">
  0.857
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  22.104
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  6.200
  </td>
   
   <td class="ee-details">
  19.399
  </td>
   
   <td class="ee-details">
  39.675
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0013.jpg">cave_2_0013</a></td>
   
   <td class="ae">
  0.740
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.540
  </td>
   
   <td class="ae-details">
  0.707
  </td>
   
   <td class="ae-details">
  0.854
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  25.140
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.554
  </td>
   
   <td class="ee-details">
  19.145
  </td>
   
   <td class="ee-details">
  41.652
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0014.jpg">cave_2_0014</a></td>
   
   <td class="ae">
  0.887
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.674
  </td>
   
   <td class="ae-details">
  1.062
  </td>
   
   <td class="ae-details">
  0.749
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  31.791
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  5.329
  </td>
   
   <td class="ee-details">
  26.245
  </td>
   
   <td class="ee-details">
  45.168
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0015.jpg">cave_2_0015</a></td>
   
   <td class="ae">
  1.008
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.780
  </td>
   
   <td class="ae-details">
  1.120
  </td>
   
   <td class="ae-details">
  0.974
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  34.718
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.699
  </td>
   
   <td class="ee-details">
  26.781
  </td>
   
   <td class="ee-details">
  47.740
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0016.jpg">cave_2_0016</a></td>
   
   <td class="ae">
  1.089
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.653
  </td>
   
   <td class="ae-details">
  1.016
  </td>
   
   <td class="ae-details">
  1.161
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  38.520
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  5.530
  </td>
   
   <td class="ee-details">
  24.579
  </td>
   
   <td class="ee-details">
  49.718
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.111
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0017.jpg">cave_2_0017</a></td>
   
   <td class="ae">
  1.133
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.283
  </td>
   
   <td class="ae-details">
  1.005
  </td>
   
   <td class="ae-details">
  1.201
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  42.101
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  10.446
  </td>
   
   <td class="ee-details">
  25.255
  </td>
   
   <td class="ee-details">
  51.965
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.113
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0018.jpg">cave_2_0018</a></td>
   
   <td class="ae">
  0.911
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.383
  </td>
   
   <td class="ae-details">
  0.918
  </td>
   
   <td class="ae-details">
  0.922
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  43.573
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  5.079
  </td>
   
   <td class="ee-details">
  28.871
  </td>
   
   <td class="ee-details">
  48.958
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0019.jpg">cave_2_0019</a></td>
   
   <td class="ae">
  0.875
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.303
  </td>
   
   <td class="ae-details">
  0.700
  </td>
   
   <td class="ae-details">
  0.919
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  46.281
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  7.320
  </td>
   
   <td class="ee-details">
  24.191
  </td>
   
   <td class="ee-details">
  50.887
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.065
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0020.jpg">cave_2_0020</a></td>
   
   <td class="ae">
  0.906
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.397
  </td>
   
   <td class="ae-details">
  0.705
  </td>
   
   <td class="ae-details">
  0.943
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  48.569
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.891
  </td>
   
   <td class="ee-details">
  19.194
  </td>
   
   <td class="ee-details">
  52.925
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0021.jpg">cave_2_0021</a></td>
   
   <td class="ae">
  0.910
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.276
  </td>
   
   <td class="ae-details">
  0.454
  </td>
   
   <td class="ae-details">
  0.972
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  51.380
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.882
  </td>
   
   <td class="ee-details">
  12.735
  </td>
   
   <td class="ee-details">
  56.451
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0022.jpg">cave_2_0022</a></td>
   
   <td class="ae">
  1.046
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.424
  </td>
   
   <td class="ae-details">
  0.581
  </td>
   
   <td class="ae-details">
  1.105
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  62.701
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.819
  </td>
   
   <td class="ee-details">
  9.323
  </td>
   
   <td class="ee-details">
  68.703
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0023.jpg">cave_2_0023</a></td>
   
   <td class="ae">
  1.341
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.518
  </td>
   
   <td class="ae-details">
  0.345
  </td>
   
   <td class="ae-details">
  1.437
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  78.713
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.451
  </td>
   
   <td class="ee-details">
  6.615
  </td>
   
   <td class="ee-details">
  86.162
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0024.jpg">cave_2_0024</a></td>
   
   <td class="ae">
  1.208
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.463
  </td>
   
   <td class="ae-details">
  0.325
  </td>
   
   <td class="ae-details">
  1.270
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  77.089
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.200
  </td>
   
   <td class="ee-details">
  10.624
  </td>
   
   <td class="ee-details">
  81.893
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0025.jpg">cave_2_0025</a></td>
   
   <td class="ae">
  1.122
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.778
  </td>
   
   <td class="ae-details">
  0.518
  </td>
   
   <td class="ae-details">
  1.158
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  83.119
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  7.459
  </td>
   
   <td class="ee-details">
  14.617
  </td>
   
   <td class="ee-details">
  87.208
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0026.jpg">cave_2_0026</a></td>
   
   <td class="ae">
  1.034
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.318
  </td>
   
   <td class="ae-details">
  1.074
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  63.866
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  11.829
  </td>
   
   <td class="ee-details">
  66.759
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0027.jpg">cave_2_0027</a></td>
   
   <td class="ae">
  1.256
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.670
  </td>
   
   <td class="ae-details">
  0.342
  </td>
   
   <td class="ae-details">
  1.319
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  63.034
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.910
  </td>
   
   <td class="ee-details">
  15.269
  </td>
   
   <td class="ee-details">
  66.357
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.062
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0028.jpg">cave_2_0028</a></td>
   
   <td class="ae">
  1.206
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.845
  </td>
   
   <td class="ae-details">
  0.323
  </td>
   
   <td class="ae-details">
  1.300
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  61.813
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  8.412
  </td>
   
   <td class="ee-details">
  10.963
  </td>
   
   <td class="ee-details">
  67.311
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.125
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0029.jpg">cave_2_0029</a></td>
   
   <td class="ae">
  1.110
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.636
  </td>
   
   <td class="ae-details">
  0.479
  </td>
   
   <td class="ae-details">
  1.183
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  66.053
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.655
  </td>
   
   <td class="ee-details">
  14.090
  </td>
   
   <td class="ee-details">
  72.280
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0030.jpg">cave_2_0030</a></td>
   
   <td class="ae">
  1.206
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.257
  </td>
   
   <td class="ae-details">
  0.543
  </td>
   
   <td class="ae-details">
  1.294
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  72.888
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.084
  </td>
   
   <td class="ee-details">
  11.292
  </td>
   
   <td class="ee-details">
  80.624
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0031.jpg">cave_2_0031</a></td>
   
   <td class="ae">
  1.006
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.345
  </td>
   
   <td class="ae-details">
  0.629
  </td>
   
   <td class="ae-details">
  1.083
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  65.474
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.312
  </td>
   
   <td class="ee-details">
  17.553
  </td>
   
   <td class="ee-details">
  74.359
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0032.jpg">cave_2_0032</a></td>
   
   <td class="ae">
  1.016
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.533
  </td>
   
   <td class="ae-details">
  0.522
  </td>
   
   <td class="ae-details">
  1.135
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  66.988
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.529
  </td>
   
   <td class="ee-details">
  14.729
  </td>
   
   <td class="ee-details">
  80.192
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0033.jpg">cave_2_0033</a></td>
   
   <td class="ae">
  0.735
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.650
  </td>
   
   <td class="ae-details">
  0.386
  </td>
   
   <td class="ae-details">
  0.818
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  52.266
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.290
  </td>
   
   <td class="ee-details">
  10.089
  </td>
   
   <td class="ee-details">
  64.521
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0034.jpg">cave_2_0034</a></td>
   
   <td class="ae">
  0.541
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.370
  </td>
   
   <td class="ae-details">
  0.276
  </td>
   
   <td class="ae-details">
  0.604
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  46.481
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  5.378
  </td>
   
   <td class="ee-details">
  10.181
  </td>
   
   <td class="ee-details">
  55.595
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0035.jpg">cave_2_0035</a></td>
   
   <td class="ae">
  0.617
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.113
  </td>
   
   <td class="ae-details">
  0.340
  </td>
   
   <td class="ae-details">
  0.681
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  45.229
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  8.616
  </td>
   
   <td class="ee-details">
  11.746
  </td>
   
   <td class="ee-details">
  53.411
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0036.jpg">cave_2_0036</a></td>
   
   <td class="ae">
  0.542
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.588
  </td>
   
   <td class="ae-details">
  0.225
  </td>
   
   <td class="ae-details">
  0.627
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  41.556
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.231
  </td>
   
   <td class="ee-details">
  8.914
  </td>
   
   <td class="ee-details">
  51.091
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0037.jpg">cave_2_0037</a></td>
   
   <td class="ae">
  0.574
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.383
  </td>
   
   <td class="ae-details">
  0.659
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  37.441
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  14.155
  </td>
   
   <td class="ee-details">
  47.829
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0038.jpg">cave_2_0038</a></td>
   
   <td class="ae">
  0.603
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.281
  </td>
   
   <td class="ae-details">
  0.721
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  37.067
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  13.895
  </td>
   
   <td class="ee-details">
  45.568
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.083
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0039.jpg">cave_2_0039</a></td>
   
   <td class="ae">
  0.611
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.406
  </td>
   
   <td class="ae-details">
  0.706
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  31.591
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  13.742
  </td>
   
   <td class="ee-details">
  39.794
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0040.jpg">cave_2_0040</a></td>
   
   <td class="ae">
  0.736
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.387
  </td>
   
   <td class="ae-details">
  0.922
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  30.396
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  15.714
  </td>
   
   <td class="ee-details">
  38.201
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.082
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0041.jpg">cave_2_0041</a></td>
   
   <td class="ae">
  0.708
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.266
  </td>
   
   <td class="ae-details">
  0.560
  </td>
   
   <td class="ae-details">
  1.025
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  25.553
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.793
  </td>
   
   <td class="ee-details">
  19.435
  </td>
   
   <td class="ee-details">
  38.754
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0042.jpg">cave_2_0042</a></td>
   
   <td class="ae">
  0.422
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.376
  </td>
   
   <td class="ae-details">
  1.308
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  14.432
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  12.904
  </td>
   
   <td class="ee-details">
  43.379
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0043.jpg">cave_2_0043</a></td>
   
   <td class="ae">
  0.128
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.313
  </td>
   
   <td class="ae-details">
  0.119
  </td>
   
   <td class="ae-details">
  0.429
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.665
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.655
  </td>
   
   <td class="ee-details">
  5.777
  </td>
   
   <td class="ee-details">
  22.391
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0044.jpg">cave_2_0044</a></td>
   
   <td class="ae">
  0.178
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.305
  </td>
   
   <td class="ae-details">
  0.172
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.339
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.307
  </td>
   
   <td class="ee-details">
  4.390
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0045.jpg">cave_2_0045</a></td>
   
   <td class="ae">
  0.231
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.233
  </td>
   
   <td class="ae-details">
  0.230
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.554
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.601
  </td>
   
   <td class="ee-details">
  3.959
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0046.jpg">cave_2_0046</a></td>
   
   <td class="ae">
  0.349
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.366
  </td>
   
   <td class="ae-details">
  0.227
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.216
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.926
  </td>
   
   <td class="ee-details">
  4.255
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0047.jpg">cave_2_0047</a></td>
   
   <td class="ae">
  0.304
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.338
  </td>
   
   <td class="ae-details">
  0.284
  </td>
   
   <td class="ae-details">
  0.110
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.221
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.746
  </td>
   
   <td class="ee-details">
  5.630
  </td>
   
   <td class="ee-details">
  26.632
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0048.jpg">cave_2_0048</a></td>
   
   <td class="ae">
  0.222
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.261
  </td>
   
   <td class="ae-details">
  0.161
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.955
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.255
  </td>
   
   <td class="ee-details">
  5.032
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.083
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_2_0049.jpg">cave_2_0049</a></td>
   
   <td class="ae">
  0.245
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.284
  </td>
   
   <td class="ae-details">
  0.206
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.009
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.305
  </td>
   
   <td class="ee-details">
  4.731
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.081
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0001.jpg">cave_4_0001</a></td>
   
   <td class="ae">
  0.410
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.463
  </td>
   
   <td class="ae-details">
  0.365
  </td>
   
   <td class="ae-details">
  0.807
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  6.394
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.356
  </td>
   
   <td class="ee-details">
  6.565
  </td>
   
   <td class="ee-details">
  56.379
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.083
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0002.jpg">cave_4_0002</a></td>
   
   <td class="ae">
  0.459
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.469
  </td>
   
   <td class="ae-details">
  0.407
  </td>
   
   <td class="ae-details">
  1.153
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  7.647
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.344
  </td>
   
   <td class="ee-details">
  7.650
  </td>
   
   <td class="ee-details">
  57.241
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0003.jpg">cave_4_0003</a></td>
   
   <td class="ae">
  0.375
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.387
  </td>
   
   <td class="ae-details">
  0.322
  </td>
   
   <td class="ae-details">
  0.857
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  6.271
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.439
  </td>
   
   <td class="ee-details">
  5.514
  </td>
   
   <td class="ee-details">
  45.324
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0004.jpg">cave_4_0004</a></td>
   
   <td class="ae">
  0.288
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.386
  </td>
   
   <td class="ae-details">
  0.211
  </td>
   
   <td class="ae-details">
  0.625
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.184
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.618
  </td>
   
   <td class="ee-details">
  5.164
  </td>
   
   <td class="ee-details">
  60.211
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.100
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0005.jpg">cave_4_0005</a></td>
   
   <td class="ae">
  0.304
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.336
  </td>
   
   <td class="ae-details">
  0.249
  </td>
   
   <td class="ae-details">
  0.820
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  7.902
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.444
  </td>
   
   <td class="ee-details">
  7.612
  </td>
   
   <td class="ee-details">
  60.647
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.100
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0006.jpg">cave_4_0006</a></td>
   
   <td class="ae">
  0.314
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.331
  </td>
   
   <td class="ae-details">
  0.274
  </td>
   
   <td class="ae-details">
  0.535
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  8.639
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.632
  </td>
   
   <td class="ee-details">
  7.241
  </td>
   
   <td class="ee-details">
  37.695
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0007.jpg">cave_4_0007</a></td>
   
   <td class="ae">
  0.370
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.270
  </td>
   
   <td class="ae-details">
  0.320
  </td>
   
   <td class="ae-details">
  1.128
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  9.306
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.205
  </td>
   
   <td class="ee-details">
  7.551
  </td>
   
   <td class="ee-details">
  44.510
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0008.jpg">cave_4_0008</a></td>
   
   <td class="ae">
  0.369
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.346
  </td>
   
   <td class="ae-details">
  0.290
  </td>
   
   <td class="ae-details">
  1.849
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  10.391
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.083
  </td>
   
   <td class="ee-details">
  6.929
  </td>
   
   <td class="ee-details">
  102.341
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0009.jpg">cave_4_0009</a></td>
   
   <td class="ae">
  0.335
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.523
  </td>
   
   <td class="ae-details">
  0.244
  </td>
   
   <td class="ae-details">
  1.020
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  9.190
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.931
  </td>
   
   <td class="ee-details">
  5.631
  </td>
   
   <td class="ee-details">
  99.366
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0010.jpg">cave_4_0010</a></td>
   
   <td class="ae">
  0.361
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.501
  </td>
   
   <td class="ae-details">
  0.255
  </td>
   
   <td class="ae-details">
  1.217
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  9.989
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.088
  </td>
   
   <td class="ee-details">
  5.812
  </td>
   
   <td class="ee-details">
  171.333
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0011.jpg">cave_4_0011</a></td>
   
   <td class="ae">
  0.354
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.409
  </td>
   
   <td class="ae-details">
  0.255
  </td>
   
   <td class="ae-details">
  1.728
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  7.945
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.618
  </td>
   
   <td class="ee-details">
  5.020
  </td>
   
   <td class="ee-details">
  108.951
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0012.jpg">cave_4_0012</a></td>
   
   <td class="ae">
  0.369
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.510
  </td>
   
   <td class="ae-details">
  0.291
  </td>
   
   <td class="ae-details">
  0.771
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.932
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.902
  </td>
   
   <td class="ee-details">
  5.480
  </td>
   
   <td class="ee-details">
  49.999
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0013.jpg">cave_4_0013</a></td>
   
   <td class="ae">
  0.394
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.493
  </td>
   
   <td class="ae-details">
  0.353
  </td>
   
   <td class="ae-details">
  0.537
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  7.083
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.989
  </td>
   
   <td class="ee-details">
  7.106
  </td>
   
   <td class="ee-details">
  49.102
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0014.jpg">cave_4_0014</a></td>
   
   <td class="ae">
  0.432
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.526
  </td>
   
   <td class="ae-details">
  0.376
  </td>
   
   <td class="ae-details">
  1.461
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  6.531
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.516
  </td>
   
   <td class="ee-details">
  7.041
  </td>
   
   <td class="ee-details">
  47.731
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0015.jpg">cave_4_0015</a></td>
   
   <td class="ae">
  0.315
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.498
  </td>
   
   <td class="ae-details">
  0.224
  </td>
   
   <td class="ae-details">
  0.631
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.544
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.101
  </td>
   
   <td class="ee-details">
  4.868
  </td>
   
   <td class="ee-details">
  49.642
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0016.jpg">cave_4_0016</a></td>
   
   <td class="ae">
  0.296
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.427
  </td>
   
   <td class="ae-details">
  0.254
  </td>
   
   <td class="ae-details">
  0.294
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  7.424
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.718
  </td>
   
   <td class="ee-details">
  6.466
  </td>
   
   <td class="ee-details">
  43.239
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0017.jpg">cave_4_0017</a></td>
   
   <td class="ae">
  0.279
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.394
  </td>
   
   <td class="ae-details">
  0.230
  </td>
   
   <td class="ae-details">
  0.358
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.939
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.193
  </td>
   
   <td class="ee-details">
  5.743
  </td>
   
   <td class="ee-details">
  28.777
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.093
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0018.jpg">cave_4_0018</a></td>
   
   <td class="ae">
  0.227
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.333
  </td>
   
   <td class="ae-details">
  0.187
  </td>
   
   <td class="ae-details">
  0.363
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.710
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.918
  </td>
   
   <td class="ee-details">
  4.593
  </td>
   
   <td class="ee-details">
  24.296
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0019.jpg">cave_4_0019</a></td>
   
   <td class="ae">
  0.235
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.263
  </td>
   
   <td class="ae-details">
  0.216
  </td>
   
   <td class="ae-details">
  0.533
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.407
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.611
  </td>
   
   <td class="ee-details">
  4.698
  </td>
   
   <td class="ee-details">
  43.943
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0020.jpg">cave_4_0020</a></td>
   
   <td class="ae">
  0.268
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.351
  </td>
   
   <td class="ae-details">
  0.243
  </td>
   
   <td class="ae-details">
  0.529
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.638
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.742
  </td>
   
   <td class="ee-details">
  5.391
  </td>
   
   <td class="ee-details">
  52.977
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0021.jpg">cave_4_0021</a></td>
   
   <td class="ae">
  0.236
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.260
  </td>
   
   <td class="ae-details">
  0.231
  </td>
   
   <td class="ae-details">
  0.261
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.536
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.679
  </td>
   
   <td class="ee-details">
  4.623
  </td>
   
   <td class="ee-details">
  30.252
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0022.jpg">cave_4_0022</a></td>
   
   <td class="ae">
  0.195
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.339
  </td>
   
   <td class="ae-details">
  0.173
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.118
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.250
  </td>
   
   <td class="ee-details">
  4.098
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0023.jpg">cave_4_0023</a></td>
   
   <td class="ae">
  0.189
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.169
  </td>
   
   <td class="ae-details">
  0.191
  </td>
   
   <td class="ae-details">
  1.630
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.518
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.115
  </td>
   
   <td class="ee-details">
  4.671
  </td>
   
   <td class="ee-details">
  51.188
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0024.jpg">cave_4_0024</a></td>
   
   <td class="ae">
  0.196
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.137
  </td>
   
   <td class="ae-details">
  0.193
  </td>
   
   <td class="ae-details">
  2.494
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.741
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.812
  </td>
   
   <td class="ee-details">
  4.662
  </td>
   
   <td class="ee-details">
  74.975
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.119
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0025.jpg">cave_4_0025</a></td>
   
   <td class="ae">
  0.183
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.124
  </td>
   
   <td class="ae-details">
  0.176
  </td>
   
   <td class="ae-details">
  1.365
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.894
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.813
  </td>
   
   <td class="ee-details">
  4.515
  </td>
   
   <td class="ee-details">
  58.986
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.096
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0026.jpg">cave_4_0026</a></td>
   
   <td class="ae">
  0.189
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.220
  </td>
   
   <td class="ae-details">
  0.154
  </td>
   
   <td class="ae-details">
  1.761
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.064
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.154
  </td>
   
   <td class="ee-details">
  4.326
  </td>
   
   <td class="ee-details">
  56.486
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0027.jpg">cave_4_0027</a></td>
   
   <td class="ae">
  0.209
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.176
  </td>
   
   <td class="ae-details">
  0.194
  </td>
   
   <td class="ae-details">
  1.982
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.864
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.432
  </td>
   
   <td class="ee-details">
  4.908
  </td>
   
   <td class="ee-details">
  57.409
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0028.jpg">cave_4_0028</a></td>
   
   <td class="ae">
  0.201
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.224
  </td>
   
   <td class="ae-details">
  0.188
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.798
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.500
  </td>
   
   <td class="ee-details">
  4.504
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.064
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0029.jpg">cave_4_0029</a></td>
   
   <td class="ae">
  0.198
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.282
  </td>
   
   <td class="ae-details">
  0.122
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.326
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.710
  </td>
   
   <td class="ee-details">
  3.878
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.067
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0030.jpg">cave_4_0030</a></td>
   
   <td class="ae">
  0.232
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.275
  </td>
   
   <td class="ae-details">
  0.175
  </td>
   
   <td class="ae-details">
  0.195
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.556
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.510
  </td>
   
   <td class="ee-details">
  4.863
  </td>
   
   <td class="ee-details">
  25.122
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0031.jpg">cave_4_0031</a></td>
   
   <td class="ae">
  0.211
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.198
  </td>
   
   <td class="ae-details">
  0.218
  </td>
   
   <td class="ae-details">
  0.805
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.472
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.073
  </td>
   
   <td class="ee-details">
  5.630
  </td>
   
   <td class="ee-details">
  33.797
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0032.jpg">cave_4_0032</a></td>
   
   <td class="ae">
  0.234
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.203
  </td>
   
   <td class="ae-details">
  0.380
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.176
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.820
  </td>
   
   <td class="ee-details">
  9.651
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0033.jpg">cave_4_0033</a></td>
   
   <td class="ae">
  0.276
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.256
  </td>
   
   <td class="ae-details">
  0.430
  </td>
   
   <td class="ae-details">
  0.373
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.392
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.640
  </td>
   
   <td class="ee-details">
  7.844
  </td>
   
   <td class="ee-details">
  27.644
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0034.jpg">cave_4_0034</a></td>
   
   <td class="ae">
  0.288
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.281
  </td>
   
   <td class="ae-details">
  0.386
  </td>
   
   <td class="ae-details">
  2.745
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.072
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.770
  </td>
   
   <td class="ee-details">
  6.832
  </td>
   
   <td class="ee-details">
  48.551
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0035.jpg">cave_4_0035</a></td>
   
   <td class="ae">
  0.272
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.256
  </td>
   
   <td class="ae-details">
  0.466
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.279
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.874
  </td>
   
   <td class="ee-details">
  7.125
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0036.jpg">cave_4_0036</a></td>
   
   <td class="ae">
  0.302
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.297
  </td>
   
   <td class="ae-details">
  0.337
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.512
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.935
  </td>
   
   <td class="ee-details">
  6.952
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0037.jpg">cave_4_0037</a></td>
   
   <td class="ae">
  0.392
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.388
  </td>
   
   <td class="ae-details">
  0.427
  </td>
   
   <td class="ae-details">
  0.063
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.793
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.035
  </td>
   
   <td class="ee-details">
  7.081
  </td>
   
   <td class="ee-details">
  20.197
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0038.jpg">cave_4_0038</a></td>
   
   <td class="ae">
  0.374
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.359
  </td>
   
   <td class="ae-details">
  0.511
  </td>
   
   <td class="ae-details">
  0.749
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.099
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.364
  </td>
   
   <td class="ee-details">
  9.523
  </td>
   
   <td class="ee-details">
  37.916
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0039.jpg">cave_4_0039</a></td>
   
   <td class="ae">
  0.242
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.188
  </td>
   
   <td class="ae-details">
  0.603
  </td>
   
   <td class="ae-details">
  0.109
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.052
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.133
  </td>
   
   <td class="ee-details">
  10.147
  </td>
   
   <td class="ee-details">
  14.567
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0040.jpg">cave_4_0040</a></td>
   
   <td class="ae">
  0.271
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.233
  </td>
   
   <td class="ae-details">
  0.323
  </td>
   
   <td class="ae-details">
  0.206
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.464
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.383
  </td>
   
   <td class="ee-details">
  6.906
  </td>
   
   <td class="ee-details">
  27.853
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.089
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0041.jpg">cave_4_0041</a></td>
   
   <td class="ae">
  0.316
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.913
  </td>
   
   <td class="ae-details">
  0.243
  </td>
   
   <td class="ae-details">
  1.943
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  8.564
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  9.437
  </td>
   
   <td class="ee-details">
  7.656
  </td>
   
   <td class="ee-details">
  52.712
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0042.jpg">cave_4_0042</a></td>
   
   <td class="ae">
  0.419
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.811
  </td>
   
   <td class="ae-details">
  0.245
  </td>
   
   <td class="ae-details">
  1.520
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  15.181
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  10.646
  </td>
   
   <td class="ee-details">
  8.288
  </td>
   
   <td class="ee-details">
  63.071
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0043.jpg">cave_4_0043</a></td>
   
   <td class="ae">
  0.430
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.149
  </td>
   
   <td class="ae-details">
  0.255
  </td>
   
   <td class="ae-details">
  1.020
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  23.076
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  11.484
  </td>
   
   <td class="ee-details">
  8.744
  </td>
   
   <td class="ee-details">
  78.205
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.084
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0044.jpg">cave_4_0044</a></td>
   
   <td class="ae">
  0.713
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.885
  </td>
   
   <td class="ae-details">
  0.428
  </td>
   
   <td class="ae-details">
  1.711
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  31.668
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  11.561
  </td>
   
   <td class="ee-details">
  11.598
  </td>
   
   <td class="ee-details">
  106.493
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0045.jpg">cave_4_0045</a></td>
   
   <td class="ae">
  0.665
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.001
  </td>
   
   <td class="ae-details">
  0.515
  </td>
   
   <td class="ae-details">
  1.586
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  25.241
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  10.700
  </td>
   
   <td class="ee-details">
  12.296
  </td>
   
   <td class="ee-details">
  112.654
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0046.jpg">cave_4_0046</a></td>
   
   <td class="ae">
  0.698
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.313
  </td>
   
   <td class="ae-details">
  0.454
  </td>
   
   <td class="ae-details">
  1.678
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  23.191
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  16.865
  </td>
   
   <td class="ee-details">
  11.174
  </td>
   
   <td class="ee-details">
  76.445
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0047.jpg">cave_4_0047</a></td>
   
   <td class="ae">
  0.779
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  2.022
  </td>
   
   <td class="ae-details">
  0.617
  </td>
   
   <td class="ae-details">
  1.500
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  21.366
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  14.894
  </td>
   
   <td class="ee-details">
  14.335
  </td>
   
   <td class="ee-details">
  62.526
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.105
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0048.jpg">cave_4_0048</a></td>
   
   <td class="ae">
  0.542
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.608
  </td>
   
   <td class="ae-details">
  0.477
  </td>
   
   <td class="ae-details">
  0.747
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  18.727
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.412
  </td>
   
   <td class="ee-details">
  11.628
  </td>
   
   <td class="ee-details">
  53.000
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.083
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/cave_4_0049.jpg">cave_4_0049</a></td>
   
   <td class="ae">
  0.471
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.500
  </td>
   
   <td class="ae-details">
  0.406
  </td>
   
   <td class="ae-details">
  0.828
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  13.189
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  6.049
  </td>
   
   <td class="ee-details">
  9.758
  </td>
   
   <td class="ee-details">
  40.692
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0001.jpg">market_2_0001</a></td>
   
   <td class="ae">
  0.517
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.600
  </td>
   
   <td class="ae-details">
  0.106
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.668
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.388
  </td>
   
   <td class="ee-details">
  3.055
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0002.jpg">market_2_0002</a></td>
   
   <td class="ae">
  0.523
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.583
  </td>
   
   <td class="ae-details">
  0.162
  </td>
   
   <td class="ae-details">
  0.334
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.886
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.405
  </td>
   
   <td class="ee-details">
  4.703
  </td>
   
   <td class="ee-details">
  71.428
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0003.jpg">market_2_0003</a></td>
   
   <td class="ae">
  0.552
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.597
  </td>
   
   <td class="ae-details">
  0.236
  </td>
   
   <td class="ae-details">
  0.773
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.656
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.490
  </td>
   
   <td class="ee-details">
  7.718
  </td>
   
   <td class="ee-details">
  66.697
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.097
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0004.jpg">market_2_0004</a></td>
   
   <td class="ae">
  0.601
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.626
  </td>
   
   <td class="ae-details">
  0.405
  </td>
   
   <td class="ae-details">
  1.765
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.955
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.375
  </td>
   
   <td class="ee-details">
  13.583
  </td>
   
   <td class="ee-details">
  47.851
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.081
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0005.jpg">market_2_0005</a></td>
   
   <td class="ae">
  0.588
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.614
  </td>
   
   <td class="ae-details">
  0.383
  </td>
   
   <td class="ae-details">
  0.445
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.650
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.249
  </td>
   
   <td class="ee-details">
  11.321
  </td>
   
   <td class="ee-details">
  28.648
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0006.jpg">market_2_0006</a></td>
   
   <td class="ae">
  0.552
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.571
  </td>
   
   <td class="ae-details">
  0.396
  </td>
   
   <td class="ae-details">
  0.201
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.219
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.077
  </td>
   
   <td class="ee-details">
  11.353
  </td>
   
   <td class="ee-details">
  22.008
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0007.jpg">market_2_0007</a></td>
   
   <td class="ae">
  0.522
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.539
  </td>
   
   <td class="ae-details">
  0.385
  </td>
   
   <td class="ae-details">
  0.162
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.180
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.006
  </td>
   
   <td class="ee-details">
  11.634
  </td>
   
   <td class="ee-details">
  24.002
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0008.jpg">market_2_0008</a></td>
   
   <td class="ae">
  0.513
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.571
  </td>
   
   <td class="ae-details">
  0.197
  </td>
   
   <td class="ae-details">
  0.296
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.378
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.144
  </td>
   
   <td class="ee-details">
  7.402
  </td>
   
   <td class="ee-details">
  22.166
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0009.jpg">market_2_0009</a></td>
   
   <td class="ae">
  0.490
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.559
  </td>
   
   <td class="ae-details">
  0.191
  </td>
   
   <td class="ae-details">
  0.113
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.155
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.242
  </td>
   
   <td class="ee-details">
  5.593
  </td>
   
   <td class="ee-details">
  12.143
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0010.jpg">market_2_0010</a></td>
   
   <td class="ae">
  0.492
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.553
  </td>
   
   <td class="ae-details">
  0.176
  </td>
   
   <td class="ae-details">
  0.608
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.142
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.220
  </td>
   
   <td class="ee-details">
  4.830
  </td>
   
   <td class="ee-details">
  32.201
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0011.jpg">market_2_0011</a></td>
   
   <td class="ae">
  0.522
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.554
  </td>
   
   <td class="ae-details">
  0.354
  </td>
   
   <td class="ae-details">
  0.310
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.484
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.405
  </td>
   
   <td class="ee-details">
  7.357
  </td>
   
   <td class="ee-details">
  24.403
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0012.jpg">market_2_0012</a></td>
   
   <td class="ae">
  0.513
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.568
  </td>
   
   <td class="ae-details">
  0.249
  </td>
   
   <td class="ae-details">
  0.406
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.458
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.253
  </td>
   
   <td class="ee-details">
  6.837
  </td>
   
   <td class="ee-details">
  30.449
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0013.jpg">market_2_0013</a></td>
   
   <td class="ae">
  0.538
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.591
  </td>
   
   <td class="ae-details">
  0.323
  </td>
   
   <td class="ae-details">
  1.105
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.667
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.336
  </td>
   
   <td class="ee-details">
  7.333
  </td>
   
   <td class="ee-details">
  35.263
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0014.jpg">market_2_0014</a></td>
   
   <td class="ae">
  0.578
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.679
  </td>
   
   <td class="ae-details">
  0.223
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.766
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.055
  </td>
   
   <td class="ee-details">
  5.269
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.083
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0015.jpg">market_2_0015</a></td>
   
   <td class="ae">
  0.610
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.720
  </td>
   
   <td class="ae-details">
  0.252
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.918
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.272
  </td>
   
   <td class="ee-details">
  5.028
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0016.jpg">market_2_0016</a></td>
   
   <td class="ae">
  0.576
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.720
  </td>
   
   <td class="ae-details">
  0.169
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.796
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.228
  </td>
   
   <td class="ee-details">
  4.412
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.081
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0017.jpg">market_2_0017</a></td>
   
   <td class="ae">
  0.597
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.761
  </td>
   
   <td class="ae-details">
  0.124
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.888
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.376
  </td>
   
   <td class="ee-details">
  4.363
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0018.jpg">market_2_0018</a></td>
   
   <td class="ae">
  0.590
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.739
  </td>
   
   <td class="ae-details">
  0.109
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.726
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.252
  </td>
   
   <td class="ee-details">
  4.266
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0019.jpg">market_2_0019</a></td>
   
   <td class="ae">
  0.566
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.680
  </td>
   
   <td class="ae-details">
  0.132
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.462
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.863
  </td>
   
   <td class="ee-details">
  4.754
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0020.jpg">market_2_0020</a></td>
   
   <td class="ae">
  0.591
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.685
  </td>
   
   <td class="ae-details">
  0.168
  </td>
   
   <td class="ae-details">
  0.507
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.986
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.739
  </td>
   
   <td class="ee-details">
  6.228
  </td>
   
   <td class="ee-details">
  21.765
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.088
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0021.jpg">market_2_0021</a></td>
   
   <td class="ae">
  0.623
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.707
  </td>
   
   <td class="ae-details">
  0.186
  </td>
   
   <td class="ae-details">
  0.505
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.477
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.861
  </td>
   
   <td class="ee-details">
  6.067
  </td>
   
   <td class="ee-details">
  24.431
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0022.jpg">market_2_0022</a></td>
   
   <td class="ae">
  0.638
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.706
  </td>
   
   <td class="ae-details">
  0.180
  </td>
   
   <td class="ae-details">
  0.569
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.407
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.856
  </td>
   
   <td class="ee-details">
  6.270
  </td>
   
   <td class="ee-details">
  26.662
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.067
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0023.jpg">market_2_0023</a></td>
   
   <td class="ae">
  0.634
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.690
  </td>
   
   <td class="ae-details">
  0.193
  </td>
   
   <td class="ae-details">
  0.409
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.238
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.725
  </td>
   
   <td class="ee-details">
  6.140
  </td>
   
   <td class="ee-details">
  26.083
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0024.jpg">market_2_0024</a></td>
   
   <td class="ae">
  0.635
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.650
  </td>
   
   <td class="ae-details">
  0.532
  </td>
   
   <td class="ae-details">
  0.551
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.817
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.620
  </td>
   
   <td class="ee-details">
  11.756
  </td>
   
   <td class="ee-details">
  30.877
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0025.jpg">market_2_0025</a></td>
   
   <td class="ae">
  0.622
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.634
  </td>
   
   <td class="ae-details">
  0.607
  </td>
   
   <td class="ae-details">
  0.224
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.802
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.176
  </td>
   
   <td class="ee-details">
  11.997
  </td>
   
   <td class="ee-details">
  24.390
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0026.jpg">market_2_0026</a></td>
   
   <td class="ae">
  0.603
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.617
  </td>
   
   <td class="ae-details">
  0.458
  </td>
   
   <td class="ae-details">
  0.749
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.944
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.105
  </td>
   
   <td class="ee-details">
  9.204
  </td>
   
   <td class="ee-details">
  29.708
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0027.jpg">market_2_0027</a></td>
   
   <td class="ae">
  0.608
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.615
  </td>
   
   <td class="ae-details">
  0.522
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.496
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.974
  </td>
   
   <td class="ee-details">
  8.207
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.091
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0028.jpg">market_2_0028</a></td>
   
   <td class="ae">
  0.580
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.597
  </td>
   
   <td class="ae-details">
  0.346
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.232
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.896
  </td>
   
   <td class="ee-details">
  5.739
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0029.jpg">market_2_0029</a></td>
   
   <td class="ae">
  0.543
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.563
  </td>
   
   <td class="ae-details">
  0.273
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.134
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.858
  </td>
   
   <td class="ee-details">
  4.975
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0030.jpg">market_2_0030</a></td>
   
   <td class="ae">
  0.532
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.559
  </td>
   
   <td class="ae-details">
  0.152
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.091
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.932
  </td>
   
   <td class="ee-details">
  3.341
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.082
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0031.jpg">market_2_0031</a></td>
   
   <td class="ae">
  0.537
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.561
  </td>
   
   <td class="ae-details">
  0.192
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.301
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.079
  </td>
   
   <td class="ee-details">
  4.511
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0032.jpg">market_2_0032</a></td>
   
   <td class="ae">
  0.543
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.565
  </td>
   
   <td class="ae-details">
  0.185
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.368
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.184
  </td>
   
   <td class="ee-details">
  4.463
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.104
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0033.jpg">market_2_0033</a></td>
   
   <td class="ae">
  0.543
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.569
  </td>
   
   <td class="ae-details">
  0.132
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.410
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.211
  </td>
   
   <td class="ee-details">
  4.609
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0034.jpg">market_2_0034</a></td>
   
   <td class="ae">
  0.543
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.561
  </td>
   
   <td class="ae-details">
  0.151
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.359
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.131
  </td>
   
   <td class="ee-details">
  6.292
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0035.jpg">market_2_0035</a></td>
   
   <td class="ae">
  0.540
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.544
  </td>
   
   <td class="ae-details">
  0.405
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.267
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.812
  </td>
   
   <td class="ee-details">
  16.444
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.067
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0036.jpg">market_2_0036</a></td>
   
   <td class="ae">
  0.537
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.536
  </td>
   
   <td class="ae-details">
  0.402
  </td>
   
   <td class="ae-details">
  0.740
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.197
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.715
  </td>
   
   <td class="ee-details">
  19.575
  </td>
   
   <td class="ee-details">
  35.603
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0037.jpg">market_2_0037</a></td>
   
   <td class="ae">
  0.539
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.538
  </td>
   
   <td class="ae-details">
  1.304
  </td>
   
   <td class="ae-details">
  1.268
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.735
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.676
  </td>
   
   <td class="ee-details">
  37.272
  </td>
   
   <td class="ee-details">
  43.889
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0038.jpg">market_2_0038</a></td>
   
   <td class="ae">
  0.528
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.528
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.643
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.643
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0039.jpg">market_2_0039</a></td>
   
   <td class="ae">
  0.536
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.536
  </td>
   
   <td class="ae-details">
  0.497
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.653
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.653
  </td>
   
   <td class="ee-details">
  8.420
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0040.jpg">market_2_0040</a></td>
   
   <td class="ae">
  0.522
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.522
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.639
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.639
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0041.jpg">market_2_0041</a></td>
   
   <td class="ae">
  0.510
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.510
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.630
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.630
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0042.jpg">market_2_0042</a></td>
   
   <td class="ae">
  0.519
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.519
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.660
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.660
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0043.jpg">market_2_0043</a></td>
   
   <td class="ae">
  0.521
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.521
  </td>
   
   <td class="ae-details">
  0.867
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.657
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.657
  </td>
   
   <td class="ee-details">
  9.702
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.107
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0044.jpg">market_2_0044</a></td>
   
   <td class="ae">
  0.510
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.510
  </td>
   
   <td class="ae-details">
  0.795
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.650
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.650
  </td>
   
   <td class="ee-details">
  9.505
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.114
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0045.jpg">market_2_0045</a></td>
   
   <td class="ae">
  0.515
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.515
  </td>
   
   <td class="ae-details">
  0.468
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.653
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.652
  </td>
   
   <td class="ee-details">
  9.269
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0046.jpg">market_2_0046</a></td>
   
   <td class="ae">
  0.511
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.511
  </td>
   
   <td class="ae-details">
  0.682
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.632
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.632
  </td>
   
   <td class="ee-details">
  9.122
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.063
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0047.jpg">market_2_0047</a></td>
   
   <td class="ae">
  0.528
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.528
  </td>
   
   <td class="ae-details">
  0.439
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.650
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.650
  </td>
   
   <td class="ee-details">
  8.420
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0048.jpg">market_2_0048</a></td>
   
   <td class="ae">
  0.524
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.524
  </td>
   
   <td class="ae-details">
  0.525
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.657
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.657
  </td>
   
   <td class="ee-details">
  8.740
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.109
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_2_0049.jpg">market_2_0049</a></td>
   
   <td class="ae">
  0.526
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.526
  </td>
   
   <td class="ae-details">
  0.395
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.688
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.682
  </td>
   
   <td class="ee-details">
  6.319
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.095
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0001.jpg">market_5_0001</a></td>
   
   <td class="ae">
  0.624
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.754
  </td>
   
   <td class="ae-details">
  0.349
  </td>
   
   <td class="ae-details">
  0.871
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  30.604
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  11.153
  </td>
   
   <td class="ee-details">
  11.484
  </td>
   
   <td class="ee-details">
  57.821
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0002.jpg">market_5_0002</a></td>
   
   <td class="ae">
  0.432
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.749
  </td>
   
   <td class="ae-details">
  0.335
  </td>
   
   <td class="ae-details">
  0.506
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  21.088
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  7.906
  </td>
   
   <td class="ee-details">
  11.483
  </td>
   
   <td class="ee-details">
  50.856
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0003.jpg">market_5_0003</a></td>
   
   <td class="ae">
  0.645
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.757
  </td>
   
   <td class="ae-details">
  0.385
  </td>
   
   <td class="ae-details">
  0.986
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  28.095
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  8.440
  </td>
   
   <td class="ee-details">
  11.816
  </td>
   
   <td class="ee-details">
  59.279
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0004.jpg">market_5_0004</a></td>
   
   <td class="ae">
  0.855
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.625
  </td>
   
   <td class="ae-details">
  0.550
  </td>
   
   <td class="ae-details">
  1.162
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  38.713
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  6.881
  </td>
   
   <td class="ee-details">
  13.408
  </td>
   
   <td class="ee-details">
  68.247
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0005.jpg">market_5_0005</a></td>
   
   <td class="ae">
  0.757
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.537
  </td>
   
   <td class="ae-details">
  0.372
  </td>
   
   <td class="ae-details">
  1.040
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  48.892
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.643
  </td>
   
   <td class="ee-details">
  10.094
  </td>
   
   <td class="ee-details">
  83.607
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0006.jpg">market_5_0006</a></td>
   
   <td class="ae">
  0.590
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.575
  </td>
   
   <td class="ae-details">
  0.485
  </td>
   
   <td class="ae-details">
  0.659
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  47.731
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  7.316
  </td>
   
   <td class="ee-details">
  13.120
  </td>
   
   <td class="ee-details">
  85.234
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0007.jpg">market_5_0007</a></td>
   
   <td class="ae">
  0.714
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.602
  </td>
   
   <td class="ae-details">
  0.634
  </td>
   
   <td class="ae-details">
  0.956
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  22.044
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.556
  </td>
   
   <td class="ee-details">
  15.784
  </td>
   
   <td class="ee-details">
  51.331
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.082
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0008.jpg">market_5_0008</a></td>
   
   <td class="ae">
  0.556
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.505
  </td>
   
   <td class="ae-details">
  0.317
  </td>
   
   <td class="ae-details">
  0.789
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  23.387
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.207
  </td>
   
   <td class="ee-details">
  8.789
  </td>
   
   <td class="ee-details">
  50.638
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.081
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0009.jpg">market_5_0009</a></td>
   
   <td class="ae">
  0.639
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.825
  </td>
   
   <td class="ae-details">
  0.559
  </td>
   
   <td class="ae-details">
  0.586
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  45.422
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  5.786
  </td>
   
   <td class="ee-details">
  12.461
  </td>
   
   <td class="ee-details">
  93.793
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0010.jpg">market_5_0010</a></td>
   
   <td class="ae">
  0.688
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.428
  </td>
   
   <td class="ae-details">
  0.535
  </td>
   
   <td class="ae-details">
  0.895
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  41.055
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.663
  </td>
   
   <td class="ee-details">
  14.486
  </td>
   
   <td class="ee-details">
  73.218
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0011.jpg">market_5_0011</a></td>
   
   <td class="ae">
  1.172
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.375
  </td>
   
   <td class="ae-details">
  1.322
  </td>
   
   <td class="ae-details">
  1.423
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  39.508
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.611
  </td>
   
   <td class="ee-details">
  28.941
  </td>
   
   <td class="ee-details">
  59.753
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0012.jpg">market_5_0012</a></td>
   
   <td class="ae">
  0.857
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.294
  </td>
   
   <td class="ae-details">
  0.707
  </td>
   
   <td class="ae-details">
  1.129
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  47.544
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.915
  </td>
   
   <td class="ee-details">
  18.572
  </td>
   
   <td class="ee-details">
  76.223
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0013.jpg">market_5_0013</a></td>
   
   <td class="ae">
  0.806
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.323
  </td>
   
   <td class="ae-details">
  0.423
  </td>
   
   <td class="ae-details">
  1.138
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  55.535
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.888
  </td>
   
   <td class="ee-details">
  9.378
  </td>
   
   <td class="ee-details">
  94.026
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0014.jpg">market_5_0014</a></td>
   
   <td class="ae">
  0.659
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.331
  </td>
   
   <td class="ae-details">
  0.239
  </td>
   
   <td class="ae-details">
  0.986
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  60.073
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.423
  </td>
   
   <td class="ee-details">
  5.571
  </td>
   
   <td class="ee-details">
  105.645
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.119
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0015.jpg">market_5_0015</a></td>
   
   <td class="ae">
  0.527
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.249
  </td>
   
   <td class="ae-details">
  0.316
  </td>
   
   <td class="ae-details">
  0.766
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  41.164
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.208
  </td>
   
   <td class="ee-details">
  7.127
  </td>
   
   <td class="ee-details">
  78.713
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.092
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0016.jpg">market_5_0016</a></td>
   
   <td class="ae">
  0.426
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.247
  </td>
   
   <td class="ae-details">
  0.314
  </td>
   
   <td class="ae-details">
  0.746
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  20.869
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.089
  </td>
   
   <td class="ee-details">
  8.685
  </td>
   
   <td class="ee-details">
  55.626
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0017.jpg">market_5_0017</a></td>
   
   <td class="ae">
  0.497
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.279
  </td>
   
   <td class="ae-details">
  0.326
  </td>
   
   <td class="ae-details">
  0.738
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  26.600
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.285
  </td>
   
   <td class="ee-details">
  7.403
  </td>
   
   <td class="ee-details">
  53.559
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0018.jpg">market_5_0018</a></td>
   
   <td class="ae">
  0.757
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.382
  </td>
   
   <td class="ae-details">
  0.383
  </td>
   
   <td class="ae-details">
  1.257
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  58.308
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.630
  </td>
   
   <td class="ee-details">
  10.128
  </td>
   
   <td class="ee-details">
  123.478
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0019.jpg">market_5_0019</a></td>
   
   <td class="ae">
  0.735
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.472
  </td>
   
   <td class="ae-details">
  0.320
  </td>
   
   <td class="ae-details">
  1.227
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  48.414
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.076
  </td>
   
   <td class="ee-details">
  8.627
  </td>
   
   <td class="ee-details">
  97.172
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.083
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0020.jpg">market_5_0020</a></td>
   
   <td class="ae">
  0.900
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.089
  </td>
   
   <td class="ae-details">
  0.546
  </td>
   
   <td class="ae-details">
  1.411
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  54.097
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  9.598
  </td>
   
   <td class="ee-details">
  13.367
  </td>
   
   <td class="ee-details">
  116.743
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0021.jpg">market_5_0021</a></td>
   
   <td class="ae">
  0.691
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.546
  </td>
   
   <td class="ae-details">
  0.314
  </td>
   
   <td class="ae-details">
  1.104
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  46.001
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.287
  </td>
   
   <td class="ee-details">
  9.030
  </td>
   
   <td class="ee-details">
  87.867
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0022.jpg">market_5_0022</a></td>
   
   <td class="ae">
  0.708
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.093
  </td>
   
   <td class="ae-details">
  0.369
  </td>
   
   <td class="ae-details">
  1.081
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  41.694
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  5.594
  </td>
   
   <td class="ee-details">
  9.735
  </td>
   
   <td class="ee-details">
  83.212
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0023.jpg">market_5_0023</a></td>
   
   <td class="ae">
  0.430
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.526
  </td>
   
   <td class="ae-details">
  0.276
  </td>
   
   <td class="ae-details">
  0.624
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  45.669
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.040
  </td>
   
   <td class="ee-details">
  9.253
  </td>
   
   <td class="ee-details">
  94.987
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0024.jpg">market_5_0024</a></td>
   
   <td class="ae">
  0.460
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.362
  </td>
   
   <td class="ae-details">
  0.344
  </td>
   
   <td class="ae-details">
  0.638
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  27.232
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  11.519
  </td>
   
   <td class="ee-details">
  10.246
  </td>
   
   <td class="ee-details">
  58.482
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.085
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0025.jpg">market_5_0025</a></td>
   
   <td class="ae">
  0.657
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.487
  </td>
   
   <td class="ae-details">
  0.404
  </td>
   
   <td class="ae-details">
  1.107
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  25.466
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  15.637
  </td>
   
   <td class="ee-details">
  11.868
  </td>
   
   <td class="ee-details">
  50.067
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0026.jpg">market_5_0026</a></td>
   
   <td class="ae">
  0.670
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.378
  </td>
   
   <td class="ae-details">
  0.376
  </td>
   
   <td class="ae-details">
  1.158
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  24.103
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.932
  </td>
   
   <td class="ee-details">
  10.538
  </td>
   
   <td class="ee-details">
  46.761
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0027.jpg">market_5_0027</a></td>
   
   <td class="ae">
  0.518
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.023
  </td>
   
   <td class="ae-details">
  0.271
  </td>
   
   <td class="ae-details">
  0.984
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  23.513
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  9.132
  </td>
   
   <td class="ee-details">
  9.440
  </td>
   
   <td class="ee-details">
  50.341
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0028.jpg">market_5_0028</a></td>
   
   <td class="ae">
  0.389
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.591
  </td>
   
   <td class="ae-details">
  0.239
  </td>
   
   <td class="ae-details">
  0.746
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  20.098
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  5.081
  </td>
   
   <td class="ee-details">
  9.342
  </td>
   
   <td class="ee-details">
  48.193
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.065
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0029.jpg">market_5_0029</a></td>
   
   <td class="ae">
  0.497
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.889
  </td>
   
   <td class="ae-details">
  0.296
  </td>
   
   <td class="ae-details">
  1.011
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  33.244
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.944
  </td>
   
   <td class="ee-details">
  10.319
  </td>
   
   <td class="ee-details">
  96.406
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.089
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0030.jpg">market_5_0030</a></td>
   
   <td class="ae">
  0.394
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.279
  </td>
   
   <td class="ae-details">
  0.297
  </td>
   
   <td class="ae-details">
  0.672
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  21.254
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  9.612
  </td>
   
   <td class="ee-details">
  9.939
  </td>
   
   <td class="ee-details">
  56.542
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.092
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0031.jpg">market_5_0031</a></td>
   
   <td class="ae">
  0.398
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.724
  </td>
   
   <td class="ae-details">
  0.359
  </td>
   
   <td class="ae-details">
  0.546
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  21.169
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  8.283
  </td>
   
   <td class="ee-details">
  11.616
  </td>
   
   <td class="ee-details">
  60.628
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0032.jpg">market_5_0032</a></td>
   
   <td class="ae">
  0.330
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.439
  </td>
   
   <td class="ae-details">
  0.304
  </td>
   
   <td class="ae-details">
  0.456
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  12.549
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  7.703
  </td>
   
   <td class="ee-details">
  9.855
  </td>
   
   <td class="ee-details">
  27.126
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0033.jpg">market_5_0033</a></td>
   
   <td class="ae">
  0.324
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.506
  </td>
   
   <td class="ae-details">
  0.335
  </td>
   
   <td class="ae-details">
  0.249
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  11.140
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  5.536
  </td>
   
   <td class="ee-details">
  9.553
  </td>
   
   <td class="ee-details">
  21.117
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.082
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0034.jpg">market_5_0034</a></td>
   
   <td class="ae">
  0.295
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  2.284
  </td>
   
   <td class="ae-details">
  0.287
  </td>
   
   <td class="ae-details">
  0.333
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  10.768
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  21.273
  </td>
   
   <td class="ee-details">
  8.538
  </td>
   
   <td class="ee-details">
  28.217
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.115
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0035.jpg">market_5_0035</a></td>
   
   <td class="ae">
  0.352
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  2.415
  </td>
   
   <td class="ae-details">
  0.299
  </td>
   
   <td class="ae-details">
  0.765
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  11.666
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  16.767
  </td>
   
   <td class="ee-details">
  8.721
  </td>
   
   <td class="ee-details">
  37.188
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.104
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0036.jpg">market_5_0036</a></td>
   
   <td class="ae">
  0.414
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.686
  </td>
   
   <td class="ae-details">
  0.345
  </td>
   
   <td class="ae-details">
  1.023
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  11.885
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  5.405
  </td>
   
   <td class="ee-details">
  8.813
  </td>
   
   <td class="ee-details">
  40.136
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.084
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0037.jpg">market_5_0037</a></td>
   
   <td class="ae">
  0.386
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.645
  </td>
   
   <td class="ae-details">
  0.341
  </td>
   
   <td class="ae-details">
  0.716
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  11.829
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  7.573
  </td>
   
   <td class="ee-details">
  8.769
  </td>
   
   <td class="ee-details">
  36.333
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0038.jpg">market_5_0038</a></td>
   
   <td class="ae">
  0.411
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.542
  </td>
   
   <td class="ae-details">
  0.358
  </td>
   
   <td class="ae-details">
  0.864
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  12.399
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  6.154
  </td>
   
   <td class="ee-details">
  9.711
  </td>
   
   <td class="ee-details">
  35.795
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0039.jpg">market_5_0039</a></td>
   
   <td class="ae">
  0.388
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.341
  </td>
   
   <td class="ae-details">
  0.809
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  12.213
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  9.679
  </td>
   
   <td class="ee-details">
  34.921
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0040.jpg">market_5_0040</a></td>
   
   <td class="ae">
  0.384
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.373
  </td>
   
   <td class="ae-details">
  0.483
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  11.238
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  9.683
  </td>
   
   <td class="ee-details">
  25.876
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0041.jpg">market_5_0041</a></td>
   
   <td class="ae">
  0.381
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.688
  </td>
   
   <td class="ae-details">
  0.384
  </td>
   
   <td class="ae-details">
  0.356
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  11.689
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  6.572
  </td>
   
   <td class="ee-details">
  10.299
  </td>
   
   <td class="ee-details">
  23.692
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0042.jpg">market_5_0042</a></td>
   
   <td class="ae">
  0.458
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.233
  </td>
   
   <td class="ae-details">
  0.407
  </td>
   
   <td class="ae-details">
  2.237
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  9.872
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.870
  </td>
   
   <td class="ee-details">
  8.502
  </td>
   
   <td class="ee-details">
  61.389
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0043.jpg">market_5_0043</a></td>
   
   <td class="ae">
  0.469
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.209
  </td>
   
   <td class="ae-details">
  0.310
  </td>
   
   <td class="ae-details">
  2.481
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  12.468
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.852
  </td>
   
   <td class="ee-details">
  8.169
  </td>
   
   <td class="ee-details">
  72.281
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0044.jpg">market_5_0044</a></td>
   
   <td class="ae">
  0.473
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.248
  </td>
   
   <td class="ae-details">
  0.411
  </td>
   
   <td class="ae-details">
  1.287
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  15.483
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.152
  </td>
   
   <td class="ee-details">
  8.637
  </td>
   
   <td class="ee-details">
  82.484
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0045.jpg">market_5_0045</a></td>
   
   <td class="ae">
  0.461
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.129
  </td>
   
   <td class="ae-details">
  0.259
  </td>
   
   <td class="ae-details">
  2.316
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  16.713
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.368
  </td>
   
   <td class="ee-details">
  8.307
  </td>
   
   <td class="ee-details">
  95.019
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.082
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0046.jpg">market_5_0046</a></td>
   
   <td class="ae">
  0.550
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.184
  </td>
   
   <td class="ae-details">
  0.449
  </td>
   
   <td class="ae-details">
  1.877
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  17.668
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.696
  </td>
   
   <td class="ee-details">
  12.982
  </td>
   
   <td class="ee-details">
  74.470
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0047.jpg">market_5_0047</a></td>
   
   <td class="ae">
  0.727
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.226
  </td>
   
   <td class="ae-details">
  0.611
  </td>
   
   <td class="ae-details">
  2.220
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  20.696
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.992
  </td>
   
   <td class="ee-details">
  12.468
  </td>
   
   <td class="ee-details">
  89.362
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.081
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0048.jpg">market_5_0048</a></td>
   
   <td class="ae">
  0.754
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.155
  </td>
   
   <td class="ae-details">
  0.703
  </td>
   
   <td class="ae-details">
  2.205
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  27.834
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.254
  </td>
   
   <td class="ee-details">
  14.334
  </td>
   
   <td class="ee-details">
  125.368
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_5_0049.jpg">market_5_0049</a></td>
   
   <td class="ae">
  0.587
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.130
  </td>
   
   <td class="ae-details">
  0.331
  </td>
   
   <td class="ae-details">
  2.218
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  23.285
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.023
  </td>
   
   <td class="ee-details">
  9.877
  </td>
   
   <td class="ee-details">
  102.879
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.130
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0001.jpg">market_6_0001</a></td>
   
   <td class="ae">
  0.695
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.450
  </td>
   
   <td class="ae-details">
  0.539
  </td>
   
   <td class="ae-details">
  1.513
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  18.085
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.906
  </td>
   
   <td class="ee-details">
  13.978
  </td>
   
   <td class="ee-details">
  62.454
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.106
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0002.jpg">market_6_0002</a></td>
   
   <td class="ae">
  0.537
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.469
  </td>
   
   <td class="ae-details">
  0.448
  </td>
   
   <td class="ae-details">
  0.837
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  17.952
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.324
  </td>
   
   <td class="ee-details">
  13.050
  </td>
   
   <td class="ee-details">
  60.925
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0003.jpg">market_6_0003</a></td>
   
   <td class="ae">
  0.586
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.405
  </td>
   
   <td class="ae-details">
  0.507
  </td>
   
   <td class="ae-details">
  1.093
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  20.375
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.204
  </td>
   
   <td class="ee-details">
  12.818
  </td>
   
   <td class="ee-details">
  70.595
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0004.jpg">market_6_0004</a></td>
   
   <td class="ae">
  0.384
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.399
  </td>
   
   <td class="ae-details">
  0.299
  </td>
   
   <td class="ae-details">
  0.506
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  20.019
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.191
  </td>
   
   <td class="ee-details">
  10.365
  </td>
   
   <td class="ee-details">
  72.113
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0005.jpg">market_6_0005</a></td>
   
   <td class="ae">
  0.542
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.449
  </td>
   
   <td class="ae-details">
  0.312
  </td>
   
   <td class="ae-details">
  1.092
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  23.424
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.815
  </td>
   
   <td class="ee-details">
  10.353
  </td>
   
   <td class="ee-details">
  81.663
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0006.jpg">market_6_0006</a></td>
   
   <td class="ae">
  0.453
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.359
  </td>
   
   <td class="ae-details">
  0.228
  </td>
   
   <td class="ae-details">
  1.000
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  23.939
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.539
  </td>
   
   <td class="ee-details">
  8.922
  </td>
   
   <td class="ee-details">
  83.118
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0007.jpg">market_6_0007</a></td>
   
   <td class="ae">
  0.394
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.415
  </td>
   
   <td class="ae-details">
  0.207
  </td>
   
   <td class="ae-details">
  0.730
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  23.019
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.328
  </td>
   
   <td class="ee-details">
  8.016
  </td>
   
   <td class="ee-details">
  78.824
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0008.jpg">market_6_0008</a></td>
   
   <td class="ae">
  0.427
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.433
  </td>
   
   <td class="ae-details">
  0.181
  </td>
   
   <td class="ae-details">
  0.937
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  23.487
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.116
  </td>
   
   <td class="ee-details">
  7.857
  </td>
   
   <td class="ee-details">
  81.322
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0009.jpg">market_6_0009</a></td>
   
   <td class="ae">
  0.365
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.479
  </td>
   
   <td class="ae-details">
  0.228
  </td>
   
   <td class="ae-details">
  0.698
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  21.041
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.669
  </td>
   
   <td class="ee-details">
  6.818
  </td>
   
   <td class="ee-details">
  75.253
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0010.jpg">market_6_0010</a></td>
   
   <td class="ae">
  0.346
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.254
  </td>
   
   <td class="ae-details">
  0.276
  </td>
   
   <td class="ae-details">
  0.631
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  19.443
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.217
  </td>
   
   <td class="ee-details">
  7.369
  </td>
   
   <td class="ee-details">
  69.100
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0011.jpg">market_6_0011</a></td>
   
   <td class="ae">
  0.367
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.264
  </td>
   
   <td class="ae-details">
  0.287
  </td>
   
   <td class="ae-details">
  0.657
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  17.698
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.744
  </td>
   
   <td class="ee-details">
  7.716
  </td>
   
   <td class="ee-details">
  54.018
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0012.jpg">market_6_0012</a></td>
   
   <td class="ae">
  0.377
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.256
  </td>
   
   <td class="ae-details">
  0.238
  </td>
   
   <td class="ae-details">
  0.798
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  17.751
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.825
  </td>
   
   <td class="ee-details">
  7.527
  </td>
   
   <td class="ee-details">
  49.090
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0013.jpg">market_6_0013</a></td>
   
   <td class="ae">
  0.370
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.463
  </td>
   
   <td class="ae-details">
  0.206
  </td>
   
   <td class="ae-details">
  0.905
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  15.823
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.167
  </td>
   
   <td class="ee-details">
  6.337
  </td>
   
   <td class="ee-details">
  47.758
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0014.jpg">market_6_0014</a></td>
   
   <td class="ae">
  0.255
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.539
  </td>
   
   <td class="ae-details">
  0.203
  </td>
   
   <td class="ae-details">
  0.493
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  12.618
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  5.667
  </td>
   
   <td class="ee-details">
  6.226
  </td>
   
   <td class="ee-details">
  44.261
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0015.jpg">market_6_0015</a></td>
   
   <td class="ae">
  0.265
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.610
  </td>
   
   <td class="ae-details">
  0.200
  </td>
   
   <td class="ae-details">
  0.862
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  11.375
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  5.915
  </td>
   
   <td class="ee-details">
  6.616
  </td>
   
   <td class="ee-details">
  57.275
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.083
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0016.jpg">market_6_0016</a></td>
   
   <td class="ae">
  0.223
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.770
  </td>
   
   <td class="ae-details">
  0.208
  </td>
   
   <td class="ae-details">
  0.621
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  7.615
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  6.121
  </td>
   
   <td class="ee-details">
  6.659
  </td>
   
   <td class="ee-details">
  40.382
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.139
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0017.jpg">market_6_0017</a></td>
   
   <td class="ae">
  0.266
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.329
  </td>
   
   <td class="ae-details">
  0.250
  </td>
   
   <td class="ae-details">
  1.009
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  7.947
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.431
  </td>
   
   <td class="ee-details">
  7.396
  </td>
   
   <td class="ee-details">
  36.986
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.101
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0018.jpg">market_6_0018</a></td>
   
   <td class="ae">
  0.264
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.294
  </td>
   
   <td class="ae-details">
  0.248
  </td>
   
   <td class="ae-details">
  1.157
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  7.446
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.431
  </td>
   
   <td class="ee-details">
  6.935
  </td>
   
   <td class="ee-details">
  39.491
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0019.jpg">market_6_0019</a></td>
   
   <td class="ae">
  0.250
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.150
  </td>
   
   <td class="ae-details">
  0.243
  </td>
   
   <td class="ae-details">
  0.975
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  7.047
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.590
  </td>
   
   <td class="ee-details">
  6.759
  </td>
   
   <td class="ee-details">
  38.167
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0020.jpg">market_6_0020</a></td>
   
   <td class="ae">
  0.214
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.149
  </td>
   
   <td class="ae-details">
  0.215
  </td>
   
   <td class="ae-details">
  0.544
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  6.101
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.969
  </td>
   
   <td class="ee-details">
  6.086
  </td>
   
   <td class="ee-details">
  27.536
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0021.jpg">market_6_0021</a></td>
   
   <td class="ae">
  0.229
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.178
  </td>
   
   <td class="ae-details">
  0.232
  </td>
   
   <td class="ae-details">
  0.680
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.956
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.311
  </td>
   
   <td class="ee-details">
  6.121
  </td>
   
   <td class="ee-details">
  30.260
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0022.jpg">market_6_0022</a></td>
   
   <td class="ae">
  0.205
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.121
  </td>
   
   <td class="ae-details">
  0.217
  </td>
   
   <td class="ae-details">
  1.985
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.288
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.925
  </td>
   
   <td class="ee-details">
  5.617
  </td>
   
   <td class="ee-details">
  46.847
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0023.jpg">market_6_0023</a></td>
   
   <td class="ae">
  0.209
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.221
  </td>
   
   <td class="ae-details">
  0.206
  </td>
   
   <td class="ae-details">
  0.402
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.804
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.921
  </td>
   
   <td class="ee-details">
  5.316
  </td>
   
   <td class="ee-details">
  45.106
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0024.jpg">market_6_0024</a></td>
   
   <td class="ae">
  0.213
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.203
  </td>
   
   <td class="ae-details">
  0.218
  </td>
   
   <td class="ae-details">
  0.336
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.687
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.541
  </td>
   
   <td class="ee-details">
  5.779
  </td>
   
   <td class="ee-details">
  44.760
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.141
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0025.jpg">market_6_0025</a></td>
   
   <td class="ae">
  0.247
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.274
  </td>
   
   <td class="ae-details">
  0.201
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.505
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.169
  </td>
   
   <td class="ee-details">
  6.737
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.108
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0026.jpg">market_6_0026</a></td>
   
   <td class="ae">
  0.341
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.362
  </td>
   
   <td class="ae-details">
  0.213
  </td>
   
   <td class="ae-details">
  1.614
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  7.322
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.400
  </td>
   
   <td class="ee-details">
  7.669
  </td>
   
   <td class="ee-details">
  155.787
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0027.jpg">market_6_0027</a></td>
   
   <td class="ae">
  0.331
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.334
  </td>
   
   <td class="ae-details">
  0.172
  </td>
   
   <td class="ae-details">
  2.091
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.609
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.762
  </td>
   
   <td class="ee-details">
  6.779
  </td>
   
   <td class="ee-details">
  73.764
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0028.jpg">market_6_0028</a></td>
   
   <td class="ae">
  0.426
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.454
  </td>
   
   <td class="ae-details">
  0.245
  </td>
   
   <td class="ae-details">
  1.542
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  7.231
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.122
  </td>
   
   <td class="ee-details">
  8.373
  </td>
   
   <td class="ee-details">
  83.574
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0029.jpg">market_6_0029</a></td>
   
   <td class="ae">
  0.549
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.545
  </td>
   
   <td class="ae-details">
  0.326
  </td>
   
   <td class="ae-details">
  1.583
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  10.797
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.801
  </td>
   
   <td class="ee-details">
  9.694
  </td>
   
   <td class="ee-details">
  79.425
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0030.jpg">market_6_0030</a></td>
   
   <td class="ae">
  0.557
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.382
  </td>
   
   <td class="ae-details">
  0.290
  </td>
   
   <td class="ae-details">
  2.317
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  12.445
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.094
  </td>
   
   <td class="ee-details">
  8.387
  </td>
   
   <td class="ee-details">
  73.814
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0031.jpg">market_6_0031</a></td>
   
   <td class="ae">
  0.501
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.373
  </td>
   
   <td class="ae-details">
  0.346
  </td>
   
   <td class="ae-details">
  1.764
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  10.612
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.022
  </td>
   
   <td class="ee-details">
  9.759
  </td>
   
   <td class="ee-details">
  54.995
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0032.jpg">market_6_0032</a></td>
   
   <td class="ae">
  0.446
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.468
  </td>
   
   <td class="ae-details">
  0.244
  </td>
   
   <td class="ae-details">
  1.151
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  9.810
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.085
  </td>
   
   <td class="ee-details">
  8.064
  </td>
   
   <td class="ee-details">
  54.230
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.117
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0033.jpg">market_6_0033</a></td>
   
   <td class="ae">
  0.453
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.505
  </td>
   
   <td class="ae-details">
  0.328
  </td>
   
   <td class="ae-details">
  0.684
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  8.990
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.205
  </td>
   
   <td class="ee-details">
  9.285
  </td>
   
   <td class="ee-details">
  46.869
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.098
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0034.jpg">market_6_0034</a></td>
   
   <td class="ae">
  0.389
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.399
  </td>
   
   <td class="ae-details">
  0.316
  </td>
   
   <td class="ae-details">
  0.952
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  7.048
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.296
  </td>
   
   <td class="ee-details">
  9.708
  </td>
   
   <td class="ee-details">
  52.982
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.065
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0035.jpg">market_6_0035</a></td>
   
   <td class="ae">
  0.400
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.423
  </td>
   
   <td class="ae-details">
  0.352
  </td>
   
   <td class="ae-details">
  0.963
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.857
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.425
  </td>
   
   <td class="ee-details">
  10.177
  </td>
   
   <td class="ee-details">
  36.940
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0036.jpg">market_6_0036</a></td>
   
   <td class="ae">
  0.388
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.394
  </td>
   
   <td class="ae-details">
  0.375
  </td>
   
   <td class="ae-details">
  0.658
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.245
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.671
  </td>
   
   <td class="ee-details">
  9.686
  </td>
   
   <td class="ee-details">
  66.141
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0037.jpg">market_6_0037</a></td>
   
   <td class="ae">
  0.394
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.377
  </td>
   
   <td class="ae-details">
  0.406
  </td>
   
   <td class="ae-details">
  1.113
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.466
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.531
  </td>
   
   <td class="ee-details">
  10.379
  </td>
   
   <td class="ee-details">
  83.028
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0038.jpg">market_6_0038</a></td>
   
   <td class="ae">
  0.378
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.363
  </td>
   
   <td class="ae-details">
  0.409
  </td>
   
   <td class="ae-details">
  0.354
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.962
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.409
  </td>
   
   <td class="ee-details">
  11.505
  </td>
   
   <td class="ee-details">
  36.698
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/market_6_0039.jpg">market_6_0039</a></td>
   
   <td class="ae">
  0.380
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.410
  </td>
   
   <td class="ae-details">
  0.321
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.295
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.276
  </td>
   
   <td class="ee-details">
  10.410
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0001.jpg">mountain_1_0001</a></td>
   
   <td class="ae">
  0.319
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.342
  </td>
   
   <td class="ae-details">
  0.165
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.863
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.684
  </td>
   
   <td class="ee-details">
  3.055
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.065
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0002.jpg">mountain_1_0002</a></td>
   
   <td class="ae">
  0.309
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.331
  </td>
   
   <td class="ae-details">
  0.170
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.837
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.641
  </td>
   
   <td class="ee-details">
  3.106
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0003.jpg">mountain_1_0003</a></td>
   
   <td class="ae">
  0.306
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.325
  </td>
   
   <td class="ae-details">
  0.189
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.849
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.592
  </td>
   
   <td class="ee-details">
  3.453
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0004.jpg">mountain_1_0004</a></td>
   
   <td class="ae">
  0.288
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.304
  </td>
   
   <td class="ae-details">
  0.191
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.828
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.569
  </td>
   
   <td class="ee-details">
  3.420
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.087
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0005.jpg">mountain_1_0005</a></td>
   
   <td class="ae">
  0.307
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.324
  </td>
   
   <td class="ae-details">
  0.208
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.928
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.639
  </td>
   
   <td class="ee-details">
  3.690
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.081
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0006.jpg">mountain_1_0006</a></td>
   
   <td class="ae">
  0.299
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.313
  </td>
   
   <td class="ae-details">
  0.213
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.953
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.614
  </td>
   
   <td class="ee-details">
  4.004
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.084
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0007.jpg">mountain_1_0007</a></td>
   
   <td class="ae">
  0.301
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.315
  </td>
   
   <td class="ae-details">
  0.221
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.087
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.682
  </td>
   
   <td class="ee-details">
  4.541
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.083
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0008.jpg">mountain_1_0008</a></td>
   
   <td class="ae">
  0.296
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.301
  </td>
   
   <td class="ae-details">
  0.266
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.262
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.620
  </td>
   
   <td class="ee-details">
  6.131
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.067
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0009.jpg">mountain_1_0009</a></td>
   
   <td class="ae">
  0.310
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.319
  </td>
   
   <td class="ae-details">
  0.256
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.420
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.671
  </td>
   
   <td class="ee-details">
  6.908
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.121
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0010.jpg">mountain_1_0010</a></td>
   
   <td class="ae">
  0.315
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.329
  </td>
   
   <td class="ae-details">
  0.230
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.435
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.704
  </td>
   
   <td class="ee-details">
  6.808
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.103
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0011.jpg">mountain_1_0011</a></td>
   
   <td class="ae">
  0.311
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.316
  </td>
   
   <td class="ae-details">
  0.278
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.514
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.638
  </td>
   
   <td class="ee-details">
  7.754
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0012.jpg">mountain_1_0012</a></td>
   
   <td class="ae">
  0.289
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.304
  </td>
   
   <td class="ae-details">
  0.197
  </td>
   
   <td class="ae-details">
  0.394
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.296
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.681
  </td>
   
   <td class="ee-details">
  5.974
  </td>
   
   <td class="ee-details">
  28.384
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0013.jpg">mountain_1_0013</a></td>
   
   <td class="ae">
  0.305
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.322
  </td>
   
   <td class="ae-details">
  0.203
  </td>
   
   <td class="ae-details">
  0.663
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.281
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.760
  </td>
   
   <td class="ee-details">
  5.395
  </td>
   
   <td class="ee-details">
  27.108
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0014.jpg">mountain_1_0014</a></td>
   
   <td class="ae">
  0.292
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.312
  </td>
   
   <td class="ae-details">
  0.169
  </td>
   
   <td class="ae-details">
  0.462
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.113
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.701
  </td>
   
   <td class="ee-details">
  4.582
  </td>
   
   <td class="ee-details">
  20.383
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0015.jpg">mountain_1_0015</a></td>
   
   <td class="ae">
  0.316
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.343
  </td>
   
   <td class="ae-details">
  0.157
  </td>
   
   <td class="ae-details">
  0.334
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.169
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.760
  </td>
   
   <td class="ee-details">
  4.642
  </td>
   
   <td class="ee-details">
  24.620
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0016.jpg">mountain_1_0016</a></td>
   
   <td class="ae">
  0.327
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.348
  </td>
   
   <td class="ae-details">
  0.199
  </td>
   
   <td class="ae-details">
  0.363
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.399
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.955
  </td>
   
   <td class="ee-details">
  5.107
  </td>
   
   <td class="ee-details">
  21.316
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0017.jpg">mountain_1_0017</a></td>
   
   <td class="ae">
  0.318
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.334
  </td>
   
   <td class="ae-details">
  0.216
  </td>
   
   <td class="ae-details">
  0.514
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.318
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.765
  </td>
   
   <td class="ee-details">
  5.834
  </td>
   
   <td class="ee-details">
  25.665
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0018.jpg">mountain_1_0018</a></td>
   
   <td class="ae">
  0.346
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.347
  </td>
   
   <td class="ae-details">
  0.339
  </td>
   
   <td class="ae-details">
  1.139
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.828
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.757
  </td>
   
   <td class="ee-details">
  9.712
  </td>
   
   <td class="ee-details">
  39.381
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0019.jpg">mountain_1_0019</a></td>
   
   <td class="ae">
  0.329
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.326
  </td>
   
   <td class="ae-details">
  0.347
  </td>
   
   <td class="ae-details">
  1.639
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.915
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.670
  </td>
   
   <td class="ee-details">
  10.895
  </td>
   
   <td class="ee-details">
  43.252
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0020.jpg">mountain_1_0020</a></td>
   
   <td class="ae">
  0.328
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.324
  </td>
   
   <td class="ae-details">
  0.338
  </td>
   
   <td class="ae-details">
  1.725
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.181
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.628
  </td>
   
   <td class="ee-details">
  12.949
  </td>
   
   <td class="ee-details">
  42.526
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0021.jpg">mountain_1_0021</a></td>
   
   <td class="ae">
  0.332
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.343
  </td>
   
   <td class="ae-details">
  0.237
  </td>
   
   <td class="ae-details">
  0.836
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.049
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.722
  </td>
   
   <td class="ee-details">
  11.058
  </td>
   
   <td class="ee-details">
  32.327
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.108
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0022.jpg">mountain_1_0022</a></td>
   
   <td class="ae">
  0.328
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.332
  </td>
   
   <td class="ae-details">
  0.251
  </td>
   
   <td class="ae-details">
  0.704
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.070
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.688
  </td>
   
   <td class="ee-details">
  10.419
  </td>
   
   <td class="ee-details">
  30.477
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.094
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0023.jpg">mountain_1_0023</a></td>
   
   <td class="ae">
  0.323
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.325
  </td>
   
   <td class="ae-details">
  0.277
  </td>
   
   <td class="ae-details">
  0.393
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.468
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.553
  </td>
   
   <td class="ee-details">
  12.956
  </td>
   
   <td class="ee-details">
  35.246
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0024.jpg">mountain_1_0024</a></td>
   
   <td class="ae">
  0.344
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.346
  </td>
   
   <td class="ae-details">
  0.271
  </td>
   
   <td class="ae-details">
  0.435
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.556
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.513
  </td>
   
   <td class="ee-details">
  13.607
  </td>
   
   <td class="ee-details">
  35.684
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0025.jpg">mountain_1_0025</a></td>
   
   <td class="ae">
  0.349
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.330
  </td>
   
   <td class="ae-details">
  0.278
  </td>
   
   <td class="ae-details">
  0.960
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.913
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.456
  </td>
   
   <td class="ee-details">
  14.473
  </td>
   
   <td class="ee-details">
  48.490
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0026.jpg">mountain_1_0026</a></td>
   
   <td class="ae">
  0.309
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.313
  </td>
   
   <td class="ae-details">
  0.190
  </td>
   
   <td class="ae-details">
  0.377
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.510
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.425
  </td>
   
   <td class="ee-details">
  12.017
  </td>
   
   <td class="ee-details">
  47.804
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.083
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0027.jpg">mountain_1_0027</a></td>
   
   <td class="ae">
  0.302
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.309
  </td>
   
   <td class="ae-details">
  0.134
  </td>
   
   <td class="ae-details">
  0.392
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.202
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.387
  </td>
   
   <td class="ee-details">
  8.366
  </td>
   
   <td class="ee-details">
  57.544
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0028.jpg">mountain_1_0028</a></td>
   
   <td class="ae">
  0.309
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.310
  </td>
   
   <td class="ae-details">
  0.140
  </td>
   
   <td class="ae-details">
  1.082
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.635
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.466
  </td>
   
   <td class="ee-details">
  8.031
  </td>
   
   <td class="ee-details">
  65.130
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0029.jpg">mountain_1_0029</a></td>
   
   <td class="ae">
  0.312
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.323
  </td>
   
   <td class="ae-details">
  0.126
  </td>
   
   <td class="ae-details">
  0.429
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.057
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.431
  </td>
   
   <td class="ee-details">
  5.967
  </td>
   
   <td class="ee-details">
  40.607
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.064
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0030.jpg">mountain_1_0030</a></td>
   
   <td class="ae">
  0.296
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.309
  </td>
   
   <td class="ae-details">
  0.103
  </td>
   
   <td class="ae-details">
  0.450
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.697
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.335
  </td>
   
   <td class="ee-details">
  4.002
  </td>
   
   <td class="ee-details">
  41.147
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0031.jpg">mountain_1_0031</a></td>
   
   <td class="ae">
  0.270
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.282
  </td>
   
   <td class="ae-details">
  0.114
  </td>
   
   <td class="ae-details">
  0.350
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.469
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.262
  </td>
   
   <td class="ee-details">
  3.903
  </td>
   
   <td class="ee-details">
  45.512
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0032.jpg">mountain_1_0032</a></td>
   
   <td class="ae">
  0.288
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.302
  </td>
   
   <td class="ae-details">
  0.124
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.545
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.330
  </td>
   
   <td class="ee-details">
  4.057
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.116
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0033.jpg">mountain_1_0033</a></td>
   
   <td class="ae">
  0.304
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.320
  </td>
   
   <td class="ae-details">
  0.125
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.547
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.333
  </td>
   
   <td class="ee-details">
  3.853
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.097
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0034.jpg">mountain_1_0034</a></td>
   
   <td class="ae">
  0.297
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.315
  </td>
   
   <td class="ae-details">
  0.118
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.530
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.279
  </td>
   
   <td class="ee-details">
  3.996
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0035.jpg">mountain_1_0035</a></td>
   
   <td class="ae">
  0.292
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.310
  </td>
   
   <td class="ae-details">
  0.127
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.561
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.305
  </td>
   
   <td class="ee-details">
  3.888
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0036.jpg">mountain_1_0036</a></td>
   
   <td class="ae">
  0.310
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.331
  </td>
   
   <td class="ae-details">
  0.133
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.563
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.293
  </td>
   
   <td class="ee-details">
  3.910
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0037.jpg">mountain_1_0037</a></td>
   
   <td class="ae">
  0.295
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.314
  </td>
   
   <td class="ae-details">
  0.139
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.597
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.298
  </td>
   
   <td class="ee-details">
  4.080
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.121
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0038.jpg">mountain_1_0038</a></td>
   
   <td class="ae">
  0.292
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.312
  </td>
   
   <td class="ae-details">
  0.138
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.585
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.273
  </td>
   
   <td class="ee-details">
  4.107
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.099
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0039.jpg">mountain_1_0039</a></td>
   
   <td class="ae">
  0.296
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.316
  </td>
   
   <td class="ae-details">
  0.139
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.603
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.286
  </td>
   
   <td class="ee-details">
  4.096
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.081
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0040.jpg">mountain_1_0040</a></td>
   
   <td class="ae">
  0.284
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.302
  </td>
   
   <td class="ae-details">
  0.144
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.592
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.229
  </td>
   
   <td class="ee-details">
  4.382
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0041.jpg">mountain_1_0041</a></td>
   
   <td class="ae">
  0.308
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.330
  </td>
   
   <td class="ae-details">
  0.144
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.708
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.358
  </td>
   
   <td class="ee-details">
  4.295
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.067
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0042.jpg">mountain_1_0042</a></td>
   
   <td class="ae">
  0.296
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.319
  </td>
   
   <td class="ae-details">
  0.138
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.675
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.291
  </td>
   
   <td class="ee-details">
  4.413
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0043.jpg">mountain_1_0043</a></td>
   
   <td class="ae">
  0.296
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.319
  </td>
   
   <td class="ae-details">
  0.136
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.667
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.295
  </td>
   
   <td class="ee-details">
  4.231
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.067
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0044.jpg">mountain_1_0044</a></td>
   
   <td class="ae">
  0.317
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.344
  </td>
   
   <td class="ae-details">
  0.141
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.765
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.345
  </td>
   
   <td class="ee-details">
  4.550
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0045.jpg">mountain_1_0045</a></td>
   
   <td class="ae">
  0.318
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.345
  </td>
   
   <td class="ae-details">
  0.147
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.842
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.424
  </td>
   
   <td class="ee-details">
  4.525
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0046.jpg">mountain_1_0046</a></td>
   
   <td class="ae">
  0.296
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.321
  </td>
   
   <td class="ae-details">
  0.142
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.740
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.268
  </td>
   
   <td class="ee-details">
  4.653
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0047.jpg">mountain_1_0047</a></td>
   
   <td class="ae">
  0.298
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.324
  </td>
   
   <td class="ae-details">
  0.143
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.767
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.302
  </td>
   
   <td class="ee-details">
  4.571
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0048.jpg">mountain_1_0048</a></td>
   
   <td class="ae">
  0.320
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.351
  </td>
   
   <td class="ae-details">
  0.135
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.806
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.351
  </td>
   
   <td class="ee-details">
  4.491
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.121
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/mountain_1_0049.jpg">mountain_1_0049</a></td>
   
   <td class="ae">
  0.304
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.333
  </td>
   
   <td class="ae-details">
  0.132
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.864
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.368
  </td>
   
   <td class="ee-details">
  4.713
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.094
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0001.jpg">shaman_2_0001</a></td>
   
   <td class="ae">
  0.358
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.358
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.168
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.168
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.084
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0002.jpg">shaman_2_0002</a></td>
   
   <td class="ae">
  0.385
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.385
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.165
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.165
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0003.jpg">shaman_2_0003</a></td>
   
   <td class="ae">
  0.403
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.403
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.062
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.062
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0004.jpg">shaman_2_0004</a></td>
   
   <td class="ae">
  0.410
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.410
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.926
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.926
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0005.jpg">shaman_2_0005</a></td>
   
   <td class="ae">
  0.377
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.377
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.726
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.726
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0006.jpg">shaman_2_0006</a></td>
   
   <td class="ae">
  0.352
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.352
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.623
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.623
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0007.jpg">shaman_2_0007</a></td>
   
   <td class="ae">
  0.349
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.349
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.590
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.590
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0008.jpg">shaman_2_0008</a></td>
   
   <td class="ae">
  0.371
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.371
  </td>
   
   <td class="ae-details">
  0.218
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.648
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.648
  </td>
   
   <td class="ee-details">
  6.192
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0009.jpg">shaman_2_0009</a></td>
   
   <td class="ae">
  0.384
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.384
  </td>
   
   <td class="ae-details">
  0.377
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.697
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.688
  </td>
   
   <td class="ee-details">
  6.092
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.102
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0010.jpg">shaman_2_0010</a></td>
   
   <td class="ae">
  0.400
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.399
  </td>
   
   <td class="ae-details">
  0.501
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.832
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.772
  </td>
   
   <td class="ee-details">
  8.151
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.096
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0011.jpg">shaman_2_0011</a></td>
   
   <td class="ae">
  0.404
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.404
  </td>
   
   <td class="ae-details">
  1.080
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.721
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.713
  </td>
   
   <td class="ee-details">
  9.806
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0012.jpg">shaman_2_0012</a></td>
   
   <td class="ae">
  0.392
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.392
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.654
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.654
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0013.jpg">shaman_2_0013</a></td>
   
   <td class="ae">
  0.383
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.383
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.661
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.661
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0014.jpg">shaman_2_0014</a></td>
   
   <td class="ae">
  0.360
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.360
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.654
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.654
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.108
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0015.jpg">shaman_2_0015</a></td>
   
   <td class="ae">
  0.358
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.358
  </td>
   
   <td class="ae-details">
  1.537
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.671
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.669
  </td>
   
   <td class="ee-details">
  22.191
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.092
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0016.jpg">shaman_2_0016</a></td>
   
   <td class="ae">
  0.354
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.354
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.712
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.712
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0017.jpg">shaman_2_0017</a></td>
   
   <td class="ae">
  0.358
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.358
  </td>
   
   <td class="ae-details">
  0.153
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.814
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.814
  </td>
   
   <td class="ee-details">
  1.864
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.062
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0018.jpg">shaman_2_0018</a></td>
   
   <td class="ae">
  0.370
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.372
  </td>
   
   <td class="ae-details">
  0.291
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.038
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.962
  </td>
   
   <td class="ee-details">
  3.576
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0019.jpg">shaman_2_0019</a></td>
   
   <td class="ae">
  0.367
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.367
  </td>
   
   <td class="ae-details">
  0.430
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.994
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.990
  </td>
   
   <td class="ee-details">
  4.237
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.089
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0020.jpg">shaman_2_0020</a></td>
   
   <td class="ae">
  0.367
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.367
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.944
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.944
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0021.jpg">shaman_2_0021</a></td>
   
   <td class="ae">
  0.378
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.377
  </td>
   
   <td class="ae-details">
  0.787
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.030
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.013
  </td>
   
   <td class="ee-details">
  7.985
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0022.jpg">shaman_2_0022</a></td>
   
   <td class="ae">
  0.370
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.369
  </td>
   
   <td class="ae-details">
  0.677
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.998
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.985
  </td>
   
   <td class="ee-details">
  6.937
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0023.jpg">shaman_2_0023</a></td>
   
   <td class="ae">
  0.361
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.361
  </td>
   
   <td class="ae-details">
  1.032
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.046
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.041
  </td>
   
   <td class="ee-details">
  16.837
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.086
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0024.jpg">shaman_2_0024</a></td>
   
   <td class="ae">
  0.365
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.365
  </td>
   
   <td class="ae-details">
  0.248
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.058
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.057
  </td>
   
   <td class="ee-details">
  2.665
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.065
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0025.jpg">shaman_2_0025</a></td>
   
   <td class="ae">
  0.365
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.365
  </td>
   
   <td class="ae-details">
  0.305
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.068
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.061
  </td>
   
   <td class="ee-details">
  3.163
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.131
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0026.jpg">shaman_2_0026</a></td>
   
   <td class="ae">
  0.375
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.376
  </td>
   
   <td class="ae-details">
  0.295
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.124
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.085
  </td>
   
   <td class="ee-details">
  3.336
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.101
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0027.jpg">shaman_2_0027</a></td>
   
   <td class="ae">
  0.382
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.384
  </td>
   
   <td class="ae-details">
  0.299
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.204
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.130
  </td>
   
   <td class="ee-details">
  3.908
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0028.jpg">shaman_2_0028</a></td>
   
   <td class="ae">
  0.407
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.407
  </td>
   
   <td class="ae-details">
  0.293
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.221
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.219
  </td>
   
   <td class="ee-details">
  3.055
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.063
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0029.jpg">shaman_2_0029</a></td>
   
   <td class="ae">
  0.398
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.398
  </td>
   
   <td class="ae-details">
  0.049
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.074
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.074
  </td>
   
   <td class="ee-details">
  3.367
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0030.jpg">shaman_2_0030</a></td>
   
   <td class="ae">
  0.423
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.423
  </td>
   
   <td class="ae-details">
  0.173
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.091
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.091
  </td>
   
   <td class="ee-details">
  5.169
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.061
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0031.jpg">shaman_2_0031</a></td>
   
   <td class="ae">
  0.436
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.436
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.114
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.114
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0032.jpg">shaman_2_0032</a></td>
   
   <td class="ae">
  0.454
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.454
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.129
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.129
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0033.jpg">shaman_2_0033</a></td>
   
   <td class="ae">
  0.468
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.468
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.084
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.084
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0034.jpg">shaman_2_0034</a></td>
   
   <td class="ae">
  0.471
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.471
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.984
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.984
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0035.jpg">shaman_2_0035</a></td>
   
   <td class="ae">
  0.446
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.446
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.867
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.867
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.065
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0036.jpg">shaman_2_0036</a></td>
   
   <td class="ae">
  0.437
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.437
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.765
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.765
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.119
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0037.jpg">shaman_2_0037</a></td>
   
   <td class="ae">
  0.443
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.443
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.740
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.740
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.098
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0038.jpg">shaman_2_0038</a></td>
   
   <td class="ae">
  0.429
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.429
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.680
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.680
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.084
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0039.jpg">shaman_2_0039</a></td>
   
   <td class="ae">
  0.425
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.425
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.660
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.660
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0040.jpg">shaman_2_0040</a></td>
   
   <td class="ae">
  0.419
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.419
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.620
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.620
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.063
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0041.jpg">shaman_2_0041</a></td>
   
   <td class="ae">
  0.410
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.410
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.575
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.575
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0042.jpg">shaman_2_0042</a></td>
   
   <td class="ae">
  0.436
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.436
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.591
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.591
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0043.jpg">shaman_2_0043</a></td>
   
   <td class="ae">
  0.436
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.436
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.562
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.562
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0044.jpg">shaman_2_0044</a></td>
   
   <td class="ae">
  0.475
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.475
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.595
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.595
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0045.jpg">shaman_2_0045</a></td>
   
   <td class="ae">
  0.515
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.515
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.647
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.647
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0046.jpg">shaman_2_0046</a></td>
   
   <td class="ae">
  0.502
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.502
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.692
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.692
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0047.jpg">shaman_2_0047</a></td>
   
   <td class="ae">
  0.489
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.489
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.819
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.819
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.084
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0048.jpg">shaman_2_0048</a></td>
   
   <td class="ae">
  0.467
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.467
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.973
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.973
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.084
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_2_0049.jpg">shaman_2_0049</a></td>
   
   <td class="ae">
  0.471
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.471
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.183
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.183
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0001.jpg">shaman_3_0001</a></td>
   
   <td class="ae">
  0.424
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.424
  </td>
   
   <td class="ae-details">
  0.376
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.674
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.634
  </td>
   
   <td class="ee-details">
  6.785
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0002.jpg">shaman_3_0002</a></td>
   
   <td class="ae">
  0.428
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.428
  </td>
   
   <td class="ae-details">
  0.357
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.951
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.903
  </td>
   
   <td class="ee-details">
  6.667
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0003.jpg">shaman_3_0003</a></td>
   
   <td class="ae">
  0.428
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.429
  </td>
   
   <td class="ae-details">
  0.339
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.186
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.129
  </td>
   
   <td class="ee-details">
  6.370
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.081
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0004.jpg">shaman_3_0004</a></td>
   
   <td class="ae">
  0.405
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.408
  </td>
   
   <td class="ae-details">
  0.220
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.993
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.940
  </td>
   
   <td class="ee-details">
  4.970
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0005.jpg">shaman_3_0005</a></td>
   
   <td class="ae">
  0.404
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.406
  </td>
   
   <td class="ae-details">
  0.315
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.927
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.830
  </td>
   
   <td class="ee-details">
  6.300
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.085
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0006.jpg">shaman_3_0006</a></td>
   
   <td class="ae">
  0.386
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.385
  </td>
   
   <td class="ae-details">
  0.394
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.927
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.786
  </td>
   
   <td class="ee-details">
  7.207
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.094
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0007.jpg">shaman_3_0007</a></td>
   
   <td class="ae">
  0.375
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.375
  </td>
   
   <td class="ae-details">
  0.384
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.899
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.748
  </td>
   
   <td class="ee-details">
  6.619
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.093
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0008.jpg">shaman_3_0008</a></td>
   
   <td class="ae">
  0.386
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.386
  </td>
   
   <td class="ae-details">
  0.380
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.891
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.735
  </td>
   
   <td class="ee-details">
  6.026
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0009.jpg">shaman_3_0009</a></td>
   
   <td class="ae">
  0.376
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.377
  </td>
   
   <td class="ae-details">
  0.344
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.730
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.584
  </td>
   
   <td class="ee-details">
  5.079
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0010.jpg">shaman_3_0010</a></td>
   
   <td class="ae">
  0.368
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.369
  </td>
   
   <td class="ae-details">
  0.350
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.701
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.547
  </td>
   
   <td class="ee-details">
  4.749
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0011.jpg">shaman_3_0011</a></td>
   
   <td class="ae">
  0.360
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.360
  </td>
   
   <td class="ae-details">
  0.350
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.613
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.458
  </td>
   
   <td class="ee-details">
  4.311
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.132
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0012.jpg">shaman_3_0012</a></td>
   
   <td class="ae">
  0.354
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.355
  </td>
   
   <td class="ae-details">
  0.332
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.537
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.445
  </td>
   
   <td class="ee-details">
  3.767
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.096
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0013.jpg">shaman_3_0013</a></td>
   
   <td class="ae">
  0.339
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.339
  </td>
   
   <td class="ae-details">
  0.330
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.466
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.425
  </td>
   
   <td class="ee-details">
  3.605
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0014.jpg">shaman_3_0014</a></td>
   
   <td class="ae">
  0.339
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.338
  </td>
   
   <td class="ae-details">
  0.387
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.439
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.423
  </td>
   
   <td class="ee-details">
  4.443
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0015.jpg">shaman_3_0015</a></td>
   
   <td class="ae">
  0.333
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.333
  </td>
   
   <td class="ae-details">
  0.400
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.366
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.356
  </td>
   
   <td class="ee-details">
  4.724
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0016.jpg">shaman_3_0016</a></td>
   
   <td class="ae">
  0.323
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.323
  </td>
   
   <td class="ae-details">
  0.284
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.336
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.332
  </td>
   
   <td class="ee-details">
  4.370
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.108
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0017.jpg">shaman_3_0017</a></td>
   
   <td class="ae">
  0.317
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.317
  </td>
   
   <td class="ae-details">
  0.283
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.293
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.289
  </td>
   
   <td class="ee-details">
  4.649
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.088
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0018.jpg">shaman_3_0018</a></td>
   
   <td class="ae">
  0.305
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.305
  </td>
   
   <td class="ae-details">
  0.217
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.223
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.221
  </td>
   
   <td class="ee-details">
  5.237
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0019.jpg">shaman_3_0019</a></td>
   
   <td class="ae">
  0.297
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.297
  </td>
   
   <td class="ae-details">
  0.195
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.170
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.170
  </td>
   
   <td class="ee-details">
  5.989
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0020.jpg">shaman_3_0020</a></td>
   
   <td class="ae">
  0.288
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.288
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.077
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.077
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.131
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0021.jpg">shaman_3_0021</a></td>
   
   <td class="ae">
  0.282
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.282
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.061
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.061
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.100
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0022.jpg">shaman_3_0022</a></td>
   
   <td class="ae">
  0.284
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.284
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.067
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.067
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0023.jpg">shaman_3_0023</a></td>
   
   <td class="ae">
  0.290
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.290
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.090
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.090
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0024.jpg">shaman_3_0024</a></td>
   
   <td class="ae">
  0.288
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.288
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.066
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.066
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0025.jpg">shaman_3_0025</a></td>
   
   <td class="ae">
  0.274
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.274
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.012
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.012
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.110
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0026.jpg">shaman_3_0026</a></td>
   
   <td class="ae">
  0.265
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.265
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.962
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.962
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.096
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0027.jpg">shaman_3_0027</a></td>
   
   <td class="ae">
  0.261
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.261
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.988
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.988
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0028.jpg">shaman_3_0028</a></td>
   
   <td class="ae">
  0.265
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.265
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.970
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.970
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0029.jpg">shaman_3_0029</a></td>
   
   <td class="ae">
  0.268
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.268
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.981
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.981
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.109
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0030.jpg">shaman_3_0030</a></td>
   
   <td class="ae">
  0.266
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.266
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.041
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.041
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.096
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0031.jpg">shaman_3_0031</a></td>
   
   <td class="ae">
  0.267
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.267
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.005
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.005
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0032.jpg">shaman_3_0032</a></td>
   
   <td class="ae">
  0.259
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.259
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.999
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.999
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0033.jpg">shaman_3_0033</a></td>
   
   <td class="ae">
  0.267
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.267
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.012
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.012
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.097
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0034.jpg">shaman_3_0034</a></td>
   
   <td class="ae">
  0.272
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.272
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.051
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.051
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0035.jpg">shaman_3_0035</a></td>
   
   <td class="ae">
  0.281
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.281
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.116
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.116
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0036.jpg">shaman_3_0036</a></td>
   
   <td class="ae">
  0.287
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.287
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.183
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.183
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.082
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0037.jpg">shaman_3_0037</a></td>
   
   <td class="ae">
  0.285
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.285
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.216
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.216
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0038.jpg">shaman_3_0038</a></td>
   
   <td class="ae">
  0.289
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.289
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.309
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.309
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.083
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0039.jpg">shaman_3_0039</a></td>
   
   <td class="ae">
  0.293
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.293
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.372
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.372
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0040.jpg">shaman_3_0040</a></td>
   
   <td class="ae">
  0.295
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.295
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.368
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.368
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0041.jpg">shaman_3_0041</a></td>
   
   <td class="ae">
  0.282
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.282
  </td>
   
   <td class="ae-details">
  0.060
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.356
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.356
  </td>
   
   <td class="ee-details">
  2.137
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.127
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0042.jpg">shaman_3_0042</a></td>
   
   <td class="ae">
  0.282
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.282
  </td>
   
   <td class="ae-details">
  0.115
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.364
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.364
  </td>
   
   <td class="ee-details">
  2.922
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.088
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0043.jpg">shaman_3_0043</a></td>
   
   <td class="ae">
  0.293
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.293
  </td>
   
   <td class="ae-details">
  0.215
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.354
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.354
  </td>
   
   <td class="ee-details">
  2.380
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0044.jpg">shaman_3_0044</a></td>
   
   <td class="ae">
  0.302
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.302
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.344
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.344
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0045.jpg">shaman_3_0045</a></td>
   
   <td class="ae">
  0.309
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.309
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.331
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.331
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.086
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0046.jpg">shaman_3_0046</a></td>
   
   <td class="ae">
  0.309
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.309
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.289
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.289
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.141
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0047.jpg">shaman_3_0047</a></td>
   
   <td class="ae">
  0.306
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.306
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.298
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.298
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.098
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0048.jpg">shaman_3_0048</a></td>
   
   <td class="ae">
  0.314
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.314
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.371
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.371
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/shaman_3_0049.jpg">shaman_3_0049</a></td>
   
   <td class="ae">
  0.317
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.317
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.398
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.398
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0001.jpg">sleeping_1_0001</a></td>
   
   <td class="ae">
  0.243
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.243
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.368
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.368
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.062
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0002.jpg">sleeping_1_0002</a></td>
   
   <td class="ae">
  0.246
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.246
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.374
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.374
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0003.jpg">sleeping_1_0003</a></td>
   
   <td class="ae">
  0.243
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.243
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.372
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.372
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0004.jpg">sleeping_1_0004</a></td>
   
   <td class="ae">
  0.244
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.244
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.371
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.371
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.084
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0005.jpg">sleeping_1_0005</a></td>
   
   <td class="ae">
  0.244
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.244
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.363
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.363
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.086
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0006.jpg">sleeping_1_0006</a></td>
   
   <td class="ae">
  0.246
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.246
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.363
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.363
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.124
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0007.jpg">sleeping_1_0007</a></td>
   
   <td class="ae">
  0.244
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.244
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.362
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.362
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.097
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0008.jpg">sleeping_1_0008</a></td>
   
   <td class="ae">
  0.244
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.244
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.359
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.359
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0009.jpg">sleeping_1_0009</a></td>
   
   <td class="ae">
  0.248
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.248
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.372
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.372
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.106
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0010.jpg">sleeping_1_0010</a></td>
   
   <td class="ae">
  0.246
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.246
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.357
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.357
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.082
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0011.jpg">sleeping_1_0011</a></td>
   
   <td class="ae">
  0.249
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.249
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.376
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.376
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0012.jpg">sleeping_1_0012</a></td>
   
   <td class="ae">
  0.248
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.248
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.366
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.366
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0013.jpg">sleeping_1_0013</a></td>
   
   <td class="ae">
  0.252
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.252
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.379
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.379
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.083
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0014.jpg">sleeping_1_0014</a></td>
   
   <td class="ae">
  0.251
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.251
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.379
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.379
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.120
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0015.jpg">sleeping_1_0015</a></td>
   
   <td class="ae">
  0.256
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.256
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.374
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.374
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.094
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0016.jpg">sleeping_1_0016</a></td>
   
   <td class="ae">
  0.257
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.257
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.381
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.381
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0017.jpg">sleeping_1_0017</a></td>
   
   <td class="ae">
  0.257
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.257
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.366
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.366
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.123
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0018.jpg">sleeping_1_0018</a></td>
   
   <td class="ae">
  0.257
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.257
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.342
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.342
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.093
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0019.jpg">sleeping_1_0019</a></td>
   
   <td class="ae">
  0.261
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.261
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.361
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.361
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0020.jpg">sleeping_1_0020</a></td>
   
   <td class="ae">
  0.260
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.260
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.335
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.335
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0021.jpg">sleeping_1_0021</a></td>
   
   <td class="ae">
  0.261
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.261
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.324
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.324
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0022.jpg">sleeping_1_0022</a></td>
   
   <td class="ae">
  0.261
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.261
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.319
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.319
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0023.jpg">sleeping_1_0023</a></td>
   
   <td class="ae">
  0.264
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.264
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.307
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.307
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0024.jpg">sleeping_1_0024</a></td>
   
   <td class="ae">
  0.266
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.266
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.288
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.288
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0025.jpg">sleeping_1_0025</a></td>
   
   <td class="ae">
  0.267
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.267
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.278
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.278
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0026.jpg">sleeping_1_0026</a></td>
   
   <td class="ae">
  0.270
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.270
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.268
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.268
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.131
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0027.jpg">sleeping_1_0027</a></td>
   
   <td class="ae">
  0.266
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.266
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.262
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.262
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.104
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0028.jpg">sleeping_1_0028</a></td>
   
   <td class="ae">
  0.268
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.268
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.268
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.268
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.085
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0029.jpg">sleeping_1_0029</a></td>
   
   <td class="ae">
  0.268
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.268
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.275
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.275
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0030.jpg">sleeping_1_0030</a></td>
   
   <td class="ae">
  0.270
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.270
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.298
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.298
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0031.jpg">sleeping_1_0031</a></td>
   
   <td class="ae">
  0.269
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.269
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.275
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.275
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0032.jpg">sleeping_1_0032</a></td>
   
   <td class="ae">
  0.265
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.265
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.274
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.274
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0033.jpg">sleeping_1_0033</a></td>
   
   <td class="ae">
  0.266
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.266
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.280
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.280
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0034.jpg">sleeping_1_0034</a></td>
   
   <td class="ae">
  0.271
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.271
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.256
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.256
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.099
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0035.jpg">sleeping_1_0035</a></td>
   
   <td class="ae">
  0.270
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.270
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.247
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.247
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.081
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0036.jpg">sleeping_1_0036</a></td>
   
   <td class="ae">
  0.278
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.278
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.241
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.241
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.081
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0037.jpg">sleeping_1_0037</a></td>
   
   <td class="ae">
  0.274
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.274
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.248
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.248
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0038.jpg">sleeping_1_0038</a></td>
   
   <td class="ae">
  0.275
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.275
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.251
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.251
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.131
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0039.jpg">sleeping_1_0039</a></td>
   
   <td class="ae">
  0.274
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.274
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.236
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.236
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.092
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0040.jpg">sleeping_1_0040</a></td>
   
   <td class="ae">
  0.276
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.276
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.260
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.260
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.086
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0041.jpg">sleeping_1_0041</a></td>
   
   <td class="ae">
  0.276
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.276
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.266
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.266
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0042.jpg">sleeping_1_0042</a></td>
   
   <td class="ae">
  0.271
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.271
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.264
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.264
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.114
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0043.jpg">sleeping_1_0043</a></td>
   
   <td class="ae">
  0.272
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.272
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.269
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.269
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.102
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0044.jpg">sleeping_1_0044</a></td>
   
   <td class="ae">
  0.271
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.271
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.271
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.271
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0045.jpg">sleeping_1_0045</a></td>
   
   <td class="ae">
  0.268
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.268
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.275
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.275
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0046.jpg">sleeping_1_0046</a></td>
   
   <td class="ae">
  0.270
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.270
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.278
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.278
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0047.jpg">sleeping_1_0047</a></td>
   
   <td class="ae">
  0.265
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.265
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.273
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.273
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.094
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0048.jpg">sleeping_1_0048</a></td>
   
   <td class="ae">
  0.266
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.266
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.291
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.291
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_1_0049.jpg">sleeping_1_0049</a></td>
   
   <td class="ae">
  0.265
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.265
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  1.292
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.292
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0001.jpg">sleeping_2_0001</a></td>
   
   <td class="ae">
  0.267
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.267
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.653
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.653
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.128
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0002.jpg">sleeping_2_0002</a></td>
   
   <td class="ae">
  0.269
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.269
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.656
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.656
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.097
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0003.jpg">sleeping_2_0003</a></td>
   
   <td class="ae">
  0.266
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.266
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.662
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.662
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0004.jpg">sleeping_2_0004</a></td>
   
   <td class="ae">
  0.262
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.262
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.663
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.663
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.118
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0005.jpg">sleeping_2_0005</a></td>
   
   <td class="ae">
  0.266
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.266
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.676
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.676
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.102
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0006.jpg">sleeping_2_0006</a></td>
   
   <td class="ae">
  0.269
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.269
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.685
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.685
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0007.jpg">sleeping_2_0007</a></td>
   
   <td class="ae">
  0.260
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.260
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.678
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.678
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.112
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0008.jpg">sleeping_2_0008</a></td>
   
   <td class="ae">
  0.262
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.262
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.680
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.680
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.090
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0009.jpg">sleeping_2_0009</a></td>
   
   <td class="ae">
  0.262
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.262
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.695
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.695
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.085
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0010.jpg">sleeping_2_0010</a></td>
   
   <td class="ae">
  0.262
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.262
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.694
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.694
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.128
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0011.jpg">sleeping_2_0011</a></td>
   
   <td class="ae">
  0.264
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.264
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.701
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.701
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.101
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0012.jpg">sleeping_2_0012</a></td>
   
   <td class="ae">
  0.258
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.258
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.713
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.713
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.083
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0013.jpg">sleeping_2_0013</a></td>
   
   <td class="ae">
  0.254
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.254
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.700
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.700
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0014.jpg">sleeping_2_0014</a></td>
   
   <td class="ae">
  0.260
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.260
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.723
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.723
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0015.jpg">sleeping_2_0015</a></td>
   
   <td class="ae">
  0.255
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.255
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.719
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.719
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.063
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0016.jpg">sleeping_2_0016</a></td>
   
   <td class="ae">
  0.254
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.254
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.719
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.719
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.070
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0017.jpg">sleeping_2_0017</a></td>
   
   <td class="ae">
  0.254
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.254
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.726
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.726
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.104
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0018.jpg">sleeping_2_0018</a></td>
   
   <td class="ae">
  0.255
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.255
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.733
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.733
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.088
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0019.jpg">sleeping_2_0019</a></td>
   
   <td class="ae">
  0.252
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.252
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.733
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.733
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0020.jpg">sleeping_2_0020</a></td>
   
   <td class="ae">
  0.254
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.254
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.743
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.743
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.081
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0021.jpg">sleeping_2_0021</a></td>
   
   <td class="ae">
  0.255
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.255
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.753
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.753
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.114
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0022.jpg">sleeping_2_0022</a></td>
   
   <td class="ae">
  0.248
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.248
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.746
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.746
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0023.jpg">sleeping_2_0023</a></td>
   
   <td class="ae">
  0.255
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.255
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.766
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.766
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.088
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0024.jpg">sleeping_2_0024</a></td>
   
   <td class="ae">
  0.251
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.251
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.763
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.763
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0025.jpg">sleeping_2_0025</a></td>
   
   <td class="ae">
  0.253
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.253
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.768
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.768
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0026.jpg">sleeping_2_0026</a></td>
   
   <td class="ae">
  0.255
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.255
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.783
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.783
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0027.jpg">sleeping_2_0027</a></td>
   
   <td class="ae">
  0.251
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.251
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.770
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.770
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.125
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0028.jpg">sleeping_2_0028</a></td>
   
   <td class="ae">
  0.252
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.252
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.783
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.783
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.096
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0029.jpg">sleeping_2_0029</a></td>
   
   <td class="ae">
  0.255
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.255
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.808
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.808
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0030.jpg">sleeping_2_0030</a></td>
   
   <td class="ae">
  0.254
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.254
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.805
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.805
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.081
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0031.jpg">sleeping_2_0031</a></td>
   
   <td class="ae">
  0.252
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.252
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.794
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.794
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.088
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0032.jpg">sleeping_2_0032</a></td>
   
   <td class="ae">
  0.248
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.248
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.790
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.790
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0033.jpg">sleeping_2_0033</a></td>
   
   <td class="ae">
  0.249
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.249
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.805
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.805
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0034.jpg">sleeping_2_0034</a></td>
   
   <td class="ae">
  0.250
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.250
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.806
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.806
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0035.jpg">sleeping_2_0035</a></td>
   
   <td class="ae">
  0.253
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.253
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.828
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.828
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.096
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0036.jpg">sleeping_2_0036</a></td>
   
   <td class="ae">
  0.250
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.250
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.822
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.822
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.081
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0037.jpg">sleeping_2_0037</a></td>
   
   <td class="ae">
  0.250
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.250
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.825
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.825
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0038.jpg">sleeping_2_0038</a></td>
   
   <td class="ae">
  0.252
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.252
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.831
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.831
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0039.jpg">sleeping_2_0039</a></td>
   
   <td class="ae">
  0.255
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.255
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.847
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.847
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.143
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0040.jpg">sleeping_2_0040</a></td>
   
   <td class="ae">
  0.253
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.253
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.851
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.851
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.083
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0041.jpg">sleeping_2_0041</a></td>
   
   <td class="ae">
  0.252
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.252
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.853
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.853
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0042.jpg">sleeping_2_0042</a></td>
   
   <td class="ae">
  0.250
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.250
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.859
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.859
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0043.jpg">sleeping_2_0043</a></td>
   
   <td class="ae">
  0.254
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.254
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.871
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.871
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.089
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0044.jpg">sleeping_2_0044</a></td>
   
   <td class="ae">
  0.254
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.254
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.881
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.881
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0045.jpg">sleeping_2_0045</a></td>
   
   <td class="ae">
  0.251
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.251
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.883
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.883
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0046.jpg">sleeping_2_0046</a></td>
   
   <td class="ae">
  0.251
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.251
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.880
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.880
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0047.jpg">sleeping_2_0047</a></td>
   
   <td class="ae">
  0.250
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.250
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.891
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.891
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.068
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0048.jpg">sleeping_2_0048</a></td>
   
   <td class="ae">
  0.252
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.252
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.899
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.899
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.098
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/sleeping_2_0049.jpg">sleeping_2_0049</a></td>
   
   <td class="ae">
  0.253
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.253
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  0.909
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  0.909
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0001.jpg">temple_2_0001</a></td>
   
   <td class="ae">
  0.308
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.334
  </td>
   
   <td class="ae-details">
  0.269
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.262
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.854
  </td>
   
   <td class="ee-details">
  3.858
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0002.jpg">temple_2_0002</a></td>
   
   <td class="ae">
  0.300
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.307
  </td>
   
   <td class="ae-details">
  0.290
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.091
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.535
  </td>
   
   <td class="ee-details">
  3.878
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0003.jpg">temple_2_0003</a></td>
   
   <td class="ae">
  0.284
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.288
  </td>
   
   <td class="ae-details">
  0.278
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.069
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.496
  </td>
   
   <td class="ee-details">
  3.852
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.134
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0004.jpg">temple_2_0004</a></td>
   
   <td class="ae">
  0.276
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.276
  </td>
   
   <td class="ae-details">
  0.277
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.001
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.356
  </td>
   
   <td class="ee-details">
  3.848
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.094
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0005.jpg">temple_2_0005</a></td>
   
   <td class="ae">
  0.260
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.252
  </td>
   
   <td class="ae-details">
  0.270
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.079
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.337
  </td>
   
   <td class="ee-details">
  3.977
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.078
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0006.jpg">temple_2_0006</a></td>
   
   <td class="ae">
  0.307
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.319
  </td>
   
   <td class="ae-details">
  0.294
  </td>
   
   <td class="ae-details">
  0.160
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.361
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.670
  </td>
   
   <td class="ee-details">
  4.086
  </td>
   
   <td class="ee-details">
  13.382
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.139
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0007.jpg">temple_2_0007</a></td>
   
   <td class="ae">
  0.305
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.306
  </td>
   
   <td class="ae-details">
  0.273
  </td>
   
   <td class="ae-details">
  1.659
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.147
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.564
  </td>
   
   <td class="ee-details">
  3.982
  </td>
   
   <td class="ee-details">
  84.320
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.100
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0008.jpg">temple_2_0008</a></td>
   
   <td class="ae">
  0.292
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.309
  </td>
   
   <td class="ae-details">
  0.274
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.111
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.381
  </td>
   
   <td class="ee-details">
  3.898
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0009.jpg">temple_2_0009</a></td>
   
   <td class="ae">
  0.274
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.273
  </td>
   
   <td class="ae-details">
  0.274
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.238
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.233
  </td>
   
   <td class="ee-details">
  4.306
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.069
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0010.jpg">temple_2_0010</a></td>
   
   <td class="ae">
  0.279
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.285
  </td>
   
   <td class="ae-details">
  0.273
  </td>
   
   <td class="ae-details">
  0.568
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.240
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.287
  </td>
   
   <td class="ee-details">
  4.215
  </td>
   
   <td class="ee-details">
  31.578
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0011.jpg">temple_2_0011</a></td>
   
   <td class="ae">
  0.284
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.304
  </td>
   
   <td class="ae-details">
  0.263
  </td>
   
   <td class="ae-details">
  0.265
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.264
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.274
  </td>
   
   <td class="ee-details">
  4.295
  </td>
   
   <td class="ee-details">
  27.085
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.126
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0012.jpg">temple_2_0012</a></td>
   
   <td class="ae">
  0.300
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.325
  </td>
   
   <td class="ae-details">
  0.276
  </td>
   
   <td class="ae-details">
  0.180
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.553
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.400
  </td>
   
   <td class="ee-details">
  4.368
  </td>
   
   <td class="ee-details">
  28.605
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.089
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0013.jpg">temple_2_0013</a></td>
   
   <td class="ae">
  0.284
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.307
  </td>
   
   <td class="ae-details">
  0.241
  </td>
   
   <td class="ae-details">
  1.113
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.180
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.631
  </td>
   
   <td class="ee-details">
  4.195
  </td>
   
   <td class="ee-details">
  71.190
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0014.jpg">temple_2_0014</a></td>
   
   <td class="ae">
  0.265
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.355
  </td>
   
   <td class="ae-details">
  0.173
  </td>
   
   <td class="ae-details">
  0.640
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.859
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.024
  </td>
   
   <td class="ee-details">
  3.975
  </td>
   
   <td class="ee-details">
  61.547
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0015.jpg">temple_2_0015</a></td>
   
   <td class="ae">
  0.260
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.333
  </td>
   
   <td class="ae-details">
  0.185
  </td>
   
   <td class="ae-details">
  0.720
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.126
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.139
  </td>
   
   <td class="ee-details">
  4.322
  </td>
   
   <td class="ee-details">
  37.239
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.126
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0016.jpg">temple_2_0016</a></td>
   
   <td class="ae">
  0.277
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.366
  </td>
   
   <td class="ae-details">
  0.190
  </td>
   
   <td class="ae-details">
  0.972
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.396
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.767
  </td>
   
   <td class="ee-details">
  4.672
  </td>
   
   <td class="ee-details">
  38.803
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.103
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0017.jpg">temple_2_0017</a></td>
   
   <td class="ae">
  0.315
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.374
  </td>
   
   <td class="ae-details">
  0.237
  </td>
   
   <td class="ae-details">
  0.613
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.540
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.641
  </td>
   
   <td class="ee-details">
  4.968
  </td>
   
   <td class="ee-details">
  35.536
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0018.jpg">temple_2_0018</a></td>
   
   <td class="ae">
  0.303
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.416
  </td>
   
   <td class="ae-details">
  0.161
  </td>
   
   <td class="ae-details">
  0.479
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  7.057
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.312
  </td>
   
   <td class="ee-details">
  5.203
  </td>
   
   <td class="ee-details">
  31.574
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0019.jpg">temple_2_0019</a></td>
   
   <td class="ae">
  0.437
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.352
  </td>
   
   <td class="ae-details">
  0.350
  </td>
   
   <td class="ae-details">
  1.094
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  14.146
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.095
  </td>
   
   <td class="ee-details">
  6.877
  </td>
   
   <td class="ee-details">
  83.621
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0020.jpg">temple_2_0020</a></td>
   
   <td class="ae">
  0.337
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.355
  </td>
   
   <td class="ae-details">
  0.248
  </td>
   
   <td class="ae-details">
  0.555
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  7.761
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.650
  </td>
   
   <td class="ee-details">
  5.564
  </td>
   
   <td class="ee-details">
  35.592
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0021.jpg">temple_2_0021</a></td>
   
   <td class="ae">
  0.366
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.342
  </td>
   
   <td class="ae-details">
  0.274
  </td>
   
   <td class="ae-details">
  0.629
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  10.973
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.894
  </td>
   
   <td class="ee-details">
  6.747
  </td>
   
   <td class="ee-details">
  43.208
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.083
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0022.jpg">temple_2_0022</a></td>
   
   <td class="ae">
  0.358
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.433
  </td>
   
   <td class="ae-details">
  0.228
  </td>
   
   <td class="ae-details">
  0.390
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  12.762
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.521
  </td>
   
   <td class="ee-details">
  4.628
  </td>
   
   <td class="ee-details">
  49.062
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0023.jpg">temple_2_0023</a></td>
   
   <td class="ae">
  0.528
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.404
  </td>
   
   <td class="ae-details">
  0.329
  </td>
   
   <td class="ae-details">
  1.068
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  22.206
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.033
  </td>
   
   <td class="ee-details">
  5.553
  </td>
   
   <td class="ee-details">
  86.416
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.129
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0024.jpg">temple_2_0024</a></td>
   
   <td class="ae">
  0.561
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.447
  </td>
   
   <td class="ae-details">
  0.424
  </td>
   
   <td class="ae-details">
  1.004
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  25.440
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.298
  </td>
   
   <td class="ee-details">
  5.907
  </td>
   
   <td class="ee-details">
  101.310
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.097
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0025.jpg">temple_2_0025</a></td>
   
   <td class="ae">
  0.587
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.337
  </td>
   
   <td class="ae-details">
  0.423
  </td>
   
   <td class="ae-details">
  1.462
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  26.519
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.679
  </td>
   
   <td class="ee-details">
  6.447
  </td>
   
   <td class="ee-details">
  117.605
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.088
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0026.jpg">temple_2_0026</a></td>
   
   <td class="ae">
  0.429
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.432
  </td>
   
   <td class="ae-details">
  0.223
  </td>
   
   <td class="ae-details">
  0.849
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  15.957
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.978
  </td>
   
   <td class="ee-details">
  4.667
  </td>
   
   <td class="ee-details">
  74.346
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.082
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0027.jpg">temple_2_0027</a></td>
   
   <td class="ae">
  0.476
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.365
  </td>
   
   <td class="ae-details">
  0.408
  </td>
   
   <td class="ae-details">
  1.083
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  12.728
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.077
  </td>
   
   <td class="ee-details">
  7.659
  </td>
   
   <td class="ee-details">
  63.398
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.140
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0028.jpg">temple_2_0028</a></td>
   
   <td class="ae">
  0.443
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.339
  </td>
   
   <td class="ae-details">
  0.281
  </td>
   
   <td class="ae-details">
  1.104
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  14.533
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.486
  </td>
   
   <td class="ee-details">
  5.265
  </td>
   
   <td class="ee-details">
  71.463
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.097
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0029.jpg">temple_2_0029</a></td>
   
   <td class="ae">
  0.328
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.272
  </td>
   
   <td class="ae-details">
  0.210
  </td>
   
   <td class="ae-details">
  0.972
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  14.552
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.134
  </td>
   
   <td class="ee-details">
  4.416
  </td>
   
   <td class="ee-details">
  109.483
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0030.jpg">temple_2_0030</a></td>
   
   <td class="ae">
  0.299
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.234
  </td>
   
   <td class="ae-details">
  0.327
  </td>
   
   <td class="ae-details">
  1.003
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  8.275
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.758
  </td>
   
   <td class="ee-details">
  5.053
  </td>
   
   <td class="ee-details">
  129.110
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.102
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0031.jpg">temple_2_0031</a></td>
   
   <td class="ae">
  0.238
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.279
  </td>
   
   <td class="ae-details">
  0.155
  </td>
   
   <td class="ae-details">
  1.448
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.097
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.286
  </td>
   
   <td class="ee-details">
  4.041
  </td>
   
   <td class="ee-details">
  56.771
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.084
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0032.jpg">temple_2_0032</a></td>
   
   <td class="ae">
  0.203
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.245
  </td>
   
   <td class="ae-details">
  0.120
  </td>
   
   <td class="ae-details">
  0.342
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.990
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.803
  </td>
   
   <td class="ee-details">
  3.832
  </td>
   
   <td class="ee-details">
  50.243
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.066
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0033.jpg">temple_2_0033</a></td>
   
   <td class="ae">
  0.200
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.234
  </td>
   
   <td class="ae-details">
  0.120
  </td>
   
   <td class="ae-details">
  0.526
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.059
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.784
  </td>
   
   <td class="ee-details">
  3.744
  </td>
   
   <td class="ee-details">
  45.019
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0034.jpg">temple_2_0034</a></td>
   
   <td class="ae">
  0.190
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.225
  </td>
   
   <td class="ae-details">
  0.104
  </td>
   
   <td class="ae-details">
  0.396
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.126
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.010
  </td>
   
   <td class="ee-details">
  3.827
  </td>
   
   <td class="ee-details">
  29.056
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0035.jpg">temple_2_0035</a></td>
   
   <td class="ae">
  0.191
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.228
  </td>
   
   <td class="ae-details">
  0.109
  </td>
   
   <td class="ae-details">
  0.409
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.267
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.937
  </td>
   
   <td class="ee-details">
  4.599
  </td>
   
   <td class="ee-details">
  48.894
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0036.jpg">temple_2_0036</a></td>
   
   <td class="ae">
  0.187
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.224
  </td>
   
   <td class="ae-details">
  0.103
  </td>
   
   <td class="ae-details">
  0.153
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.746
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.892
  </td>
   
   <td class="ee-details">
  4.111
  </td>
   
   <td class="ee-details">
  60.775
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.104
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0037.jpg">temple_2_0037</a></td>
   
   <td class="ae">
  0.175
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.208
  </td>
   
   <td class="ae-details">
  0.094
  </td>
   
   <td class="ae-details">
  0.450
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.407
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.706
  </td>
   
   <td class="ee-details">
  4.058
  </td>
   
   <td class="ee-details">
  41.984
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.085
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0038.jpg">temple_2_0038</a></td>
   
   <td class="ae">
  0.165
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.193
  </td>
   
   <td class="ae-details">
  0.093
  </td>
   
   <td class="ae-details">
  0.671
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.332
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.648
  </td>
   
   <td class="ee-details">
  4.002
  </td>
   
   <td class="ee-details">
  32.336
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0039.jpg">temple_2_0039</a></td>
   
   <td class="ae">
  0.163
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.183
  </td>
   
   <td class="ae-details">
  0.108
  </td>
   
   <td class="ae-details">
  1.096
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.308
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.638
  </td>
   
   <td class="ee-details">
  4.082
  </td>
   
   <td class="ee-details">
  64.467
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.125
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0040.jpg">temple_2_0040</a></td>
   
   <td class="ae">
  0.160
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.180
  </td>
   
   <td class="ae-details">
  0.103
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.306
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.674
  </td>
   
   <td class="ee-details">
  4.095
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.101
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0041.jpg">temple_2_0041</a></td>
   
   <td class="ae">
  0.155
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.174
  </td>
   
   <td class="ae-details">
  0.096
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.227
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.661
  </td>
   
   <td class="ee-details">
  3.984
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0042.jpg">temple_2_0042</a></td>
   
   <td class="ae">
  0.154
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.172
  </td>
   
   <td class="ae-details">
  0.091
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.186
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.677
  </td>
   
   <td class="ee-details">
  3.950
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0043.jpg">temple_2_0043</a></td>
   
   <td class="ae">
  0.155
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.172
  </td>
   
   <td class="ae-details">
  0.093
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.185
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.686
  </td>
   
   <td class="ee-details">
  4.085
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.131
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0044.jpg">temple_2_0044</a></td>
   
   <td class="ae">
  0.154
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.174
  </td>
   
   <td class="ae-details">
  0.074
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.164
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.736
  </td>
   
   <td class="ee-details">
  3.946
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.094
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0045.jpg">temple_2_0045</a></td>
   
   <td class="ae">
  0.157
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.172
  </td>
   
   <td class="ae-details">
  0.086
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.133
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.726
  </td>
   
   <td class="ee-details">
  3.998
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.075
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0046.jpg">temple_2_0046</a></td>
   
   <td class="ae">
  0.153
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.167
  </td>
   
   <td class="ae-details">
  0.079
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.109
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.751
  </td>
   
   <td class="ee-details">
  3.933
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0047.jpg">temple_2_0047</a></td>
   
   <td class="ae">
  0.155
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.170
  </td>
   
   <td class="ae-details">
  0.069
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.068
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.797
  </td>
   
   <td class="ee-details">
  3.631
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.104
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0048.jpg">temple_2_0048</a></td>
   
   <td class="ae">
  0.156
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.169
  </td>
   
   <td class="ae-details">
  0.070
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.033
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.795
  </td>
   
   <td class="ee-details">
  3.554
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.088
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_2_0049.jpg">temple_2_0049</a></td>
   
   <td class="ae">
  0.161
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.175
  </td>
   
   <td class="ae-details">
  0.063
  </td>
   
   <td class="ae-details">
  n/a
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  2.018
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  1.815
  </td>
   
   <td class="ee-details">
  3.454
  </td>
   
   <td class="ee-details">
  n/a
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0001.jpg">temple_3_0001</a></td>
   
   <td class="ae">
  1.077
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.127
  </td>
   
   <td class="ae-details">
  0.226
  </td>
   
   <td class="ae-details">
  0.215
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  8.462
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  8.317
  </td>
   
   <td class="ee-details">
  8.188
  </td>
   
   <td class="ee-details">
  16.668
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0002.jpg">temple_3_0002</a></td>
   
   <td class="ae">
  1.058
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.172
  </td>
   
   <td class="ae-details">
  0.186
  </td>
   
   <td class="ae-details">
  0.095
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  7.812
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  8.033
  </td>
   
   <td class="ee-details">
  4.503
  </td>
   
   <td class="ee-details">
  15.042
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.106
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0003.jpg">temple_3_0003</a></td>
   
   <td class="ae">
  0.904
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.993
  </td>
   
   <td class="ae-details">
  0.282
  </td>
   
   <td class="ae-details">
  0.101
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  7.041
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  6.907
  </td>
   
   <td class="ee-details">
  6.082
  </td>
   
   <td class="ee-details">
  17.261
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.083
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0004.jpg">temple_3_0004</a></td>
   
   <td class="ae">
  0.809
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.871
  </td>
   
   <td class="ae-details">
  0.347
  </td>
   
   <td class="ae-details">
  0.456
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  6.018
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  5.415
  </td>
   
   <td class="ee-details">
  7.243
  </td>
   
   <td class="ee-details">
  23.567
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0005.jpg">temple_3_0005</a></td>
   
   <td class="ae">
  0.700
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.736
  </td>
   
   <td class="ae-details">
  0.293
  </td>
   
   <td class="ae-details">
  0.912
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.718
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.664
  </td>
   
   <td class="ee-details">
  4.309
  </td>
   
   <td class="ee-details">
  39.300
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0006.jpg">temple_3_0006</a></td>
   
   <td class="ae">
  0.637
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.636
  </td>
   
   <td class="ae-details">
  0.730
  </td>
   
   <td class="ae-details">
  0.715
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.475
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.288
  </td>
   
   <td class="ee-details">
  22.327
  </td>
   
   <td class="ee-details">
  30.539
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0007.jpg">temple_3_0007</a></td>
   
   <td class="ae">
  0.532
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.531
  </td>
   
   <td class="ae-details">
  0.761
  </td>
   
   <td class="ae-details">
  0.528
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.291
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.203
  </td>
   
   <td class="ee-details">
  18.458
  </td>
   
   <td class="ee-details">
  41.733
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.064
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0008.jpg">temple_3_0008</a></td>
   
   <td class="ae">
  0.359
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.358
  </td>
   
   <td class="ae-details">
  0.670
  </td>
   
   <td class="ae-details">
  1.000
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.814
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.803
  </td>
   
   <td class="ee-details">
  11.387
  </td>
   
   <td class="ee-details">
  41.258
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.101
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0009.jpg">temple_3_0009</a></td>
   
   <td class="ae">
  0.349
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.349
  </td>
   
   <td class="ae-details">
  0.380
  </td>
   
   <td class="ae-details">
  0.380
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.212
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.174
  </td>
   
   <td class="ee-details">
  12.590
  </td>
   
   <td class="ee-details">
  29.650
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.091
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0010.jpg">temple_3_0010</a></td>
   
   <td class="ae">
  0.240
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.238
  </td>
   
   <td class="ae-details">
  0.293
  </td>
   
   <td class="ae-details">
  0.689
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.098
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.957
  </td>
   
   <td class="ee-details">
  5.837
  </td>
   
   <td class="ee-details">
  50.998
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0011.jpg">temple_3_0011</a></td>
   
   <td class="ae">
  0.201
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.208
  </td>
   
   <td class="ae-details">
  0.152
  </td>
   
   <td class="ae-details">
  0.262
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.162
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.262
  </td>
   
   <td class="ee-details">
  3.423
  </td>
   
   <td class="ee-details">
  20.343
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0012.jpg">temple_3_0012</a></td>
   
   <td class="ae">
  0.181
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.179
  </td>
   
   <td class="ae-details">
  0.176
  </td>
   
   <td class="ae-details">
  0.992
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  3.972
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.859
  </td>
   
   <td class="ee-details">
  3.882
  </td>
   
   <td class="ee-details">
  38.529
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.130
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0013.jpg">temple_3_0013</a></td>
   
   <td class="ae">
  0.185
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.284
  </td>
   
   <td class="ae-details">
  0.172
  </td>
   
   <td class="ae-details">
  0.878
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.181
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.060
  </td>
   
   <td class="ee-details">
  4.265
  </td>
   
   <td class="ee-details">
  47.841
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.103
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0014.jpg">temple_3_0014</a></td>
   
   <td class="ae">
  0.222
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.334
  </td>
   
   <td class="ae-details">
  0.207
  </td>
   
   <td class="ae-details">
  1.829
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  4.503
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.252
  </td>
   
   <td class="ee-details">
  4.665
  </td>
   
   <td class="ee-details">
  47.940
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0015.jpg">temple_3_0015</a></td>
   
   <td class="ae">
  0.287
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.191
  </td>
   
   <td class="ae-details">
  0.300
  </td>
   
   <td class="ae-details">
  0.310
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.780
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.752
  </td>
   
   <td class="ee-details">
  6.070
  </td>
   
   <td class="ee-details">
  19.226
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0016.jpg">temple_3_0016</a></td>
   
   <td class="ae">
  0.256
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.221
  </td>
   
   <td class="ae-details">
  0.261
  </td>
   
   <td class="ae-details">
  0.249
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  5.940
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.942
  </td>
   
   <td class="ee-details">
  6.009
  </td>
   
   <td class="ee-details">
  26.126
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.125
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0017.jpg">temple_3_0017</a></td>
   
   <td class="ae">
  0.277
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.316
  </td>
   
   <td class="ae-details">
  0.273
  </td>
   
   <td class="ae-details">
  0.197
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  6.642
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.599
  </td>
   
   <td class="ee-details">
  6.990
  </td>
   
   <td class="ee-details">
  13.323
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.092
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0018.jpg">temple_3_0018</a></td>
   
   <td class="ae">
  0.301
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.315
  </td>
   
   <td class="ae-details">
  0.295
  </td>
   
   <td class="ae-details">
  0.361
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  7.797
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.235
  </td>
   
   <td class="ee-details">
  7.361
  </td>
   
   <td class="ee-details">
  23.879
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.084
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0019.jpg">temple_3_0019</a></td>
   
   <td class="ae">
  0.454
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.514
  </td>
   
   <td class="ae-details">
  0.449
  </td>
   
   <td class="ae-details">
  0.419
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  11.945
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.195
  </td>
   
   <td class="ee-details">
  9.547
  </td>
   
   <td class="ee-details">
  36.600
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.076
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0020.jpg">temple_3_0020</a></td>
   
   <td class="ae">
  0.773
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.656
  </td>
   
   <td class="ae-details">
  0.805
  </td>
   
   <td class="ae-details">
  0.745
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  22.575
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  3.220
  </td>
   
   <td class="ee-details">
  16.115
  </td>
   
   <td class="ee-details">
  47.238
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.063
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0021.jpg">temple_3_0021</a></td>
   
   <td class="ae">
  0.905
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.604
  </td>
   
   <td class="ae-details">
  1.110
  </td>
   
   <td class="ae-details">
  0.728
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  34.300
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.981
  </td>
   
   <td class="ee-details">
  17.727
  </td>
   
   <td class="ee-details">
  65.409
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.109
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0022.jpg">temple_3_0022</a></td>
   
   <td class="ae">
  1.046
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.503
  </td>
   
   <td class="ae-details">
  1.389
  </td>
   
   <td class="ae-details">
  1.002
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  53.053
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  2.746
  </td>
   
   <td class="ee-details">
  21.349
  </td>
   
   <td class="ee-details">
  85.171
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.097
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0023.jpg">temple_3_0023</a></td>
   
   <td class="ae">
  0.987
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.402
  </td>
   
   <td class="ae-details">
  1.254
  </td>
   
   <td class="ae-details">
  1.016
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  63.344
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.111
  </td>
   
   <td class="ee-details">
  20.591
  </td>
   
   <td class="ee-details">
  88.731
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.067
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0024.jpg">temple_3_0024</a></td>
   
   <td class="ae">
  0.727
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.526
  </td>
   
   <td class="ae-details">
  0.724
  </td>
   
   <td class="ae-details">
  0.731
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  50.579
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  7.389
  </td>
   
   <td class="ee-details">
  14.870
  </td>
   
   <td class="ee-details">
  71.023
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.071
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0025.jpg">temple_3_0025</a></td>
   
   <td class="ae">
  0.773
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.929
  </td>
   
   <td class="ae-details">
  0.902
  </td>
   
   <td class="ae-details">
  0.640
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  37.913
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  17.580
  </td>
   
   <td class="ee-details">
  17.447
  </td>
   
   <td class="ee-details">
  59.076
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.119
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0026.jpg">temple_3_0026</a></td>
   
   <td class="ae">
  0.673
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.312
  </td>
   
   <td class="ae-details">
  0.710
  </td>
   
   <td class="ae-details">
  0.621
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  28.522
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.259
  </td>
   
   <td class="ee-details">
  13.145
  </td>
   
   <td class="ee-details">
  50.668
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.105
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0027.jpg">temple_3_0027</a></td>
   
   <td class="ae">
  0.460
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.428
  </td>
   
   <td class="ae-details">
  0.516
  </td>
   
   <td class="ae-details">
  0.466
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  17.945
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  6.112
  </td>
   
   <td class="ee-details">
  14.624
  </td>
   
   <td class="ee-details">
  39.530
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.077
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0028.jpg">temple_3_0028</a></td>
   
   <td class="ae">
  0.589
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.498
  </td>
   
   <td class="ae-details">
  0.568
  </td>
   
   <td class="ae-details">
  0.595
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  20.751
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  13.217
  </td>
   
   <td class="ee-details">
  11.517
  </td>
   
   <td class="ee-details">
  46.023
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.065
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0029.jpg">temple_3_0029</a></td>
   
   <td class="ae">
  0.844
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.747
  </td>
   
   <td class="ae-details">
  0.767
  </td>
   
   <td class="ae-details">
  1.078
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  28.963
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  8.012
  </td>
   
   <td class="ee-details">
  18.642
  </td>
   
   <td class="ee-details">
  62.083
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.103
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0030.jpg">temple_3_0030</a></td>
   
   <td class="ae">
  0.756
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.013
  </td>
   
   <td class="ae-details">
  0.709
  </td>
   
   <td class="ae-details">
  0.896
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  26.876
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  10.670
  </td>
   
   <td class="ee-details">
  18.461
  </td>
   
   <td class="ee-details">
  54.219
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.087
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0031.jpg">temple_3_0031</a></td>
   
   <td class="ae">
  0.600
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.138
  </td>
   
   <td class="ae-details">
  0.535
  </td>
   
   <td class="ae-details">
  0.744
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  28.004
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  25.001
  </td>
   
   <td class="ee-details">
  11.141
  </td>
   
   <td class="ee-details">
  68.236
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0032.jpg">temple_3_0032</a></td>
   
   <td class="ae">
  0.650
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.588
  </td>
   
   <td class="ae-details">
  0.634
  </td>
   
   <td class="ae-details">
  0.715
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  28.738
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  4.591
  </td>
   
   <td class="ee-details">
  15.579
  </td>
   
   <td class="ee-details">
  78.480
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0033.jpg">temple_3_0033</a></td>
   
   <td class="ae">
  0.604
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.731
  </td>
   
   <td class="ae-details">
  0.312
  </td>
   
   <td class="ae-details">
  0.757
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  26.222
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  6.132
  </td>
   
   <td class="ee-details">
  10.111
  </td>
   
   <td class="ee-details">
  35.542
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.139
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0034.jpg">temple_3_0034</a></td>
   
   <td class="ae">
  0.461
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.466
  </td>
   
   <td class="ae-details">
  0.417
  </td>
   
   <td class="ae-details">
  0.713
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  23.050
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  5.100
  </td>
   
   <td class="ee-details">
  18.792
  </td>
   
   <td class="ee-details">
  48.221
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.101
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0035.jpg">temple_3_0035</a></td>
   
   <td class="ae">
  0.828
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.709
  </td>
   
   <td class="ae-details">
  0.560
  </td>
   
   <td class="ae-details">
  1.212
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  21.519
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  5.036
  </td>
   
   <td class="ee-details">
  15.548
  </td>
   
   <td class="ee-details">
  55.643
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.079
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0036.jpg">temple_3_0036</a></td>
   
   <td class="ae">
  0.945
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.640
  </td>
   
   <td class="ae-details">
  0.798
  </td>
   
   <td class="ae-details">
  1.237
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  34.898
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  5.898
  </td>
   
   <td class="ee-details">
  15.415
  </td>
   
   <td class="ee-details">
  72.769
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.067
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0037.jpg">temple_3_0037</a></td>
   
   <td class="ae">
  1.149
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  1.012
  </td>
   
   <td class="ae-details">
  1.224
  </td>
   
   <td class="ae-details">
  0.992
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  48.916
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  9.024
  </td>
   
   <td class="ee-details">
  31.944
  </td>
   
   <td class="ee-details">
  90.512
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.122
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0038.jpg">temple_3_0038</a></td>
   
   <td class="ae">
  1.037
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.886
  </td>
   
   <td class="ae-details">
  0.370
  </td>
   
   <td class="ae-details">
  1.161
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  56.869
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  13.832
  </td>
   
   <td class="ee-details">
  13.005
  </td>
   
   <td class="ee-details">
  65.008
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.088
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0039.jpg">temple_3_0039</a></td>
   
   <td class="ae">
  0.846
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.440
  </td>
   
   <td class="ae-details">
  0.879
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  69.870
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  12.299
  </td>
   
   <td class="ee-details">
  74.547
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.080
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0040.jpg">temple_3_0040</a></td>
   
   <td class="ae">
  0.993
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.319
  </td>
   
   <td class="ae-details">
  1.059
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  77.923
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  9.694
  </td>
   
   <td class="ee-details">
  84.603
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0041.jpg">temple_3_0041</a></td>
   
   <td class="ae">
  1.246
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.439
  </td>
   
   <td class="ae-details">
  0.191
  </td>
   
   <td class="ae-details">
  1.404
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  86.317
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  18.197
  </td>
   
   <td class="ee-details">
  8.044
  </td>
   
   <td class="ee-details">
  98.070
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.111
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0042.jpg">temple_3_0042</a></td>
   
   <td class="ae">
  1.257
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.811
  </td>
   
   <td class="ae-details">
  1.319
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  91.506
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  24.552
  </td>
   
   <td class="ee-details">
  100.933
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.090
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0043.jpg">temple_3_0043</a></td>
   
   <td class="ae">
  1.097
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.836
  </td>
   
   <td class="ae-details">
  1.128
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  79.522
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  28.193
  </td>
   
   <td class="ee-details">
  85.667
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.072
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0044.jpg">temple_3_0044</a></td>
   
   <td class="ae">
  1.019
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.563
  </td>
   
   <td class="ae-details">
  1.113
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  69.324
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  21.219
  </td>
   
   <td class="ee-details">
  79.262
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.073
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0045.jpg">temple_3_0045</a></td>
   
   <td class="ae">
  0.874
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.299
  </td>
   
   <td class="ae-details">
  1.044
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  63.898
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  14.453
  </td>
   
   <td class="ee-details">
  78.537
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.114
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0046.jpg">temple_3_0046</a></td>
   
   <td class="ae">
  0.887
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.203
  </td>
   
   <td class="ae-details">
  1.121
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  58.962
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  11.660
  </td>
   
   <td class="ee-details">
  75.120
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.090
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0047.jpg">temple_3_0047</a></td>
   
   <td class="ae">
  0.656
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.090
  </td>
   
   <td class="ae-details">
  0.865
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  50.099
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  8.894
  </td>
   
   <td class="ee-details">
  65.241
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.085
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0048.jpg">temple_3_0048</a></td>
   
   <td class="ae">
  0.567
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  n/a
  </td>
   
   <td class="ae-details">
  0.400
  </td>
   
   <td class="ae-details">
  0.680
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  44.488
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  n/a
  </td>
   
   <td class="ee-details">
  15.514
  </td>
   
   <td class="ee-details">
  64.118
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.074
  </td>
      </tr>  
    
      <tr>
        
   <td class="id right-sep"><a href="https://s3-us-west-1.amazonaws.com/flowthrone-data/pwcnet-v1/temple_3_0049.jpg">temple_3_0049</a></td>
   
   <td class="ae">
  0.605
  </td>
   <!-- interval ranges for angular errors -->  
   
   <td class="ae-details">
  0.248
  </td>
   
   <td class="ae-details">
  0.388
  </td>
   
   <td class="ae-details">
  0.754
  </td>
   
   <!-- -->
   <td class="ee left-sep">
  41.023
  </td>
   <!-- interval ranges for endpoint errors -->  
   
   <td class="ee-details">
  15.574
  </td>
   
   <td class="ee-details">
  12.875
  </td>
   
   <td class="ee-details">
  60.342
  </td>
   
   <!-- -->
   <td class="elapsed left-sep">
  1.127
  </td>
      </tr>  
