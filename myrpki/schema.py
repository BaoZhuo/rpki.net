import lxml.etree
myrpki = lxml.etree.RelaxNG(lxml.etree.fromstring('''<?xml version="1.0" encoding="UTF-8"?>
<!--
  $Id: schema.rnc 2625 2009-07-16 04:32:25Z sra $
  
  RelaxNG Schema for MyRPKI XML messages
  
  libxml2 (including xmllint) only groks the XML syntax of RelaxNG, so
  run the compact syntax through trang to get XML syntax.
-->
<grammar ns="http://www.hactrn.net/uris/rpki/myrpki/" xmlns="http://relaxng.org/ns/structure/1.0" datatypeLibrary="http://www.w3.org/2001/XMLSchema-datatypes">
  <define name="base64">
    <data type="base64Binary">
      <param name="maxLength">512000</param>
    </data>
  </define>
  <define name="object_handle">
    <data type="string">
      <param name="maxLength">255</param>
      <param name="pattern">[\-_A-Za-z0-9]*</param>
    </data>
  </define>
  <define name="uri">
    <data type="anyURI">
      <param name="maxLength">4096</param>
    </data>
  </define>
  <define name="asn_list">
    <data type="string">
      <param name="maxLength">512000</param>
      <param name="pattern">[\-,0-9]*</param>
    </data>
  </define>
  <define name="ipv4_list">
    <data type="string">
      <param name="maxLength">512000</param>
      <param name="pattern">[\-,0-9/.]*</param>
    </data>
  </define>
  <define name="ipv6_list">
    <data type="string">
      <param name="maxLength">512000</param>
      <param name="pattern">[\-,0-9/:a-fA-F]*</param>
    </data>
  </define>
  <start>
    <element name="myrpki">
      <attribute name="version">
        <data type="positiveInteger">
          <param name="maxInclusive">1</param>
        </data>
      </attribute>
      <attribute name="handle">
        <ref name="object_handle"/>
      </attribute>
      <zeroOrMore>
        <ref name="roa_request_elt"/>
      </zeroOrMore>
      <zeroOrMore>
        <ref name="child_elt"/>
      </zeroOrMore>
      <zeroOrMore>
        <ref name="parent_elt"/>
      </zeroOrMore>
      <optional>
        <ref name="bpki_ca_certificate_elt"/>
      </optional>
      <optional>
        <ref name="bpki_crl_elt"/>
      </optional>
      <optional>
        <ref name="bpki_repository_certificate_elt"/>
      </optional>
      <optional>
        <ref name="bpki_bsc_certificate_elt"/>
      </optional>
      <optional>
        <ref name="bpki_bsc_pkcs10_elt"/>
      </optional>
    </element>
  </start>
  <define name="roa_request_elt">
    <element name="roa_request">
      <attribute name="asn">
        <data type="positiveInteger"/>
      </attribute>
      <attribute name="v4">
        <ref name="ipv4_list"/>
      </attribute>
      <attribute name="v6">
        <ref name="ipv6_list"/>
      </attribute>
    </element>
  </define>
  <define name="child_elt">
    <element name="child">
      <attribute name="handle">
        <ref name="object_handle"/>
      </attribute>
      <attribute name="valid_until">
        <data type="dateTime">
          <param name="pattern">.*Z</param>
        </data>
      </attribute>
      <optional>
        <attribute name="asns">
          <ref name="asn_list"/>
        </attribute>
      </optional>
      <optional>
        <attribute name="v4">
          <ref name="ipv4_list"/>
        </attribute>
      </optional>
      <optional>
        <attribute name="v6">
          <ref name="ipv6_list"/>
        </attribute>
      </optional>
      <optional>
        <element name="bpki_certificate">
          <ref name="base64"/>
        </element>
      </optional>
    </element>
  </define>
  <define name="parent_elt">
    <element name="parent">
      <attribute name="handle">
        <ref name="object_handle"/>
      </attribute>
      <optional>
        <attribute name="service_uri">
          <ref name="uri"/>
        </attribute>
      </optional>
      <optional>
        <element name="bpki_cms_certificate">
          <ref name="base64"/>
        </element>
      </optional>
      <optional>
        <element name="bpki_https_certificate">
          <ref name="base64"/>
        </element>
      </optional>
    </element>
  </define>
  <define name="bpki_ca_certificate_elt">
    <element name="bpki_ca_certificate">
      <ref name="base64"/>
    </element>
  </define>
  <define name="bpki_crl_elt">
    <element name="bpki_crl">
      <ref name="base64"/>
    </element>
  </define>
  <define name="bpki_repository_certificate_elt">
    <element name="bpki_repository_certificate">
      <ref name="base64"/>
    </element>
  </define>
  <define name="bpki_bsc_certificate_elt">
    <element name="bpki_bsc_certificate">
      <ref name="base64"/>
    </element>
  </define>
  <define name="bpki_bsc_pkcs10_elt">
    <element name="bpki_bsc_pkcs10">
      <ref name="base64"/>
    </element>
  </define>
</grammar>
<!--
  Local Variables:
  indent-tabs-mode: nil
  End:
-->
'''))