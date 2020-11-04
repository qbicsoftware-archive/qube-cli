package life.qbic.portal.portlet

import spock.lang.Specification

class Test extends Specification{

    def "first test"(){
        when:
        def value = 2+2
        then:
        value == 4
    }

}
