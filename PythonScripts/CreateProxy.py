import io
pram ="""<?xml version="1.0" encoding="UTF-8"?>
<proxy  name="vfs_{0}" xmlns="http://ws.apache.org/ns/synapse">
        <target>
            <inSequence>
                <property name="transport.vfs.ReplyFileName"
                          expression="fn:concat(fn:substring-after(get-property('MessageID'), 'urn:uuid:'), '.xml')"
                          scope="transport"/>
                <property name="FORCE_SC_ACCEPTED" value="true" scope="axis2"/>
                <property action="set" name="OUT_ONLY" value="true"/>
                <send>
                    <endpoint>
               <address uri="vfs:file:///Users/vsivajothy/Area51/APACHE/SynapseTestBed/VFS/Out/client_{0}-test/"
                        format="pox"/>
            </endpoint>
                </send>
            </inSequence>
            <outSequence>
                <send/>
            </outSequence>
        </target>
        <publishWSDL uri="file:repository/conf/sample/resources/proxy/sample_proxy_1.wsdl"/>
</proxy>"""
for i in range(1001, 1501):
   with open('vfs_{0}.xml'.format(i),'w') as f:
       f.write(str(pram.format(i)))
