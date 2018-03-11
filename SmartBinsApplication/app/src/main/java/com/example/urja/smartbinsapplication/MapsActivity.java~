package com.example.urja.smartbinsapplication;

import android.Manifest;
import android.annotation.SuppressLint;
import android.content.pm.PackageManager;
import android.graphics.Color;
import android.os.AsyncTask;
import android.support.annotation.NonNull;
import android.support.v4.app.ActivityCompat;
import android.support.v4.app.FragmentActivity;
import android.os.Bundle;
import android.util.Log;
import android.widget.Toast;

import com.android.volley.NetworkResponse;
import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.BitmapDescriptor;
import com.google.android.gms.maps.model.BitmapDescriptorFactory;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;
import com.google.android.gms.maps.model.PolylineOptions;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URL;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class MapsActivity extends FragmentActivity implements OnMapReadyCallback {

    private GoogleMap mMap;
    private static final int LOCATION_REQUEST=500;
    ArrayList<LatLng> listpoints;
    String URL = "https://bin-flaskapp.herokuapp.com/generateReport";
    LatLng latLng[];
    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_maps);
        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        final CustomRequest jsObjRequest = new CustomRequest(Request.Method.GET, URL, new Response.Listener<NetworkResponse>() {
            @Override
            public void onResponse(NetworkResponse response)
            {
                String resultResponse = new String(response.data);
                try
                {
                    JSONObject result=new JSONObject(resultResponse);
                    JSONArray binArray=result.getJSONArray("result");
                    latLng=new LatLng[binArray.length()];
                    for(int i=0;i<binArray.length();i++)
                    {
                        JSONObject jsonObject=binArray.getJSONObject(i);
                        double lat=jsonObject.getDouble("latitude");
                        double lon=jsonObject.getDouble("longitude");
                        latLng[i]=new LatLng(lat,lon);
                    }
                    Log.i("tag",""+latLng.length);
                    listpoints=new ArrayList<>();
                    for(int i=0;i<latLng.length;i++)
                    {
                        listpoints.add(latLng[i]);
                        MarkerOptions markerOptions=new MarkerOptions();
                        markerOptions.position(latLng[i]);
                        markerOptions.icon(BitmapDescriptorFactory.defaultMarker(BitmapDescriptorFactory.HUE_RED));
                        mMap.addMarker(markerOptions);
                    }
                    String url = getRequestUrl(listpoints.get(0),listpoints.get(0));
                    TaskRequestDirections taskRequestDirection=new TaskRequestDirections();
                    taskRequestDirection.execute(url);
                    //Log.i("size",""+binArray.length());
                    // JSONObject data=result.getJSONObject("item");
                    /*String status=result.getString("status");
                    Log.d("tag",status);*/

                }
                catch (JSONException e)
                {
                    e.printStackTrace();
                }
                catch (Exception e)
                {
                    e.printStackTrace();
                }

            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

            }

        });

        MySingleton.getInstance(getApplicationContext()).addToRequestQueue(jsObjRequest);
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);



    }


    /**
     * Manipulates the map once available.
     * This callback is triggered when the map is ready to be used.
     * This is where we can add markers or lines, add listeners or move the camera. In this case,
     * we just add a marker near Sydney, Australia.
     * If Google Play services is not installed on the device, the user will be prompted to install
     * it inside the SupportMapFragment. This method will only be triggered once the user has
     * installed Google Play services and returned to the app.
     */
    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;

        // Add a marker in Sydney and move the camera
        mMap.getUiSettings().setZoomControlsEnabled(true);
        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
          ActivityCompat.requestPermissions(this,new String[]{Manifest.permission.ACCESS_FINE_LOCATION},LOCATION_REQUEST);

            return;
        }
        mMap.setMyLocationEnabled(true);

       /* mMap.setOnMapClickListener(new GoogleMap.OnMapClickListener() {
            @Override
            public void onMapClick(LatLng latLng) {
                if(listpoints.size() == 5)
                {
                    listpoints.clear();
                    mMap.clear();
                }
                listpoints.add(latLng);
                MarkerOptions markerOptions=new MarkerOptions();
                markerOptions.position(latLng);
                if(listpoints.size() == 1)
                {
                    markerOptions.icon(BitmapDescriptorFactory.defaultMarker(BitmapDescriptorFactory.HUE_GREEN));

                }
                else if(listpoints.size() == 2)
                {
                    markerOptions.icon(BitmapDescriptorFactory.defaultMarker(BitmapDescriptorFactory.HUE_RED));
                }
                else
                {
                    markerOptions.icon(BitmapDescriptorFactory.defaultMarker(BitmapDescriptorFactory.HUE_AZURE));
                }
                mMap.addMarker(markerOptions);
                if(listpoints.size() == 5)
                {
                    Log.i("tag",""+listpoints.get(0));
                    String url = getRequestUrl(listpoints.get(0),listpoints.get(1));
                    Log.i("url",url);
                    TaskRequestDirections taskRequestDirection=new TaskRequestDirections();
                    taskRequestDirection.execute(url);
                }
            }
        });*/
    }
    private String getRequestUrl(LatLng origin,LatLng dest)
    {
        String str_org="origin="+origin.latitude+","+origin.longitude;
        String str_dest="destination="+dest.latitude+","+dest.longitude;
        String sensor="sensor=false";
        String mode="mode=driving";
        // Waypoints
        String waypoints = "";
        for(int i=1;i<listpoints.size();i++){
            LatLng point  = (LatLng) listpoints.get(i);
            if(i==1)
                waypoints = "waypoints=optimize:true|";
            waypoints += point.latitude + "," + point.longitude + "|";
        }

        String param=str_org+"&"+str_dest+"&"+sensor+"&"+mode+"&"+waypoints;
        String output="json";
        String url="https://maps.googleapis.com/maps/api/directions/"+output+"?" + param;
        return url;

    }
    private  String requestDirection(String reqUrl) throws IOException {
        String responseString="";
        InputStream inputStream=null;
        HttpURLConnection httpURLConnections = null;
        try
        {
            URL url=new URL(reqUrl);
            httpURLConnections=(HttpURLConnection)url.openConnection();
            httpURLConnections.connect();
            inputStream=httpURLConnections.getInputStream();
            InputStreamReader   inputStreamReader=new InputStreamReader(inputStream);
            BufferedReader bufferedReader=new BufferedReader(inputStreamReader);
            StringBuffer stringBuffer=new StringBuffer();
            String line="";
            while ((line=bufferedReader.readLine()) != null)
                stringBuffer.append(line);

            responseString=stringBuffer.toString();
            bufferedReader.close();
            inputStreamReader.close();

        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
        finally {
            if(inputStream != null)
                inputStream.close();
        }
        httpURLConnections.disconnect();
        Log.i("Response",responseString);
        return responseString;
    }
    @SuppressLint("MissingPermission")
    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        switch (requestCode)
        {
            case LOCATION_REQUEST:
                if(grantResults.length > 0 && grantResults[0]==PackageManager.PERMISSION_GRANTED)
                    mMap.setMyLocationEnabled(true);
                break;
        }
    }
    public  class TaskRequestDirections extends AsyncTask<String,Void,String>
    {
        @Override
        protected String doInBackground(String... strings) {
            String responseString="";
            try {
                responseString = requestDirection(strings[0]);
            }
            catch (IOException e)
            {
                e.printStackTrace();
            }
            return responseString;

        }
        protected void onPostExecute(String s)
        {
            super.onPostExecute(s);
            TaskParser taskParser=new TaskParser();
            Log.i("path",s);
            taskParser.execute(s);
        }
    }
    public class TaskParser extends AsyncTask<String,Void,List<List<HashMap<String,String>>>>
    {
        @Override
        protected List<List<HashMap<String, String>>> doInBackground(String... strings) {
            List<List<HashMap<String,String>>> routes=null;
            JSONObject jsonObject=null;
            try {
                Log.i("string",strings[0]);
                jsonObject = new JSONObject(strings[0]);
                DirectionsJSONParser directionsJSONParser=new DirectionsJSONParser();
                routes=directionsJSONParser.parse(jsonObject);

            }
            catch (JSONException e)
            {
                e.printStackTrace();
            }
            return routes;

        }

        @Override
        protected void onPostExecute(List<List<HashMap<String, String>>> lists) {
            ArrayList points =null;
            PolylineOptions polylineOptions = null;
            Log.i("routes",""+lists);

            for(List<HashMap<String,String>> path : lists)
            {
                Log.i("path",""+path);
                points=new ArrayList();
                polylineOptions=new PolylineOptions();
                for(HashMap<String , String> point: path)
                {
                    Log.i("pont",""+point);
                    double lat=Double.parseDouble(point.get("lat"));
                    double lon=Double.parseDouble(point.get("lng"));
                    points.add(new LatLng(lat,lon));


                }
                polylineOptions.addAll(points);
                polylineOptions.width(15);
                polylineOptions.color(Color.BLUE);
                polylineOptions.geodesic(true);
            }
            if(polylineOptions != null)
                mMap.addPolyline(polylineOptions);
            else
                Toast.makeText(getApplicationContext(),"Direction not found!",Toast.LENGTH_SHORT).show();
        }
    }
}
